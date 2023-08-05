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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.x_popup_menu import XPopupMenu as XPopupMenu_8ee90a55

class XPopupMenuController(XInterface_8f010a43):
    """
    provides data to a pop-up menu controller implementation to fill and update a pop-up menu dynamically.
    
    A pop-up menu controller gets a com.sun.star.awt.XPopupMenu from its parent menu implementation. The controller has to fill this pop-up menu with a set of menu items and/or sub menus. The parent menu implementation briefs the controller whenever the pop-up menu gets activated by a user.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XPopupMenuController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XPopupMenuController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XPopupMenuController'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XPopupMenuController'

    @abstractmethod
    def setPopupMenu(self, PopupMenu: 'XPopupMenu_8ee90a55') -> None:
        """
        provides a com.sun.star.awt.XPopupMenu to a pop-up menu controller implementation.
        
        The controller must fill this pop-up menu with its functions.
        """
        ...
    @abstractmethod
    def updatePopupMenu(self) -> None:
        """
        briefs the pop-up menu controller to update the contents of the provided pop-up menu to reflect the current state.
        
        A controller should never update the pop-up menu structure on its own to prevent performance problems. A better way would be that a controller registers itself as status listener to for a command URL and immediately deregister after that. Therefore status updates will not be send regularly for a non visible pop-up menu.
        """
        ...

__all__ = ['XPopupMenuController']

