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
# Namespace: com.sun.star.sheet
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class IconSetFormatEntry(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.IconSetFormatEntry", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.IconSetFormatEntry``"""
        pass

    class IconSetFormatEntryEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.IconSetFormatEntry", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.IconSetFormatEntry`` as Enum values"""
        pass

else:
    from com.sun.star.sheet import IconSetFormatEntry as IconSetFormatEntry

    class IconSetFormatEntryEnum(IntEnum):
        """
        Enum of Const Class IconSetFormatEntry

        """
        ICONSET_MIN = IconSetFormatEntry.ICONSET_MIN
        """
        Can not be set! Will always be the type of the first entry.
        """
        ICONSET_PERCENTILE = IconSetFormatEntry.ICONSET_PERCENTILE
        ICONSET_VALUE = IconSetFormatEntry.ICONSET_VALUE
        ICONSET_PERCENT = IconSetFormatEntry.ICONSET_PERCENT
        ICONSET_FORMULA = IconSetFormatEntry.ICONSET_FORMULA

__all__ = ['IconSetFormatEntry', 'IconSetFormatEntryEnum']
