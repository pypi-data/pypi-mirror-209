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

    from com.sun.star.drawing.DashStyle import RECT as DASH_STYLE_RECT
    from com.sun.star.drawing.DashStyle import RECTRELATIVE as DASH_STYLE_RECTRELATIVE
    from com.sun.star.drawing.DashStyle import ROUND as DASH_STYLE_ROUND
    from com.sun.star.drawing.DashStyle import ROUNDRELATIVE as DASH_STYLE_ROUNDRELATIVE

    class DashStyle(uno.Enum):
        """
        Enum Class


        See Also:
            `API DashStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a89f0dc2e221d6f608088093da27764d1>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.DashStyle', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.DashStyle'
        __ooo_type_name__: str = 'enum'

        RECT: DashStyle = DASH_STYLE_RECT
        """
        the dash is a rectangle
        """
        RECTRELATIVE: DashStyle = DASH_STYLE_RECTRELATIVE
        """
        the dash is a rectangle, with the size of the dash given in relation to the length of the line
        """
        ROUND: DashStyle = DASH_STYLE_ROUND
        """
        the dash is a point
        
        the lines join with an arc
        
        the line will get a half circle as additional cap
        """
        ROUNDRELATIVE: DashStyle = DASH_STYLE_ROUNDRELATIVE
        """
        the dash is a point, with the size of the dash given in relation to the length of the line
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DashStyle(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.DashStyle", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.DashStyle`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DashStyle']
