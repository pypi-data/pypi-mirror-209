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
# Namespace: com.sun.star.style
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.style.GraphicLocation import AREA as GRAPHIC_LOCATION_AREA
    from com.sun.star.style.GraphicLocation import LEFT_BOTTOM as GRAPHIC_LOCATION_LEFT_BOTTOM
    from com.sun.star.style.GraphicLocation import LEFT_MIDDLE as GRAPHIC_LOCATION_LEFT_MIDDLE
    from com.sun.star.style.GraphicLocation import LEFT_TOP as GRAPHIC_LOCATION_LEFT_TOP
    from com.sun.star.style.GraphicLocation import MIDDLE_BOTTOM as GRAPHIC_LOCATION_MIDDLE_BOTTOM
    from com.sun.star.style.GraphicLocation import MIDDLE_MIDDLE as GRAPHIC_LOCATION_MIDDLE_MIDDLE
    from com.sun.star.style.GraphicLocation import MIDDLE_TOP as GRAPHIC_LOCATION_MIDDLE_TOP
    from com.sun.star.style.GraphicLocation import NONE as GRAPHIC_LOCATION_NONE
    from com.sun.star.style.GraphicLocation import RIGHT_BOTTOM as GRAPHIC_LOCATION_RIGHT_BOTTOM
    from com.sun.star.style.GraphicLocation import RIGHT_MIDDLE as GRAPHIC_LOCATION_RIGHT_MIDDLE
    from com.sun.star.style.GraphicLocation import RIGHT_TOP as GRAPHIC_LOCATION_RIGHT_TOP
    from com.sun.star.style.GraphicLocation import TILED as GRAPHIC_LOCATION_TILED

    class GraphicLocation(uno.Enum):
        """
        Enum Class


        See Also:
            `API GraphicLocation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#ae71ca73feb713866e85597329dfaec2e>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.style.GraphicLocation', value)

        __ooo_ns__: str = 'com.sun.star.style'
        __ooo_full_ns__: str = 'com.sun.star.style.GraphicLocation'
        __ooo_type_name__: str = 'enum'

        AREA = cast("GraphicLocation", GRAPHIC_LOCATION_AREA)
        """
        The graphic is scaled to fill the whole surrounding area.
        """
        LEFT_BOTTOM = cast("GraphicLocation", GRAPHIC_LOCATION_LEFT_BOTTOM)
        """
        The graphic is located in the bottom left corner.
        """
        LEFT_MIDDLE = cast("GraphicLocation", GRAPHIC_LOCATION_LEFT_MIDDLE)
        """
        The graphic is located in the middle of the left edge.
        """
        LEFT_TOP = cast("GraphicLocation", GRAPHIC_LOCATION_LEFT_TOP)
        """
        The graphic is located in the top left corner.
        """
        MIDDLE_BOTTOM = cast("GraphicLocation", GRAPHIC_LOCATION_MIDDLE_BOTTOM)
        """
        The graphic is located in the middle of the bottom edge.
        """
        MIDDLE_MIDDLE = cast("GraphicLocation", GRAPHIC_LOCATION_MIDDLE_MIDDLE)
        """
        The graphic is located at the center of the surrounding object.
        """
        MIDDLE_TOP = cast("GraphicLocation", GRAPHIC_LOCATION_MIDDLE_TOP)
        """
        The graphic is located in the middle of the top edge.
        """
        NONE = cast("GraphicLocation", GRAPHIC_LOCATION_NONE)
        """
        No column or page break is applied.
        
        This value specifies that a location is not yet assigned.
        """
        RIGHT_BOTTOM = cast("GraphicLocation", GRAPHIC_LOCATION_RIGHT_BOTTOM)
        """
        The graphic is located in the bottom right corner.
        """
        RIGHT_MIDDLE = cast("GraphicLocation", GRAPHIC_LOCATION_RIGHT_MIDDLE)
        """
        The graphic is located in the middle of the right edge.
        """
        RIGHT_TOP = cast("GraphicLocation", GRAPHIC_LOCATION_RIGHT_TOP)
        """
        The graphic is located in the top right corner.
        """
        TILED = cast("GraphicLocation", GRAPHIC_LOCATION_TILED)
        """
        The graphic is repeatedly spread over the surrounding object like tiles.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class GraphicLocation(metaclass=UnoEnumMeta, type_name="com.sun.star.style.GraphicLocation", name_space="com.sun.star.style"):
        """Dynamically created class that represents ``com.sun.star.style.GraphicLocation`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['GraphicLocation']
