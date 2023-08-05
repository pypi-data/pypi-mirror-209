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
from ..container.x_element_access import XElementAccess as XElementAccess_cd60e3f
if typing.TYPE_CHECKING:
    from .element_change import ElementChange as ElementChange_bc680bd6

class XChangesSet(XElementAccess_cd60e3f):
    """
    this interface enables inspecting a set of changes forming one batch transaction.
    
    An object implementing this interface should implement more container interfaces to access individual changes as well.

    See Also:
        `API XChangesSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XChangesSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XChangesSet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XChangesSet'

    @abstractmethod
    def getAllChanges(self) -> 'typing.Tuple[ElementChange_bc680bd6, ...]':
        """
        queries for all contained changes at once.
        """
        ...

__all__ = ['XChangesSet']

