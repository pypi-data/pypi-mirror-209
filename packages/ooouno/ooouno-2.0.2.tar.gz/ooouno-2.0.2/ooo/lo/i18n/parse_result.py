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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class ParseResult(object):
    """
    Struct Class

    Parser results returned by XCharacterClassification.parseAnyToken() and XCharacterClassification.parsePredefinedToken().

    See Also:
        `API ParseResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1ParseResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.ParseResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.ParseResult'
    """Literal Constant ``com.sun.star.i18n.ParseResult``"""

    def __init__(self, LeadingWhiteSpace: typing.Optional[int] = 0, EndPos: typing.Optional[int] = 0, CharLen: typing.Optional[int] = 0, Value: typing.Optional[float] = 0.0, TokenType: typing.Optional[int] = 0, StartFlags: typing.Optional[int] = 0, ContFlags: typing.Optional[int] = 0, DequotedNameOrString: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            LeadingWhiteSpace (int, optional): LeadingWhiteSpace value.
            EndPos (int, optional): EndPos value.
            CharLen (int, optional): CharLen value.
            Value (float, optional): Value value.
            TokenType (int, optional): TokenType value.
            StartFlags (int, optional): StartFlags value.
            ContFlags (int, optional): ContFlags value.
            DequotedNameOrString (str, optional): DequotedNameOrString value.
        """
        super().__init__()

        if isinstance(LeadingWhiteSpace, ParseResult):
            oth: ParseResult = LeadingWhiteSpace
            self.LeadingWhiteSpace = oth.LeadingWhiteSpace
            self.EndPos = oth.EndPos
            self.CharLen = oth.CharLen
            self.Value = oth.Value
            self.TokenType = oth.TokenType
            self.StartFlags = oth.StartFlags
            self.ContFlags = oth.ContFlags
            self.DequotedNameOrString = oth.DequotedNameOrString
            return

        kargs = {
            "LeadingWhiteSpace": LeadingWhiteSpace,
            "EndPos": EndPos,
            "CharLen": CharLen,
            "Value": Value,
            "TokenType": TokenType,
            "StartFlags": StartFlags,
            "ContFlags": ContFlags,
            "DequotedNameOrString": DequotedNameOrString,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._leading_white_space = kwargs["LeadingWhiteSpace"]
        self._end_pos = kwargs["EndPos"]
        self._char_len = kwargs["CharLen"]
        self._value = kwargs["Value"]
        self._token_type = kwargs["TokenType"]
        self._start_flags = kwargs["StartFlags"]
        self._cont_flags = kwargs["ContFlags"]
        self._dequoted_name_or_string = kwargs["DequotedNameOrString"]


    @property
    def LeadingWhiteSpace(self) -> int:
        """
        Count of ignored leading whitespace, in UTF-16 code units, not Unicode code points.
        """
        return self._leading_white_space

    @LeadingWhiteSpace.setter
    def LeadingWhiteSpace(self, value: int) -> None:
        self._leading_white_space = value

    @property
    def EndPos(self) -> int:
        """
        UTF-16 code unit index of first unprocessed character.
        """
        return self._end_pos

    @EndPos.setter
    def EndPos(self, value: int) -> None:
        self._end_pos = value

    @property
    def CharLen(self) -> int:
        """
        Number of code points (not UTF-16 code units) of the parsed token, not including leading whitespace.
        """
        return self._char_len

    @CharLen.setter
    def CharLen(self, value: int) -> None:
        self._char_len = value

    @property
    def Value(self) -> float:
        """
        Value of token in case of numeric.
        """
        return self._value

    @Value.setter
    def Value(self, value: float) -> None:
        self._value = value

    @property
    def TokenType(self) -> int:
        """
        KParseType token type like KParseType.IDENTNAME.
        """
        return self._token_type

    @TokenType.setter
    def TokenType(self, value: int) -> None:
        self._token_type = value

    @property
    def StartFlags(self) -> int:
        """
        KParseTokens flags of first character of actual token matched.
        
        If TokenType is a KParseType.SINGLE_QUOTE_NAME or a KParseType.DOUBLE_QUOTE_STRING the first character is the first character inside the quotes, not the quote itself.
        """
        return self._start_flags

    @StartFlags.setter
    def StartFlags(self, value: int) -> None:
        self._start_flags = value

    @property
    def ContFlags(self) -> int:
        """
        KParseTokens flags of remaining characters of actual token matched.
        """
        return self._cont_flags

    @ContFlags.setter
    def ContFlags(self, value: int) -> None:
        self._cont_flags = value

    @property
    def DequotedNameOrString(self) -> str:
        """
        If a quoted name or string is encountered the dequoted result goes here.
        """
        return self._dequoted_name_or_string

    @DequotedNameOrString.setter
    def DequotedNameOrString(self, value: str) -> None:
        self._dequoted_name_or_string = value


__all__ = ['ParseResult']
