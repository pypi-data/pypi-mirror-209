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
# Namespace: com.sun.star.text
from abc import abstractmethod
from .x_text_content import XTextContent as XTextContent_b16e0ba5

class XDocumentIndex(XTextContent_b16e0ba5):
    """
    This is the main interface for a document index.
    
    Use com.sun.star.util.XRefreshable and com.sun.star.lang.XServiceInfo instead, if available.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDocumentIndex <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDocumentIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XDocumentIndex'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XDocumentIndex'

    @abstractmethod
    def getServiceName(self) -> str:
        """
        returns the service name that was used to create this document index type.
        """
        ...
    @abstractmethod
    def update(self) -> None:
        """
        initiates an update to the document index.
        """
        ...

__all__ = ['XDocumentIndex']

