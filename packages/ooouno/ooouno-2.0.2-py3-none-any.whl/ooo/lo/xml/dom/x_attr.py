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
from .x_node import XNode as XNode_83fb09a5
if typing.TYPE_CHECKING:
    from .x_element import XElement as XElement_a33d0ae9

class XAttr(XNode_83fb09a5):
    """

    See Also:
        `API XAttr <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XAttr.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XAttr'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XAttr'

    @abstractmethod
    def getName(self) -> str:
        """
        Returns the name of this attribute.
        """
        ...
    @abstractmethod
    def getOwnerElement(self) -> 'XElement_a33d0ae9':
        """
        The Element node this attribute is attached to or null if this attribute is not in use.
        """
        ...
    @abstractmethod
    def getSpecified(self) -> bool:
        """
        If this attribute was explicitly given a value in the original document, this is true; otherwise, it is false.
        """
        ...
    @abstractmethod
    def getValue(self) -> str:
        """
        On retrieval, the value of the attribute is returned as a string.
        """
        ...
    @abstractmethod
    def setValue(self, value: str) -> None:
        """
        Sets the value of the attribute from a string.
        
        Throws: DOMException - NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...

__all__ = ['XAttr']

