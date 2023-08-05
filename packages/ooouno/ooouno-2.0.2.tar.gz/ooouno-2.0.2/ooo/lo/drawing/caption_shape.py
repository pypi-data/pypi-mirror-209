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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing
import typing
from abc import abstractproperty
from .fill_properties import FillProperties as FillProperties_f1200da8
from .line_properties import LineProperties as LineProperties_f13f0da9
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class CaptionShape(FillProperties_f1200da8, LineProperties_f13f0da9, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    The CaptionShape represents a rectangular drawing shape with an additional set of lines.
    
    It can be used as a description for a fixed point inside a drawing.

    See Also:
        `API CaptionShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1CaptionShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.CaptionShape'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CaptionAngle(self) -> int:
        """
        This property specifies the escape angle of the line of a caption.
        
        It is only used if CaptionIsFixedAngle is set to TRUE
        """
        ...

    @abstractproperty
    def CaptionEscapeAbsolute(self) -> int:
        """
        This property specifies the absolute escape distance for the line of a caption.
        """
        ...

    @abstractproperty
    def CaptionEscapeDirection(self) -> int:
        """
        This property specifies the escape direction for the line of a caption.
        """
        ...

    @abstractproperty
    def CaptionEscapeRelative(self) -> int:
        """
        This property specifies the relative escape distance for the line of a caption.
        """
        ...

    @abstractproperty
    def CaptionGap(self) -> int:
        """
        This property specifies the distance between the text area of the caption and the start of the line.
        """
        ...

    @abstractproperty
    def CaptionIsEscapeRelative(self) -> bool:
        """
        If this property is TRUE, the property CaptionEscapeRelative is used, else the property CaptionEscapeAbsolute is used.
        """
        ...

    @abstractproperty
    def CaptionIsFitLineLength(self) -> bool:
        """
        If this property is TRUE, the application determines the best possible length for the caption line.
        """
        ...

    @abstractproperty
    def CaptionIsFixedAngle(self) -> bool:
        """
        This property specifies if the escape angle of the line of a caption is fixed or free.
        
        If this is set to FALSE, the application can choose the best possible angle. If not, the value in CaptionAngle is used.
        """
        ...

    @abstractproperty
    def CaptionLineLength(self) -> int:
        """
        This property specifies the length of the caption line.
        """
        ...

    @abstractproperty
    def CaptionPoint(self) -> 'Point_5fb2085e':
        """
        The caption point property specify the position of the point that is captioned.
        
        A set of lines are rendered from the caption area.
        """
        ...

    @abstractproperty
    def CaptionType(self) -> int:
        """
        This property specifies the geometry of the line of a caption.
        """
        ...

    @abstractproperty
    def CornerRadius(self) -> int:
        """
        This is the radius of the caption area corners.
        """
        ...


__all__ = ['CaptionShape']

