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
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XAutoscroll(XInterface_8f010a43):
    """
    Interface for autoscroll support.
    
    During Drag and Drop operations it is possible that a user may wish to drop the subject of the operation on a region of a scrollable GUI control that is not currently visible to the user.
    
    In such situations it is desirable that the GUI control detect this and institute a scroll operation in order to make obscured region(s) visible to the user. This feature is known as autoscrolling.
    
    If a GUI control is both an active DropTarget and is also scrollable, it can receive notifications of autoscrolling gestures by the user from the Drag and Drop system by implementing this interface.
    
    An autoscrolling gesture is initiated by the user by keeping the drag cursor motionless with a border region of the Component, referred to as the \"autoscrolling region\", for a predefined period of time, this will result in repeated scroll requests to the Component until the drag Cursor resumes its motion.

    See Also:
        `API XAutoscroll <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XAutoscroll.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.XAutoscroll'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.XAutoscroll'

    @abstractmethod
    def autoscroll(self, cursorLocationX: int, cursorLocationY: int) -> None:
        """
        Notify the component to autoscroll.
        """
        ...
    @abstractmethod
    def getAutoscrollRegion(self) -> object:
        """
        Returns the regions describing the autoscrolling region.
        """
        ...

__all__ = ['XAutoscroll']

