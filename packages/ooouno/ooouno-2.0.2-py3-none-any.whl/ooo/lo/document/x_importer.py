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
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XImporter(XInterface_8f010a43):
    """
    makes it possible to connect a document with an ImportFilter
    
    An ImportFilter must know the target of his filter operation. To set this on a filter is part of this interface. Same mechanism exist for export too.

    See Also:
        `API XImporter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XImporter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XImporter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XImporter'

    @abstractmethod
    def setTargetDocument(self, Document: 'XComponent_98dc0ab5') -> None:
        """
        sets the target document for the importer

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XImporter']

