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
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.TextureKind2 import COLOR as TEXTURE_KIND_2_COLOR
    from com.sun.star.drawing.TextureKind2 import INTENSITY as TEXTURE_KIND_2_INTENSITY
    from com.sun.star.drawing.TextureKind2 import LUMINANCE as TEXTURE_KIND_2_LUMINANCE

    class TextureKind2(uno.Enum):
        """
        Enum Class


        See Also:
            `API TextureKind2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adaf903dffc9b5178ac0a76faef6142f2>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.TextureKind2', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.TextureKind2'
        __ooo_type_name__: str = 'enum'

        COLOR: TextureKind2 = TEXTURE_KIND_2_COLOR
        """
        With this mode the lighting is ignored and only the texture color information is used.
        
        With this mode, the lighting is ignored and only the texture color information is used.
        """
        INTENSITY: TextureKind2 = TEXTURE_KIND_2_INTENSITY
        """
        With TextureKind INTENSITY, each texture pixel is used as an intensity value.
        """
        LUMINANCE: TextureKind2 = TEXTURE_KIND_2_LUMINANCE
        """
        With TextureKind LUMINANCE, the texture and the lighting information is mixed to produce the image, so a lit, textured object is achieved.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TextureKind2(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.TextureKind2", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.TextureKind2`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TextureKind2']
