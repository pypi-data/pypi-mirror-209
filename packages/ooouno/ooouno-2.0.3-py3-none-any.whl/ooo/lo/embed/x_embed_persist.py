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
from .x_common_embed_persist import XCommonEmbedPersist as XCommonEmbedPersist_16930e8d
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_storage import XStorage as XStorage_8e460a32

class XEmbedPersist(XCommonEmbedPersist_16930e8d):
    """
    specifies an implementation for embedded object persistence.
    
    The idea is that any usable embedded object should be initialized with an entry in the parent storage that will be used as persistent representation.

    See Also:
        `API XEmbedPersist <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEmbedPersist.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XEmbedPersist'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XEmbedPersist'

    @abstractmethod
    def getEntryName(self) -> str:
        """
        allows to retrieve the current object entry name.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
        ...
    @abstractmethod
    def hasEntry(self) -> bool:
        """
        allows to detect if the object has entry.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
        ...
    @abstractmethod
    def saveCompleted(self, bUseNew: bool) -> None:
        """
        specifies whether the object should use an old storage or a new one after \"save as\" operation.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def setPersistentEntry(self, xStorage: 'XStorage_8e460a32', sEntName: str, nEntryConnectionMode: int, aMediaArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]', aObjectArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        provides object with a parent storage and a name for object's entry.
        
        An entry with the specified name should be created/opened inside provided storage. It can be a storage or a stream. For example, OOo API will refer to OLE storages only by streams, but the object implementation will use storage based on this stream.
        
        Factory does this call to initialize the embedded object. The linked object can be initialized by factory in different way ( internally ).
        
        It is also possible to switch object persistent representation through this call. Actually this is the way, this call can be used by user ( since initialization is done by factory ).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def storeAsEntry(self, xStorage: 'XStorage_8e460a32', sEntName: str, aMediaArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]', aObjectArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        lets the object store itself to an entry in destination storage and prepare to use the new entry for own persistence.
        
        The object should be stored to the new entry, after that the entry should be remembered by the object. After the storing process is finished the XEmbedPersist.saveCompleted() method can be used to specify whether the object should use the new entry or the old one. The object persistence can not be used until XEmbedPersist.saveCompleted() is called. So this state can be treated as \"HandsOff\" state.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def storeToEntry(self, xStorage: 'XStorage_8e460a32', sEntName: str, aMediaArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]', aObjectArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        lets the object store itself to an entry in destination storage, the own persistence entry is not changed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XEmbedPersist']

