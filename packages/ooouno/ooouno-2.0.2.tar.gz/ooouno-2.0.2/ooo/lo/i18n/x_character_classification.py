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
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .parse_result import ParseResult as ParseResult_9ea00ac2
    from ..lang.locale import Locale as Locale_70d308fa

class XCharacterClassification(XInterface_8f010a43):
    """
    Character classification (upper, lower, digit, letter, number, ...) and generic Unicode enabled parser.

    See Also:
        `API XCharacterClassification <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XCharacterClassification.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XCharacterClassification'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XCharacterClassification'

    @abstractmethod
    def getCharacterDirection(self, aText: str, nPos: int) -> int:
        """
        Get DirectionProperty of character at position nPos.
        """
        ...
    @abstractmethod
    def getCharacterType(self, aText: str, nPos: int, aLocale: 'Locale_70d308fa') -> int:
        """
        Get KCharacterType of character at position nPos.
        """
        ...
    @abstractmethod
    def getScript(self, aText: str, nPos: int) -> int:
        """
        Get UnicodeScript of character at position nPos.
        """
        ...
    @abstractmethod
    def getStringType(self, aText: str, nPos: int, nCount: int, aLocale: 'Locale_70d308fa') -> int:
        """
        Get accumulated KCharacterTypes of string starting at position nPos of length nCount code points.
        """
        ...
    @abstractmethod
    def getType(self, aText: str, nPos: int) -> int:
        """
        Get UnicodeType of character at position nPos.
        """
        ...
    @abstractmethod
    def parseAnyToken(self, aText: str, nPos: int, aLocale: 'Locale_70d308fa', nStartCharFlags: int, aUserDefinedCharactersStart: str, nContCharFlags: int, aUserDefinedCharactersCont: str) -> 'ParseResult_9ea00ac2':
        """
        Parse a string for a token starting at position nPos.
        
        A name or identifier must match the KParseTokens criteria passed in nStartCharFlags and nContCharFlags and may additionally contain characters of aUserDefinedCharactersStart and/or aUserDefinedCharactersCont.
        
        If a token may represent either a numeric value or a name according to the passed Start/Cont-Flags/Chars, both KParseType.ASC_NUM (or KParseType.UNI_NUM) and KParseType.IDENTNAME are set in ParseResult.TokenType.
        """
        ...
    @abstractmethod
    def parsePredefinedToken(self, nTokenType: int, aText: str, nPos: int, aLocale: 'Locale_70d308fa', nStartCharFlags: int, aUserDefinedCharactersStart: str, nContCharFlags: int, aUserDefinedCharactersCont: str) -> 'ParseResult_9ea00ac2':
        """
        Parse a string for a token of type nTokenType starting at position nPos.
        
        Other parameters are the same as in parseAnyToken(). If the actual token does not match the passed nTokenType a ParseResult.TokenType set to 0 (zero) is returned.
        """
        ...
    @abstractmethod
    def toLower(self, aText: str, nPos: int, nCount: int, aLocale: 'Locale_70d308fa') -> str:
        """
        Convert upper case alpha to lower case alpha, starting at position nPos for nCount code points.
        """
        ...
    @abstractmethod
    def toTitle(self, aText: str, nPos: int, nCount: int, aLocale: 'Locale_70d308fa') -> str:
        """
        Convert to title case, starting at position nPos for nCount code points.
        """
        ...
    @abstractmethod
    def toUpper(self, aText: str, nPos: int, nCount: int, aLocale: 'Locale_70d308fa') -> str:
        """
        Convert lower case alpha to upper case alpha, starting at position nPos for nCount code points.
        """
        ...

__all__ = ['XCharacterClassification']

