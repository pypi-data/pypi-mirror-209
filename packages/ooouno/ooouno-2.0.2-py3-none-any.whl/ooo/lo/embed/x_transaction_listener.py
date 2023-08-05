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
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XTransactionListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events when a transacted object is committed or reverted.

    See Also:
        `API XTransactionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XTransactionListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XTransactionListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XTransactionListener'

    @abstractmethod
    def commited(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is called after the object is committed.
        """
        ...
    @abstractmethod
    def preCommit(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is called just before the object is committed.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def preRevert(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is called just before the object is reverted.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def reverted(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is called after the object is reverted.
        """
        ...

__all__ = ['XTransactionListener']

