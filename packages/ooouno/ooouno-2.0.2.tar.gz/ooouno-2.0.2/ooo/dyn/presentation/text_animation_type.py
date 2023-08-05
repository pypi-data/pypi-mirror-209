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

    class TextAnimationType(metaclass=UnoConstMeta, type_name="com.sun.star.presentation.TextAnimationType", name_space="com.sun.star.presentation"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.presentation.TextAnimationType``"""
        pass

    class TextAnimationTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.presentation.TextAnimationType", name_space="com.sun.star.presentation"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.presentation.TextAnimationType`` as Enum values"""
        pass

else:
    from com.sun.star.presentation import TextAnimationType as TextAnimationType

    class TextAnimationTypeEnum(IntEnum):
        """
        Enum of Const Class TextAnimationType

        Defines how a target com.sun.star.text.XTextRange is animated inside an com.sun.star.animations.XIterateContainer.
        
        This is stored inside the attribute com.sun.star.animations.XIterateContainer.IterateType.
        """
        BY_PARAGRAPH = TextAnimationType.BY_PARAGRAPH
        """
        the text is animated paragraph by paragraph
        """
        BY_WORD = TextAnimationType.BY_WORD
        """
        the text is animated word by word
        """
        BY_LETTER = TextAnimationType.BY_LETTER
        """
        the text is animated letter by letter.
        """

__all__ = ['TextAnimationType', 'TextAnimationTypeEnum']
