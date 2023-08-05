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
# Namespace: com.sun.star.mozilla
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .mozilla_product_type import MozillaProductType as MozillaProductType_2e210f5b

class XProfileManager(XInterface_8f010a43):
    """
    is the interface to boot up and switch Mozilla/Thunderbird profiles

    See Also:
        `API XProfileManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mozilla_1_1XProfileManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.XProfileManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.mozilla.XProfileManager'

    @abstractmethod
    def bootupProfile(self, product: 'MozillaProductType_2e210f5b', profileName: str) -> int:
        """
        attempts to init XPCOM runtime using given profile.
        """
        ...
    @abstractmethod
    def getCurrentProduct(self) -> 'MozillaProductType_2e210f5b':
        """
        attempts to get the current product.
        """
        ...
    @abstractmethod
    def getCurrentProfile(self) -> str:
        """
        attempts to get the current profile name.
        """
        ...
    @abstractmethod
    def isCurrentProfileLocked(self) -> bool:
        """
        attempts to check whether the current profile locked or not
        """
        ...
    @abstractmethod
    def setCurrentProfile(self, product: 'MozillaProductType_2e210f5b', profileName: str) -> str:
        """
        attempts to set the current used profile name for the given product.
        """
        ...
    @abstractmethod
    def shutdownProfile(self) -> int:
        """
        attempts to shutdown the current profile.
        """
        ...

__all__ = ['XProfileManager']

