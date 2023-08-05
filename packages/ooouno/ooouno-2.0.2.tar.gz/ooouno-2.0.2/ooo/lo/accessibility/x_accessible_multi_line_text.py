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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from .x_accessible_text import XAccessibleText as XAccessibleText_5b77105b
if typing.TYPE_CHECKING:
    from .text_segment import TextSegment as TextSegment_1e5b0ee8

class XAccessibleMultiLineText(XAccessibleText_5b77105b):
    """
    Implement this interface to give provide a mapping between text index and line numbers.
    
    This interface is typically used in conjunction with the XAccessibleText interface and extents it with a notion of line numbers
    
    **since**
    
        OOo 3.0 not yet published

    See Also:
        `API XAccessibleMultiLineText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleMultiLineText.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleMultiLineText'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleMultiLineText'

    @abstractmethod
    def getLineNumberAtIndex(self, nIndex: int) -> int:
        """
        Returns the line number at the specified index.
        
        For a text object that is spread over multiple lines, this method provides a mapping from a text index to the corresponding line number.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getNumberOfLineWithCaret(self) -> int:
        """
        Returns the number of the line in which the caret is located.
        
        The line number returned will most of the time be identical to calling XAccessibleMultiLineText.getLineNumberAtIndex() with the index returned by XAccessibleText.getCaretPosition() beside the following special case:
        
        Some text implementations place the caret at the end of the current line when the End key gets pressed. Since the index of this position is identical to the one of the first character of the following line, XAccessibleMultiLineText.getLineNumberAtIndex() will return the line following the current one in this case.
        """
        ...
    @abstractmethod
    def getTextAtLineNumber(self, nLineNo: int) -> 'TextSegment_1e5b0ee8':
        """
        Returns the text of the specified line.
        
        Returns the substring of text that makes up the specified line number.
        
        The number of lines can be obtained by calling XAccessibleMultiLineText.getLineNumberAtIndex() with the index of the last character. In a loop, the last line has been reached when TextSegment.SegmentEnd of the returned value is equal to the index of the last character of the text.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getTextAtLineWithCaret(self) -> 'TextSegment_1e5b0ee8':
        """
        Returns the text of the line in which the caret is located.
        
        The substring returned will most of the time be identical to calling XAccessibleText.getTextAtIndex() with the index returned by XAccessibleText.getCaretPosition() and type AccessibleTextType.LINE beside the following special case:
        
        Some text implementations place the caret at the end of the current line when the End key gets pressed. Since the index of this position is identical to the one of the first character of the following line, XAccessibleMultiLineText.getLineNumberAtIndex() will return the line following the current one in this case.
        """
        ...

__all__ = ['XAccessibleMultiLineText']

