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
# Namespace: com.sun.star.xml.dom
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from .xdom_implementation import XDOMImplementation as XDOMImplementation_22320ec5
    from .x_document import XDocument as XDocument_aebc0b5e
    from ..sax.x_entity_resolver import XEntityResolver as XEntityResolver_fcf10dfa
    from ..sax.x_error_handler import XErrorHandler as XErrorHandler_e0860cf3

class XDocumentBuilder(XInterface_8f010a43):
    """
    Builds a new dom tree.

    See Also:
        `API XDocumentBuilder <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XDocumentBuilder.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XDocumentBuilder'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XDocumentBuilder'

    @abstractmethod
    def getDOMImplementation(self) -> 'XDOMImplementation_22320ec5':
        """
        Obtain an instance of a DOMImplementation object.
        """
        ...
    @abstractmethod
    def isNamespaceAware(self) -> bool:
        """
        Indicates whether or not this parser is configured to understand namespaces.
        """
        ...
    @abstractmethod
    def isValidating(self) -> bool:
        """
        Indicates whether or not this parser is configured to validate XML documents.
        """
        ...
    @abstractmethod
    def newDocument(self) -> 'XDocument_aebc0b5e':
        """
        Obtain a new instance of a DOM Document object to build a DOM tree with.
        """
        ...
    @abstractmethod
    def parse(self, is_: 'XInputStream_98d40ab4') -> 'XDocument_aebc0b5e':
        """
        Parse the content of the given InputStream as an XML document and return a new DOM Document object.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def parseURI(self, uri: str) -> 'XDocument_aebc0b5e':
        """
        Parse the content of the given URI as an XML document and return a new DOM Document object.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def setEntityResolver(self, er: 'XEntityResolver_fcf10dfa') -> None:
        """
        Specify the EntityResolver to be used to resolve entities present in the XML document to be parsed.
        """
        ...
    @abstractmethod
    def setErrorHandler(self, eh: 'XErrorHandler_e0860cf3') -> None:
        """
        Specify the ErrorHandler to be used to report errors present in the XML document to be parsed.
        """
        ...

__all__ = ['XDocumentBuilder']

