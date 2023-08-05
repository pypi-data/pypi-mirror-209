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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class reservedWords(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.reservedWords", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.reservedWords``"""
        pass

    class reservedWordsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.reservedWords", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.reservedWords`` as Enum values"""
        pass

else:
    from com.sun.star.i18n import reservedWords as reservedWords

    class reservedWordsEnum(IntEnum):
        """
        Enum of Const Class reservedWords

        Offsets into the sequence of strings returned by XLocaleData.getReservedWord().
        """
        TRUE_WORD = reservedWords.TRUE_WORD
        """
        \"true\"
        """
        FALSE_WORD = reservedWords.FALSE_WORD
        """
        \"false\"
        """
        QUARTER1_WORD = reservedWords.QUARTER1_WORD
        """
        \"1st quarter\"
        """
        QUARTER2_WORD = reservedWords.QUARTER2_WORD
        """
        \"2nd quarter\"
        """
        QUARTER3_WORD = reservedWords.QUARTER3_WORD
        """
        \"3rd quarter\"
        """
        QUARTER4_WORD = reservedWords.QUARTER4_WORD
        """
        \"4th quarter\"
        """
        ABOVE_WORD = reservedWords.ABOVE_WORD
        """
        \"above\"
        """
        BELOW_WORD = reservedWords.BELOW_WORD
        """
        \"below\"
        """
        QUARTER1_ABBREVIATION = reservedWords.QUARTER1_ABBREVIATION
        """
        \"Q1\"
        """
        QUARTER2_ABBREVIATION = reservedWords.QUARTER2_ABBREVIATION
        """
        \"Q2\"
        """
        QUARTER3_ABBREVIATION = reservedWords.QUARTER3_ABBREVIATION
        """
        \"Q3\"
        """
        QUARTER4_ABBREVIATION = reservedWords.QUARTER4_ABBREVIATION
        """
        \"Q4\"
        """
        COUNT = reservedWords.COUNT
        """
        Yes, this must be the count of known reserved words and one more than the maximum number used above! Count of known reserved words.
        """

__all__ = ['reservedWords', 'reservedWordsEnum']
