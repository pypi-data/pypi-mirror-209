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
# Namespace: com.sun.star.rendering
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from .render_state import RenderState as RenderState_e4490d27
    from .view_state import ViewState as ViewState_cab30c62
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20

class XSprite(XInterface_8f010a43):
    """
    Interface to control a sprite object.
    
    This is the basic interface to control a sprite object on a XSpriteCanvas. Sprites are moving, back-buffered objects.

    See Also:
        `API XSprite <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XSprite.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XSprite'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XSprite'

    @abstractmethod
    def clip(self, aClip: 'XPolyPolygon2D_e1b0e20') -> None:
        """
        Apply a clipping to the shape output.
        
        The given clip poly-polygon is always interpreted in device coordinate space. As the sprite has its own local coordinate system, with its origin on screen being equal to its current position, the clip poly-polygon's origin will always coincide with the sprite's origin. Furthermore, if any sprite transformation is set via transform(), the clip is subject to this transformation, too. The implementation is free, if it has a cached representation of the sprite at hand, to clip-output only this cached representation (e.g. a bitmap), instead of re-rendering the sprite from first principles. This is usually the case for an implementation of a XCustomSprite interface, since it typically has no other cached pictorial information at hand.
        
        Please note that if this sprite is not animated, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().
        
        Specifying an empty interface denotes no clipping, i.e. everything contained in the sprite will be visible (subject to device-dependent constraints, of course). Specifying an empty XPolyPolygon2D, i.e. a poly-polygon containing zero polygons, or an XPolyPolygon2D with any number of empty sub-polygons, denotes the NULL clip. That means, nothing from the sprite will be visible.
        """
        ...
    @abstractmethod
    def hide(self) -> None:
        """
        Make the sprite invisible.
        
        This method makes the sprite invisible.
        """
        ...
    @abstractmethod
    def move(self, aNewPos: 'RealPoint2D_d6e70c78', aViewState: 'ViewState_cab30c62', aRenderState: 'RenderState_e4490d27') -> None:
        """
        Move sprite to the specified position.
        
        The position specified here is first transformed by the combined view and render transformation. The resulting position is then used as the output position (also in device coordinates) of the rendered sprite content.
        
        Please note that if this sprite is not animated, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setAlpha(self, nAlpha: float) -> None:
        """
        Set overall transparency of the sprite.
        
        This method is useful for e.g. fading in/out of animations.
        
        Please note that if this sprite is not animated, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setPriority(self, nPriority: float) -> None:
        """
        Set sprite priority.
        
        The sprite priority determines the order of rendering relative to all other sprites of the associated canvas. The higher the priority, the later will the sprite be rendered, or, in other words, the closer to the screen surface the sprite is shown.
        """
        ...
    @abstractmethod
    def show(self) -> None:
        """
        Make the sprite visible.
        
        This method makes the sprite visible on the canvas it was created on.
        """
        ...
    @abstractmethod
    def transform(self, aTransformation: 'AffineMatrix2D_ff040da8') -> None:
        """
        Apply a local transformation to the sprite.
        
        The given transformation matrix locally transforms the sprite shape. If this transformation contains translational components, be aware that sprite content moved beyond the sprite area (a box from (0,0) to (spriteWidth,spriteHeight)) might (but need not) be clipped. Use XSprite.move() to change the sprite location on screen. The canvas implementations are free, if they have a cached representation of the sprite at hand, to transform only this cached representation (e.g. a bitmap), instead of re-rendering the sprite from first principles. This is usually the case for an implementation of a XCustomSprite interface, since it typically has no other cached pictorial information at hand.
        
        Please note that if this sprite is not animated, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XSprite']

