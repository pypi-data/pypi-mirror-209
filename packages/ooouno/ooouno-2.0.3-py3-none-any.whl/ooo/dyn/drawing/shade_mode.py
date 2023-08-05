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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.ShadeMode import DRAFT as SHADE_MODE_DRAFT
    from com.sun.star.drawing.ShadeMode import FLAT as SHADE_MODE_FLAT
    from com.sun.star.drawing.ShadeMode import PHONG as SHADE_MODE_PHONG
    from com.sun.star.drawing.ShadeMode import SMOOTH as SHADE_MODE_SMOOTH

    class ShadeMode(uno.Enum):
        """
        Enum Class


        See Also:
            `API ShadeMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#af49ab4b65513d2c0077f76b2227326e9>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.ShadeMode', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.ShadeMode'
        __ooo_type_name__: str = 'enum'

        DRAFT = cast("ShadeMode", SHADE_MODE_DRAFT)
        """
        DRAFT is a special mode which uses a BSP tree and triangle subdivision for displaying.
        """
        FLAT = cast("ShadeMode", SHADE_MODE_FLAT)
        """
        forces one normal per flat part.
        
        With FLAT shading, the faces of the object are rendered in a solid color.
        """
        PHONG = cast("ShadeMode", SHADE_MODE_PHONG)
        """
        With PHONG shading, the normal itself is interpolated to get more realistic colors and light reflections.
        """
        SMOOTH = cast("ShadeMode", SHADE_MODE_SMOOTH)
        """
        the point is smooth, the first derivation from the curve discussion view.
        
        With SMOOTH shading, the colors of the lit vertices is interpolated.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ShadeMode(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.ShadeMode", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.ShadeMode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ShadeMode']
