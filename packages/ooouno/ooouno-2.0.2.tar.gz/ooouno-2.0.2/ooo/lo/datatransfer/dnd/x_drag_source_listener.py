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
# Namespace: com.sun.star.datatransfer.dnd
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .drag_source_drag_event import DragSourceDragEvent as DragSourceDragEvent_d53c12da
    from .drag_source_drop_event import DragSourceDropEvent as DragSourceDropEvent_d5d412f1
    from .drag_source_event import DragSourceEvent as DragSourceEvent_8ccf115c

class XDragSourceListener(XEventListener_c7230c4a):
    """
    This interface must be implemented by any drag gesture recognizer implementation that a drag source supports.

    See Also:
        `API XDragSourceListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDragSourceListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.XDragSourceListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.XDragSourceListener'

    @abstractmethod
    def dragDropEnd(self, dsde: 'DragSourceDropEvent_d5d412f1') -> None:
        """
        This method is invoked to signify that the Drag and Drop operation is complete.
        """
        ...
    @abstractmethod
    def dragEnter(self, dsde: 'DragSourceDragEvent_d53c12da') -> None:
        """
        Called as the hotspot enters a platform dependent drop site.
        
        NOTE: currently this notification can not be ensured by all implementations. Do not rely on it !
        """
        ...
    @abstractmethod
    def dragExit(self, dse: 'DragSourceEvent_8ccf115c') -> None:
        """
        Called as the hotspot exits a platform dependent drop site.
        
        NOTE: Currently this notification can not be ensured by all implementations. Do not rely on it !
        """
        ...
    @abstractmethod
    def dragOver(self, dsde: 'DragSourceDragEvent_d53c12da') -> None:
        """
        Called as the hotspot moves over a platform dependent drop site.
        """
        ...
    @abstractmethod
    def dropActionChanged(self, dsde: 'DragSourceDragEvent_d53c12da') -> None:
        """
        Called when the user has modified the drop gesture.
        """
        ...

__all__ = ['XDragSourceListener']

