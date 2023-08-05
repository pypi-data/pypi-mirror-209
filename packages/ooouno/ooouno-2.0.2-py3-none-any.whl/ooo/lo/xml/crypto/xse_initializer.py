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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xxml_security_context import XXMLSecurityContext as XXMLSecurityContext_681010ae

class XSEInitializer(XInterface_8f010a43):
    """
    Interface to manipulate Security Environment.

    See Also:
        `API XSEInitializer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XSEInitializer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XSEInitializer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XSEInitializer'

    @abstractmethod
    def createSecurityContext(self, aString: str) -> 'XXMLSecurityContext_681010ae':
        """
        Creates a security context.
        """
        ...
    @abstractmethod
    def freeSecurityContext(self, securityContext: 'XXMLSecurityContext_681010ae') -> None:
        """
        Frees a security context.
        """
        ...

__all__ = ['XSEInitializer']

