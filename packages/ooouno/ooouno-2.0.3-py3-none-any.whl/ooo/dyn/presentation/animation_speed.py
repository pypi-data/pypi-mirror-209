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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.presentation.AnimationSpeed import FAST as ANIMATION_SPEED_FAST
    from com.sun.star.presentation.AnimationSpeed import MEDIUM as ANIMATION_SPEED_MEDIUM
    from com.sun.star.presentation.AnimationSpeed import SLOW as ANIMATION_SPEED_SLOW

    class AnimationSpeed(uno.Enum):
        """
        Enum Class


        See Also:
            `API AnimationSpeed <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a07b64dc4a366b20ad5052f974ffdbf62>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.presentation.AnimationSpeed', value)

        __ooo_ns__: str = 'com.sun.star.presentation'
        __ooo_full_ns__: str = 'com.sun.star.presentation.AnimationSpeed'
        __ooo_type_name__: str = 'enum'

        FAST = cast("AnimationSpeed", ANIMATION_SPEED_FAST)
        """
        set the speed from the animation/fade to fast.
        """
        MEDIUM = cast("AnimationSpeed", ANIMATION_SPEED_MEDIUM)
        """
        set the speed from the animation/fade to medium.
        """
        SLOW = cast("AnimationSpeed", ANIMATION_SPEED_SLOW)
        """
        set the speed from the animation/fade to slow.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class AnimationSpeed(metaclass=UnoEnumMeta, type_name="com.sun.star.presentation.AnimationSpeed", name_space="com.sun.star.presentation"):
        """Dynamically created class that represents ``com.sun.star.presentation.AnimationSpeed`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['AnimationSpeed']
