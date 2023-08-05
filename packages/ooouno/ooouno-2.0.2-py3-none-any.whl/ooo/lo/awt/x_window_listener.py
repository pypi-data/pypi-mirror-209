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
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .window_event import WindowEvent as WindowEvent_9a2b0ace
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XWindowListener(XEventListener_c7230c4a):
    """
    makes it possible to receive window events.
    
    Component events are provided only for notification purposes. Moves and resizes will be handled internally by the window component, so that GUI layout works properly regardless of whether a program registers such a listener or not.

    See Also:
        `API XWindowListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XWindowListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XWindowListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XWindowListener'

    @abstractmethod
    def windowHidden(self, e: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the window has been hidden.
        """
        ...
    @abstractmethod
    def windowMoved(self, e: 'WindowEvent_9a2b0ace') -> None:
        """
        is invoked when the window has been moved.
        """
        ...
    @abstractmethod
    def windowResized(self, e: 'WindowEvent_9a2b0ace') -> None:
        """
        is invoked when the window has been resized.
        """
        ...
    @abstractmethod
    def windowShown(self, e: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the window has been shown.
        """
        ...

__all__ = ['XWindowListener']

