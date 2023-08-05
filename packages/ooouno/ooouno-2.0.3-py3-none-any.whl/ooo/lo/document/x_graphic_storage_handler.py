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
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35

class XGraphicStorageHandler(XInterface_8f010a43):
    """
    interface for loading, saving and serializing of XGraphic objects to a document storage
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API XGraphicStorageHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XGraphicStorageHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XGraphicStorageHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XGraphicStorageHandler'

    @abstractmethod
    def createInputStream(self, xGraphic: 'XGraphic_a4da0afc') -> 'XInputStream_98d40ab4':
        """
        create an input stream from the input graphic
        """
        ...
    @abstractmethod
    def loadGraphic(self, aURL: str) -> 'XGraphic_a4da0afc':
        """
        load a graphic defined by the URL from the storage
        """
        ...
    @abstractmethod
    def loadGraphicFromOutputStream(self, xOutputStream: 'XOutputStream_a4e00b35') -> 'XGraphic_a4da0afc':
        """
        load a graphic from the output stream
        """
        ...
    @abstractmethod
    def saveGraphic(self, xGraphic: 'XGraphic_a4da0afc') -> str:
        """
        save the graphic to the storage and return the URL reference to its location inside the storage
        """
        ...
    @abstractmethod
    def saveGraphicByName(self, xGraphic: 'XGraphic_a4da0afc', savedMimeType: str, aRequestedName: str) -> str:
        """
        save the graphic to the storage with a requested name and return the URL reference to its location inside the storage and the mime type of the format that the graphic was saved to as an output parameter

        * ``savedMimeType`` is an out direction argument.
        """
        ...

__all__ = ['XGraphicStorageHandler']

