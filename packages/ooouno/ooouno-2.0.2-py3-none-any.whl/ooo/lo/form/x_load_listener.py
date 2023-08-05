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
# Namespace: com.sun.star.form
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XLoadListener(XEventListener_c7230c4a):
    """
    receives load-related events from a loadable object.
    
    The interface is typically implemented by data-bound components, which want to listen to the data source that contains their database form.

    See Also:
        `API XLoadListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XLoadListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XLoadListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XLoadListener'

    @abstractmethod
    def loaded(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the object has successfully connected to a datasource.
        """
        ...
    @abstractmethod
    def reloaded(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the object has been reloaded.
        """
        ...
    @abstractmethod
    def reloading(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the object is about to be reloaded.
        
        Components may use this to stop any other event processing related to the event source until they get the reloaded event.
        """
        ...
    @abstractmethod
    def unloaded(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked after the object has disconnected from a datasource.
        """
        ...
    @abstractmethod
    def unloading(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when the object is about to be unloaded.
        
        Components may use this to stop any other event processing related to the event source before the object is unloaded.
        """
        ...

__all__ = ['XLoadListener']

