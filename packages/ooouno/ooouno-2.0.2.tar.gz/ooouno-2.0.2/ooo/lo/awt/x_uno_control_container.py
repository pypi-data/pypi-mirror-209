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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_tab_controller import XTabController as XTabController_bacd0be7

class XUnoControlContainer(XInterface_8f010a43):
    """
    gives access to the tab controllers of a UnoControlContainer.

    See Also:
        `API XUnoControlContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XUnoControlContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XUnoControlContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XUnoControlContainer'

    @abstractmethod
    def addTabController(self, TabController: 'XTabController_bacd0be7') -> None:
        """
        adds a single tab controller.
        """
        ...
    @abstractmethod
    def getTabControllers(self) -> 'typing.Tuple[XTabController_bacd0be7, ...]':
        """
        returns all currently specified tab controllers.
        """
        ...
    @abstractmethod
    def removeTabController(self, TabController: 'XTabController_bacd0be7') -> None:
        """
        removes a single tab controller.
        """
        ...
    @abstractmethod
    def setTabControllers(self, TabControllers: 'typing.Tuple[XTabController_bacd0be7, ...]') -> None:
        """
        sets a set of tab controllers.
        """
        ...

__all__ = ['XUnoControlContainer']

