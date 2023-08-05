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
# Namespace: com.sun.star.awt
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ScrollBarOrientation(metaclass=UnoConstMeta, type_name="com.sun.star.awt.ScrollBarOrientation", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.ScrollBarOrientation``"""
        pass

    class ScrollBarOrientationEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.ScrollBarOrientation", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.ScrollBarOrientation`` as Enum values"""
        pass

else:
    from com.sun.star.awt import ScrollBarOrientation as ScrollBarOrientation

    class ScrollBarOrientationEnum(IntEnum):
        """
        Enum of Const Class ScrollBarOrientation

        These constants are used to specify the orientation of a scroll bar.
        """
        HORIZONTAL = ScrollBarOrientation.HORIZONTAL
        """
        specifies a horizontal scroll bar.
        """
        VERTICAL = ScrollBarOrientation.VERTICAL
        """
        specifies a vertical scroll bar.
        """

__all__ = ['ScrollBarOrientation', 'ScrollBarOrientationEnum']
