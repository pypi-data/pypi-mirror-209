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
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0

class XSystemChildFactory(XInterface_8f010a43):
    """
    specifies a factory interface for creating system child windows.

    See Also:
        `API XSystemChildFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XSystemChildFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XSystemChildFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XSystemChildFactory'

    @abstractmethod
    def createSystemChild(self, Parent: object, ProcessId: uno.ByteSequence, SystemType: int) -> 'XWindowPeer_99760ab0':
        """
        creates a system child window.
        
        You must check the machine ID and the process ID.WIN32: HWND.WIN16: HWND.
        
        JAVA: global reference to a java.awt.Component object provided from the JNI-API.
        
        MAC: (NSView*) pointer.
        """
        ...

__all__ = ['XSystemChildFactory']

