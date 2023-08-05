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

    from com.sun.star.drawing.TextFitToSizeType import ALLLINES as TEXT_FIT_TO_SIZE_TYPE_ALLLINES
    from com.sun.star.drawing.TextFitToSizeType import AUTOFIT as TEXT_FIT_TO_SIZE_TYPE_AUTOFIT
    from com.sun.star.drawing.TextFitToSizeType import NONE as TEXT_FIT_TO_SIZE_TYPE_NONE
    from com.sun.star.drawing.TextFitToSizeType import PROPORTIONAL as TEXT_FIT_TO_SIZE_TYPE_PROPORTIONAL

    class TextFitToSizeType(uno.Enum):
        """
        Enum Class


        See Also:
            `API TextFitToSizeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a119322ec5cab271556edacd80f9d780a>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.TextFitToSizeType', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.TextFitToSizeType'
        __ooo_type_name__: str = 'enum'

        ALLLINES: TextFitToSizeType = TEXT_FIT_TO_SIZE_TYPE_ALLLINES
        """
        Nowadays this is the same as PROPORTIONAL.
        """
        AUTOFIT: TextFitToSizeType = TEXT_FIT_TO_SIZE_TYPE_AUTOFIT
        """
        The font size is scaled down (never up!) isotropically to fit the available space.
        
        Auto line-breaks will keep working.
        """
        NONE: TextFitToSizeType = TEXT_FIT_TO_SIZE_TYPE_NONE
        """
        the area is not filled.
        
        The text size is only defined by the font properties.
        
        Don't animate this text.
        
        the line is hidden.
        
        the joint between lines will not be connected
        
        the line has no special end.
        """
        PROPORTIONAL: TextFitToSizeType = TEXT_FIT_TO_SIZE_TYPE_PROPORTIONAL
        """
        The bitmap with the rendered glyphs is scaled up or down proportionally to fit the size of the shape.
        
        This may scale anisotropically. No AutoGrow and no Auto line-breaks in this case.
        
        On fontwork custom shapes, the rendering is different: each line of text is separately scaled proportionally to fit the width.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TextFitToSizeType(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.TextFitToSizeType", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.TextFitToSizeType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TextFitToSizeType']
