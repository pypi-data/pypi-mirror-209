# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing.framework
import typing
from abc import abstractmethod
from .x_module_controller import XModuleController as XModuleController_c5d112d2
if typing.TYPE_CHECKING:
    from ...frame.x_controller import XController as XController_b00e0b8f

class ModuleController(XModuleController_c5d112d2):
    """
    Service Class

    See XModuleController for a description of the module controller.
    
    See ConfigurationController for a comment why this service may be removed in the future.
    
    The ModuleController object for an application can be obtained via the XControllerManager interface.

    See Also:
        `API ModuleController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1ModuleController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.ModuleController'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, xController: 'XController_b00e0b8f') -> None:
        """
        Create a new instance of a ModuleController as sub controller of the given XController object.
        """
        ...

__all__ = ['ModuleController']

