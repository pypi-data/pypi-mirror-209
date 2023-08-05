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
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..accessibility.x_accessible import XAccessible as XAccessible_1cbc0eb6
    from ..awt.x_window import XWindow as XWindow_713b0924

class XToolPanel(ABC):
    """
    describes the basic interface to be implemented by a tool panel

    See Also:
        `API XToolPanel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XToolPanel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XToolPanel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XToolPanel'

    @abstractmethod
    def createAccessible(self, ParentAccessible: 'XAccessible_1cbc0eb6') -> 'XAccessible_1cbc0eb6':
        """
        creates the root of the Accessibility object tree for the tool panel
        """
        ...
    @abstractproperty
    def Window(self) -> 'XWindow_713b0924':
        """
        provides access to the tool panel's main window.
        
        It is allowed for an implementation to return NULL here, but in this case some functionality, for instance automatic positioning of the tool panel, might not be available, and must be implemented by the tool panel itself.
        """
        ...


__all__ = ['XToolPanel']

