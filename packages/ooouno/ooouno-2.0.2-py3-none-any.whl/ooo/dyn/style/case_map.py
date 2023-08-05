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
# Namespace: com.sun.star.style
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CaseMap(metaclass=UnoConstMeta, type_name="com.sun.star.style.CaseMap", name_space="com.sun.star.style"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.style.CaseMap``"""
        pass

    class CaseMapEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.style.CaseMap", name_space="com.sun.star.style"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.style.CaseMap`` as Enum values"""
        pass

else:
    from com.sun.star.style import CaseMap as CaseMap

    class CaseMapEnum(IntEnum):
        """
        Enum of Const Class CaseMap

        These constants are used to specify a case-related mapping for formatting and displaying characters.
        """
        NONE = CaseMap.NONE
        """
        The case of the characters is unchanged.
        """
        UPPERCASE = CaseMap.UPPERCASE
        """
        All characters are put in upper case.
        """
        LOWERCASE = CaseMap.LOWERCASE
        """
        All characters are put in lower case.
        """
        TITLE = CaseMap.TITLE
        """
        The first character of each word is put in upper case.
        """
        SMALLCAPS = CaseMap.SMALLCAPS
        """
        All characters are put in upper case, but with a smaller font height.
        """

__all__ = ['CaseMap', 'CaseMapEnum']
