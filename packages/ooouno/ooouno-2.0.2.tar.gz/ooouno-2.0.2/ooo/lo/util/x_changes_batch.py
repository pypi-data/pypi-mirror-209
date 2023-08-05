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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .changes_set import ChangesSet as ChangesSet_99de0aab

class XChangesBatch(XInterface_8f010a43):
    """
    this interface enables applying a set of changes in one batch transaction.
    
    An object implementing this interface allows other interfaces to change its state locally. It will keep a list of pending changes until such changes are committed or canceled.
    
    Only when they are explicitly committed will these changes take effect persistently or globally.

    See Also:
        `API XChangesBatch <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XChangesBatch.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XChangesBatch'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XChangesBatch'

    @abstractmethod
    def commitChanges(self) -> None:
        """
        commits any pending changes.
        
        The exact action depends on the concrete service.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def getPendingChanges(self) -> 'ChangesSet_99de0aab':
        """
        queries for any pending changes that can be committed.
        """
        ...
    @abstractmethod
    def hasPendingChanges(self) -> bool:
        """
        checks whether this object has any pending changes that can be committed.
        """
        ...

__all__ = ['XChangesBatch']

