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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XFrameLoaderQuery(XInterface_8f010a43):
    """
    use service FrameLoaderFactory instead of this
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XFrameLoaderQuery <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrameLoaderQuery.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XFrameLoaderQuery'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XFrameLoaderQuery'

    @abstractmethod
    def getAvailableFilterNames(self) -> 'typing.Tuple[str, ...]':
        """
        use member com.sun.star.container.XNameAccess.getElementNames() provided by service FrameLoaderFactory instead of this
        """
        ...
    @abstractmethod
    def getLoaderProperties(self, sFilterName: str) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        use member com.sun.star.container.XNameAccess.getByName() provided by service FrameLoaderFactory instead of this
        """
        ...
    @abstractmethod
    def searchFilter(self, sURL: str, seqArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> str:
        """
        use member com.sun.star.container.XContainerQuery provided by service FrameLoaderFactory instead of this
        """
        ...

__all__ = ['XFrameLoaderQuery']

