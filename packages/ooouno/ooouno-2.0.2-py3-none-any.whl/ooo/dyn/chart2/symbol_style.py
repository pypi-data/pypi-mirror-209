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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.chart2.SymbolStyle import AUTO as SYMBOL_STYLE_AUTO
    from com.sun.star.chart2.SymbolStyle import GRAPHIC as SYMBOL_STYLE_GRAPHIC
    from com.sun.star.chart2.SymbolStyle import NONE as SYMBOL_STYLE_NONE
    from com.sun.star.chart2.SymbolStyle import POLYGON as SYMBOL_STYLE_POLYGON
    from com.sun.star.chart2.SymbolStyle import STANDARD as SYMBOL_STYLE_STANDARD

    class SymbolStyle(uno.Enum):
        """
        Enum Class


        See Also:
            `API SymbolStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a8068445d248b830d1708dcb2a2afb2c6>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.chart2.SymbolStyle', value)

        __ooo_ns__: str = 'com.sun.star.chart2'
        __ooo_full_ns__: str = 'com.sun.star.chart2.SymbolStyle'
        __ooo_type_name__: str = 'enum'

        AUTO: SymbolStyle = SYMBOL_STYLE_AUTO
        """
        The symbol is taken automatically.
        """
        GRAPHIC: SymbolStyle = SYMBOL_STYLE_GRAPHIC
        """
        uses the graphic given in Symbol.Graphic as symbol.
        """
        NONE: SymbolStyle = SYMBOL_STYLE_NONE
        """
        Default, no pies are exploded.
        
        no transparency attribute is evaluated
        
        The symbol is invisible.
        """
        POLYGON: SymbolStyle = SYMBOL_STYLE_POLYGON
        """
        uses the symbol given in the com.sun.star.drawing.PolyPolygonBezierCoords given in Symbol.PolygonCoords.
        """
        STANDARD: SymbolStyle = SYMBOL_STYLE_STANDARD
        """
        uses one of the standard symbols.
        
        Which standard symbol is given in Symbol.StandardSymbol.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class SymbolStyle(metaclass=UnoEnumMeta, type_name="com.sun.star.chart2.SymbolStyle", name_space="com.sun.star.chart2"):
        """Dynamically created class that represents ``com.sun.star.chart2.SymbolStyle`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['SymbolStyle']
