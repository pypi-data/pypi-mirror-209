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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from .gradient import Gradient as Gradient_7a8a0982
    from .raster_operation import RasterOperation as RasterOperation_c9430c76
    from .simple_font_metric import SimpleFontMetric as SimpleFontMetric_d53c0cb9
    from .x_device import XDevice as XDevice_70ba08fc
    from .x_display_bitmap import XDisplayBitmap as XDisplayBitmap_bb550bdf
    from .x_font import XFont as XFont_5f480843
    from .x_region import XRegion as XRegion_70f30910
    from ..util.color import Color as Color_68e908c5

class XGraphics(XInterface_8f010a43):
    """
    provides the basic output operation of a device.

    See Also:
        `API XGraphics <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XGraphics.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XGraphics'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XGraphics'

    @abstractmethod
    def copy(self, xSource: 'XDevice_70ba08fc', nSourceX: int, nSourceY: int, nSourceWidth: int, nSourceHeight: int, nDestX: int, nDestY: int, nDestWidth: int, nDestHeight: int) -> None:
        """
        copies a rectangle of pixels from another device into this one.
        """
        ...
    @abstractmethod
    def draw(self, xBitmapHandle: 'XDisplayBitmap_bb550bdf', SourceX: int, SourceY: int, SourceWidth: int, SourceHeight: int, DestX: int, DestY: int, DestWidth: int, DestHeight: int) -> None:
        """
        draws a part of the specified bitmap to the output device.
        """
        ...
    @abstractmethod
    def drawArc(self, X: int, Y: int, Width: int, Height: int, X1: int, Y1: int, X2: int, Y2: int) -> None:
        """
        draws an arc (part of a circle) in the output device.
        """
        ...
    @abstractmethod
    def drawChord(self, nX: int, nY: int, nWidth: int, nHeight: int, nX1: int, nY1: int, nX2: int, nY2: int) -> None:
        """
        draws a chord of a circular area in the output device.
        
        A chord is a segment of a circle. You get two chords from a circle if you intersect the circle with a straight line joining two points on the circle.
        """
        ...
    @abstractmethod
    def drawEllipse(self, X: int, Y: int, Width: int, Height: int) -> None:
        """
        draws an ellipse in the output device.
        """
        ...
    @abstractmethod
    def drawGradient(self, nX: int, nY: int, nWidth: int, Height: int, aGradient: 'Gradient_7a8a0982') -> None:
        """
        draws a color dispersion in the output device.
        """
        ...
    @abstractmethod
    def drawLine(self, X1: int, Y1: int, X2: int, Y2: int) -> None:
        """
        draws a line in the output device.
        """
        ...
    @abstractmethod
    def drawPie(self, X: int, Y: int, Width: int, Height: int, X1: int, Y1: int, X2: int, Y2: int) -> None:
        """
        draws a circular area in the output device.
        """
        ...
    @abstractmethod
    def drawPixel(self, X: int, Y: int) -> None:
        """
        sets a single pixel in the output device.
        """
        ...
    @abstractmethod
    def drawPolyLine(self, DataX: uno.ByteSequence, DataY: uno.ByteSequence) -> None:
        """
        draws multiple lines in the output device at once.
        """
        ...
    @abstractmethod
    def drawPolyPolygon(self, DataX: 'typing.Tuple[uno.ByteSequence, ...]', DataY: 'typing.Tuple[uno.ByteSequence, ...]') -> None:
        """
        draws multiple polygons in the output device at once.
        """
        ...
    @abstractmethod
    def drawPolygon(self, DataX: uno.ByteSequence, DataY: uno.ByteSequence) -> None:
        """
        draws a polygon line in the output device.
        """
        ...
    @abstractmethod
    def drawRect(self, X: int, Y: int, Width: int, Height: int) -> None:
        """
        draws a rectangle in the output device.
        """
        ...
    @abstractmethod
    def drawRoundedRect(self, X: int, Y: int, Width: int, Height: int, nHorzRound: int, nVertRound: int) -> None:
        """
        draws a rectangle with rounded corners in the output device.
        """
        ...
    @abstractmethod
    def drawText(self, X: int, Y: int, Text: str) -> None:
        """
        draws text in the output device.
        """
        ...
    @abstractmethod
    def drawTextArray(self, X: int, Y: int, Text: str, Longs: uno.ByteSequence) -> None:
        """
        draws texts in the output device using an explicit kerning table.
        """
        ...
    @abstractmethod
    def getDevice(self) -> 'XDevice_70ba08fc':
        """
        returns the device of this graphics.
        """
        ...
    @abstractmethod
    def getFontMetric(self) -> 'SimpleFontMetric_d53c0cb9':
        """
        returns the font metric of the current font.
        """
        ...
    @abstractmethod
    def intersectClipRegion(self, xClipping: 'XRegion_70f30910') -> None:
        """
        builds the intersection with the current region.
        """
        ...
    @abstractmethod
    def pop(self) -> None:
        """
        restores all previous saved settings.
        """
        ...
    @abstractmethod
    def push(self) -> None:
        """
        saves all current settings (Font, TextColor, TextFillColor, LineColor, FillColor, RasterOp, ClipRegion).
        """
        ...
    @abstractmethod
    def selectFont(self, aDescription: 'FontDescriptor_bc110c0a') -> None:
        """
        creates a new font and sets the font.
        """
        ...
    @abstractmethod
    def setClipRegion(self, Clipping: 'XRegion_70f30910') -> None:
        """
        sets the clip region to specified clipping.
        """
        ...
    @abstractmethod
    def setFillColor(self, nColor: 'Color_68e908c5') -> None:
        """
        sets the fill color.
        """
        ...
    @abstractmethod
    def setFont(self, xNewFont: 'XFont_5f480843') -> None:
        """
        sets the font used by text operations.
        """
        ...
    @abstractmethod
    def setLineColor(self, nColor: 'Color_68e908c5') -> None:
        """
        sets the line color.
        """
        ...
    @abstractmethod
    def setRasterOp(self, ROP: 'RasterOperation_c9430c76') -> None:
        """
        sets the raster operation.
        
        If the device does not support raster operations then this call is ignored.
        """
        ...
    @abstractmethod
    def setTextColor(self, nColor: 'Color_68e908c5') -> None:
        """
        sets the text color used by text operations.
        """
        ...
    @abstractmethod
    def setTextFillColor(self, nColor: 'Color_68e908c5') -> None:
        """
        sets the fill color used by text operations.
        """
        ...

__all__ = ['XGraphics']

