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

# Standard
from typing import Optional
import copy

# Third Party
import pytest

# Local
from caikit.core import LocalBackend
from caikit.core.module import MODULE_BACKEND_REGISTRY, MODULE_REGISTRY, ModuleBase
from caikit.core.module_backend_config import (
    _CONFIGURED_LOAD_BACKENDS,
    _CONFIGURED_TRAIN_BACKENDS,
)
from caikit.core.module_backends import BackendBase, backend_types

# Add mock backend
# This is set in the base test config's load_priority list
from caikit.core.module_backends.base import SharedLoadBackendBase


class MockBackend(BackendBase):
    backend_type = "MOCK"

    def __init__(self, config=...) -> None:
        super().__init__(config)
        self._started = False

    def start(self):
        self._started = True

    def register_config(self, config):
        self.config = {**config, **self.config}

    def stop(self):
        self._started = False


backend_types.register_backend_type(MockBackend)


# Add a new shared load backend that tests can use
class TestLoader(SharedLoadBackendBase):
    backend_type = "TESTLOADER"

    def load(self, model_path: str, *args, **kwargs) -> Optional[ModuleBase]:
        # allow config.model_type to control whether this loader barfs
        if "model_type" in self.config and "model_type" in kwargs:
            if self.config["model_type"] != kwargs["model_type"]:
                # Don't load in this loader
                return None
        # use the "Local" loader to actually load the model
        model = LocalBackend().load(model_path)
        return model

    def register_config(self, config):
        pass

    def stop(self):
        pass

    def start(self):
        pass


backend_types.register_backend_type(TestLoader)


@pytest.fixture
def reset_backend_types():
    """Fixture that will reset the backend types if a test modifies them"""
    base_backend_types = {
        key: val for key, val in backend_types.MODULE_BACKEND_TYPES.items()
    }
    base_backend_fns = {
        key: val for key, val in backend_types.MODULE_BACKEND_CONFIG_FUNCTIONS.items()
    }
    yield
    backend_types.MODULE_BACKEND_TYPES.clear()
    backend_types.MODULE_BACKEND_TYPES.update(base_backend_types)
    backend_types.MODULE_BACKEND_CONFIG_FUNCTIONS.clear()
    backend_types.MODULE_BACKEND_CONFIG_FUNCTIONS.update(base_backend_fns)


@pytest.fixture
def reset_module_backend_registry():
    """Fixture that will reset the module distribution registry if a test modifies them"""
    module_registry = {key: val for key, val in MODULE_BACKEND_REGISTRY.items()}
    yield
    MODULE_BACKEND_REGISTRY.clear()
    MODULE_BACKEND_REGISTRY.update(module_registry)


@pytest.fixture
def reset_module_registry():
    """Fixture that will reset caikit.core module registry if a test modifies it"""
    module_registry = {key: val for key, val in MODULE_REGISTRY.items()}
    yield
    MODULE_REGISTRY.clear()
    MODULE_REGISTRY.update(module_registry)


@pytest.fixture
def reset_configured_backends():
    """Fixture that will reset the configured backends"""
    load_backends_list = copy.copy(_CONFIGURED_LOAD_BACKENDS)
    train_backends_list = copy.copy(_CONFIGURED_TRAIN_BACKENDS)
    _CONFIGURED_LOAD_BACKENDS.clear()
    _CONFIGURED_TRAIN_BACKENDS.clear()
    yield
    _CONFIGURED_LOAD_BACKENDS.clear()
    _CONFIGURED_LOAD_BACKENDS.extend(load_backends_list)
    _CONFIGURED_TRAIN_BACKENDS.clear()
    _CONFIGURED_TRAIN_BACKENDS.extend(train_backends_list)


@pytest.fixture
def reset_globals(
    reset_backend_types,
    reset_configured_backends,
    reset_module_registry,
    reset_module_backend_registry,
):
    """Fixture that will reset the backend types and module registries if a test modifies them"""
