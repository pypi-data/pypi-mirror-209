# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module defines the @schema decorator which can be used to declare data
model objects inline without manually defining the protobufs representation
"""


# Standard
from enum import Enum
from typing import Any, Callable, List, Type, Union, get_args, get_origin
import dataclasses

# Third Party
from google.protobuf import message as _message
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

# First Party
from py_to_proto.dataclass_to_proto import DataclassConverter
import alog
import py_to_proto

# Local
from ..toolkit.errors import error_handler
from . import enums
from .base import DataBase, _DataBaseMetaClass

## Globals #####################################################################

log = alog.use_channel("SCHEMA")
error = error_handler.get(log)

# Common package prefix
CAIKIT_DATA_MODEL = "caikit_data_model"

# Registry of auto-generated protos so that they can be rendered to .proto
_AUTO_GEN_PROTO_CLASSES = []

# Special attribute used to indicate which defaults are user provided
_USER_DEFINED_DEFAULTS = "__user_defined_defaults__"

## Public ######################################################################


class _DataObjectBaseMetaClass(_DataBaseMetaClass):
    """This metaclass is used for the DataObject base class so that all data
    objects can delay the creation of their proto class until after the
    metaclass has been instantiated.
    """

    def __new__(mcs, name, bases, attrs):
        """When instantiating a new DataObject class, the proto class will not
        yet have been generated, but the set of fields will be known since the
        class will be the raw input representation of a @dataclass
        """

        # Get the annotations that will go into the dataclass
        if name != "DataObjectBase":
            raw_field_names = attrs.get("__annotations__")
            if raw_field_names is None:
                raise TypeError(
                    "All DataObjectBase classes must follow dataclass syntax"
                )

            # TODO: Sort out oneof field names
            field_names = list(raw_field_names.keys())

            # Add the forward declaration
            attrs[_DataBaseMetaClass._FWD_DECL_FIELDS] = field_names

        # Delegate to the base metaclass
        return super().__new__(mcs, name, bases, attrs)


class DataObjectBase(DataBase, metaclass=_DataObjectBaseMetaClass):
    """A DataObject is a data model class that is backed by a @dataclass.

    Data model classes that use the @dataobject decorator must derive from this
    base class.
    """


def dataobject(*args, **kwargs) -> Callable[[Type], Type[DataBase]]:
    """The @dataobject decorator can be used to define a Data Model object's
    schema inline with the definition of the python class rather than needing to
    bind to a pre-compiled protobufs class. For example:

    @dataobject("foo.bar")
    @dataclass
    class MyDataObject(DataObjectBase):
        '''My Custom Data Object'''
        foo: str
        bar: int

    NOTE: The wrapped class must NOT inherit directly from DataBase. That
        inheritance will be added by this decorator, but if it is written
        directly, the metaclass that links protobufs to the class will be called
        before this decorator can auto-gen the protobufs class.

    Args:
        package:  str
            The package name to use for the generated protobufs class

    Returns:
        decorator:  Callable[[Type], Type[DataBase]]
            The decorator function that will wrap the given class
    """

    def decorator(cls: Type) -> Type[DataBase]:
        # Make sure that the wrapped class does NOT inherit from DataBase
        error.value_check(
            "<COR95184230E>",
            issubclass(cls, (DataObjectBase, Enum)),
            "{} must inherit from DataObjectBase/Enum when using @dataobject",
            cls.__name__,
        )

        # Add the package to the kwargs
        kwargs.setdefault("package", package)

        # If there's a schema in the keyword args, use jtd_to_proto
        schema = kwargs.pop("schema", None)
        if schema is not None:
            log.debug("Using JTD To Proto")
            kwargs.setdefault("validate_jtd", True)
            descriptor = py_to_proto.jtd_to_proto(
                name=cls.__name__,
                jtd_def=schema,
                **kwargs,
            )
        # If it's already a dataclass, convert it directly
        else:
            log.debug("Using dataclass/enum to proto on dataclass")

            # If it's not an enum, fill in any missing field defaults as None
            # and make sure it's a dataclass
            if not issubclass(cls, Enum):
                log.debug2("Wrapping data class %s", cls)
                user_defined_defaults = {}
                for annotation in getattr(cls, "__annotations__", {}):
                    user_defined_default = getattr(cls, annotation, dataclasses.MISSING)
                    if user_defined_default == dataclasses.MISSING:
                        log.debug3("Filling in None default for %s.%s", cls, annotation)
                        setattr(cls, annotation, None)
                    else:
                        user_defined_defaults[annotation] = user_defined_default
                # If the current __init__ is auto-generated by dataclass, remove
                # it so that a new one is created with the new defaults. This is
                # a little hard to detect across different python versions, so
                # the most reliable way is to assume that the only place
                # __annotations__ are added to the __init__ function itself are
                # in dataclass. If cls is either not a dataclass or is a
                # dataclass with a non-default __init__, there will not be
                # annotations
                if getattr(cls.__init__, "__annotations__", None):
                    log.debug3("Resetting default dataclass init")
                    delattr(cls, "__init__")
                cls = dataclasses.dataclass(cls)
                setattr(cls, _USER_DEFINED_DEFAULTS, user_defined_defaults)

            descriptor = _dataobject_to_proto(dataclass_=cls, **kwargs)

        # Create the message class from the dataclass
        proto_class = py_to_proto.descriptor_to_message_class(descriptor)
        _AUTO_GEN_PROTO_CLASSES.append(proto_class)

        # Add enums to the global enums module
        for enum_class in _get_all_enums(proto_class):
            log.debug2("Importing enum [%s]", enum_class.DESCRIPTOR.name)
            enums.import_enum(enum_class)

        # Declare the merged class that binds DataBase to the wrapped class with
        # this generated proto class
        if isinstance(proto_class, type):
            setattr(cls, "_proto_class", proto_class)
            cls = _make_data_model_class(proto_class, cls)
        else:
            enums.import_enum(proto_class, cls)
            setattr(cls, "_proto_enum", proto_class)

        # Return the decorated class
        return cls

    # If called without the function invocation, fill in the default argument
    if args and callable(args[0]):
        assert not kwargs, "This shouldn't happen!"
        package = CAIKIT_DATA_MODEL
        return decorator(args[0])

    # Pull the package as an arg or a keyword arg
    if args:
        package = args[0]
        if "package" in kwargs:
            raise TypeError("Got multiple values for argument 'package'")
    else:
        package = kwargs.get("package", CAIKIT_DATA_MODEL)
    return decorator


def render_dataobject_protos(interfaces_dir: str):
    """Write out protobufs files for all proto classes generated from dataobjects
    to the target interfaces directory

    Args:
        interfaces_dir:  str
            The target directory (must already exist)
    """
    for proto_class in _AUTO_GEN_PROTO_CLASSES:
        proto_class.write_proto_file(interfaces_dir)


## Implementation Details ######################################################


def _dataobject_to_proto(*args, **kwargs):
    return _DataobjectConverter(*args, **kwargs).descriptor


class _DataobjectConverter(DataclassConverter):
    """Augment the dataclass converter to be able to pull descriptors from
    existing data objects
    """

    def get_concrete_type(self, entry: Any) -> Any:
        """Also include data model classes and enums as concrete types"""
        unwrapped = self._resolve_wrapped_type(entry)
        if (
            isinstance(unwrapped, type)
            and issubclass(unwrapped, DataBase)
            and unwrapped._proto_class is not None
        ) or hasattr(unwrapped, "_proto_enum"):
            return entry
        return super().get_concrete_type(entry)

    def get_descriptor(self, entry: Any) -> Any:
        """Unpack data model classes and enums to their descriptors"""
        entry = self._resolve_wrapped_type(entry)
        if isinstance(entry, type) and issubclass(entry, DataBase):
            return entry._proto_class.DESCRIPTOR
        proto_enum = getattr(entry, "_proto_enum", None)
        if proto_enum is not None:
            return proto_enum.DESCRIPTOR
        return super().get_descriptor(entry)

    def get_optional_field_names(self, entry: Any) -> List[str]:
        """Get the names of any fields which are optional. This will be any
        field that has a user-defined default or is marked as Optional[]
        """
        optional_fields = list(getattr(entry, _USER_DEFINED_DEFAULTS, {}))
        for field_name, field in entry.__dataclass_fields__.items():
            if (
                field_name not in optional_fields
                and self._is_python_optional(field.type) is not None
            ):
                optional_fields.append(field_name)
        return optional_fields

    @staticmethod
    def _is_python_optional(entry: Any) -> Any:
        """Detect if this type is a python optional"""
        if get_origin(entry) is Union:
            args = get_args(entry)
            return type(None) in args


def _get_all_enums(
    proto_class: Union[_message.Message, EnumTypeWrapper],
) -> List[EnumTypeWrapper]:
    """Given a generated proto class, recursively extract all enums"""
    all_enums = []
    if isinstance(proto_class, EnumTypeWrapper):
        all_enums.append(proto_class)
    else:
        for enum_descriptor in proto_class.DESCRIPTOR.enum_types:
            all_enums.append(getattr(proto_class, enum_descriptor.name))
        for nested_proto_descriptor in proto_class.DESCRIPTOR.nested_types:
            all_enums.extend(
                _get_all_enums(getattr(proto_class, nested_proto_descriptor.name))
            )

    return all_enums


def _make_data_model_class(proto_class, cls):
    if issubclass(cls, DataObjectBase):
        _DataBaseMetaClass.parse_proto_descriptor(cls)

    # Recursively make all nested message wrappers
    for nested_message_descriptor in proto_class.DESCRIPTOR.nested_types:
        nested_message_name = nested_message_descriptor.name
        nested_proto_class = getattr(proto_class, nested_message_name)
        setattr(
            cls,
            nested_message_name,
            _make_data_model_class(
                nested_proto_class,
                _DataBaseMetaClass.__new__(
                    _DataBaseMetaClass,
                    name=nested_message_name,
                    bases=(DataBase,),
                    attrs={"_proto_class": getattr(proto_class, nested_message_name)},
                ),
            ),
        )
    for nested_enum_descriptor in proto_class.DESCRIPTOR.enum_types:
        setattr(
            cls,
            nested_enum_descriptor.name,
            getattr(enums, nested_enum_descriptor.name),
        )

    return cls
