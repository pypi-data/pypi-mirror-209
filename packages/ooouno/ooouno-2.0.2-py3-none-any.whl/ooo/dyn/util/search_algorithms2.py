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
# Namespace: com.sun.star.util
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class SearchAlgorithms2(metaclass=UnoConstMeta, type_name="com.sun.star.util.SearchAlgorithms2", name_space="com.sun.star.util"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.util.SearchAlgorithms2``"""
        pass

    class SearchAlgorithms2Enum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.util.SearchAlgorithms2", name_space="com.sun.star.util"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.util.SearchAlgorithms2`` as Enum values"""
        pass

else:
    from com.sun.star.util import SearchAlgorithms2 as SearchAlgorithms2

    class SearchAlgorithms2Enum(IntEnum):
        """
        Enum of Const Class SearchAlgorithms2

        Constants that define the search algorithm to be used with com.sun.star.util.SearchOptions2.SearchAlgorithms2.
        
        **since**
        
            LibreOffice 5.2
        """
        ABSOLUTE = SearchAlgorithms2.ABSOLUTE
        """
        Literal.
        """
        REGEXP = SearchAlgorithms2.REGEXP
        """
        Regular expression.
        """
        APPROXIMATE = SearchAlgorithms2.APPROXIMATE
        """
        Weighted Levenshtein Distance.
        """
        WILDCARD = SearchAlgorithms2.WILDCARD
        """
        Wildcards '*' and '?' An escape character is defined by setting com.sun.star.util.SearchOptions2.WildcardEscapeCharacter.
        """

__all__ = ['SearchAlgorithms2', 'SearchAlgorithms2Enum']
