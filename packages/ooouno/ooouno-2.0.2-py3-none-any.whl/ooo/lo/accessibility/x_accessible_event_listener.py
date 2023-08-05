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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .accessible_event_object import AccessibleEventObject as AccessibleEventObject_c61f12b7

class XAccessibleEventListener(XEventListener_c7230c4a):
    """
    makes it possible to register a component as a listener, which is called whenever an accessibility event occurs.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleEventListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleEventListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleEventListener'

    @abstractmethod
    def notifyEvent(self, aEvent: 'AccessibleEventObject_c61f12b7') -> None:
        """
        is called whenever an accessible event (see AccessibleEventObject) occurs.
        """
        ...

__all__ = ['XAccessibleEventListener']

