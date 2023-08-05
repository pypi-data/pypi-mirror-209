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
# Namespace: com.sun.star.text
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class VertOrientation(metaclass=UnoConstMeta, type_name="com.sun.star.text.VertOrientation", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.VertOrientation``"""
        pass

    class VertOrientationEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.VertOrientation", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.VertOrientation`` as Enum values"""
        pass

else:
    from com.sun.star.text import VertOrientation as VertOrientation

    class VertOrientationEnum(IntEnum):
        """
        Enum of Const Class VertOrientation

        These enumeration values are used to specify the vertical orientation.
        """
        NONE = VertOrientation.NONE
        """
        no hard alignment
        """
        TOP = VertOrientation.TOP
        """
        aligned at the top
        """
        CENTER = VertOrientation.CENTER
        """
        aligned at the center
        """
        BOTTOM = VertOrientation.BOTTOM
        """
        aligned at the bottom
        """
        CHAR_TOP = VertOrientation.CHAR_TOP
        """
        aligned at the top of a character (anchored to character)
        """
        CHAR_CENTER = VertOrientation.CHAR_CENTER
        """
        aligned at the center of a character (anchored to character )
        """
        CHAR_BOTTOM = VertOrientation.CHAR_BOTTOM
        """
        aligned at the bottom of a character (anchored to character )
        """
        LINE_TOP = VertOrientation.LINE_TOP
        """
        aligned at the top of the line (anchored to character )
        """
        LINE_CENTER = VertOrientation.LINE_CENTER
        """
        aligned at the center of the line (anchored to character )
        """
        LINE_BOTTOM = VertOrientation.LINE_BOTTOM
        """
        aligned at the bottom of the line (anchored to character )
        """

__all__ = ['VertOrientation', 'VertOrientationEnum']
