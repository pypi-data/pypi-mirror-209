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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_text import XText as XText_690408ca

class XTextRange(XInterface_8f010a43):
    """
    describes the object's position in a text.
    
    It represents a text range. The beginning and end of the range may be identical.

    See Also:
        `API XTextRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XTextRange'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XTextRange'

    @abstractmethod
    def getEnd(self) -> 'XTextRange':
        """
        """
        ...
    @abstractmethod
    def getStart(self) -> 'XTextRange':
        """
        """
        ...
    @abstractmethod
    def getString(self) -> str:
        """
        """
        ...
    @abstractmethod
    def getText(self) -> 'XText_690408ca':
        """
        """
        ...
    @abstractmethod
    def setString(self, aString: str) -> None:
        """
        the whole string of characters of this piece of text is replaced.
        
        All styles are removed when applying this method.
        """
        ...

__all__ = ['XTextRange']

