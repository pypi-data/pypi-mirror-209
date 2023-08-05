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
# Namespace: com.sun.star.sdbcx
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XCreateCatalog(XInterface_8f010a43):
    """
    may be implemented to hide the complexity of creating a database catalog.

    See Also:
        `API XCreateCatalog <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XCreateCatalog.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XCreateCatalog'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XCreateCatalog'

    @abstractmethod
    def createCatalog(self, info: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        creates the catalog by using a sequence of property values.
        
        The kind of properties depends on the provider.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...

__all__ = ['XCreateCatalog']

