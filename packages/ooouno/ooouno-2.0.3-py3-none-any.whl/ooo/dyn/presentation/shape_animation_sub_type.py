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
# Namespace: com.sun.star.presentation
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ShapeAnimationSubType(metaclass=UnoConstMeta, type_name="com.sun.star.presentation.ShapeAnimationSubType", name_space="com.sun.star.presentation"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.presentation.ShapeAnimationSubType``"""
        pass

    class ShapeAnimationSubTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.presentation.ShapeAnimationSubType", name_space="com.sun.star.presentation"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.presentation.ShapeAnimationSubType`` as Enum values"""
        pass

else:
    from com.sun.star.presentation import ShapeAnimationSubType as ShapeAnimationSubType

    class ShapeAnimationSubTypeEnum(IntEnum):
        """
        Enum of Const Class ShapeAnimationSubType

        Defines the whole shape or a subitem as a target for an effect.
        """
        AS_WHOLE = ShapeAnimationSubType.AS_WHOLE
        """
        the whole shape is a target
        """
        ONLY_BACKGROUND = ShapeAnimationSubType.ONLY_BACKGROUND
        """
        only the background is a target.
        
        The Background of a shape is the whole shape except all visible elements that are part of the shapes text.
        """
        ONLY_TEXT = ShapeAnimationSubType.ONLY_TEXT
        """
        only the text is a target.
        
        This includes all glyphs, font decorations and bullets.
        """

__all__ = ['ShapeAnimationSubType', 'ShapeAnimationSubTypeEnum']
