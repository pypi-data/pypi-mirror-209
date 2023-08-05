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
from .x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource_8cdf11a3
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class XEncryptionProtectedSource2(XEncryptionProtectedSource_8cdf11a3):
    """
    This interface allows to set a password for an object.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XEncryptionProtectedSource2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEncryptionProtectedSource2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XEncryptionProtectedSource2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XEncryptionProtectedSource2'

    @abstractmethod
    def hasEncryptionData(self) -> bool:
        """
        determine if an encryption data is set for this object.
        """
        ...
    @abstractmethod
    def setEncryptionData(self, aEncryptionData: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> None:
        """
        sets an encryption data for the object.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XEncryptionProtectedSource2']

