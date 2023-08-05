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

    from com.sun.star.presentation.AnimationEffect import APPEAR as ANIMATION_EFFECT_APPEAR
    from com.sun.star.presentation.AnimationEffect import CLOCKWISE as ANIMATION_EFFECT_CLOCKWISE
    from com.sun.star.presentation.AnimationEffect import CLOSE_HORIZONTAL as ANIMATION_EFFECT_CLOSE_HORIZONTAL
    from com.sun.star.presentation.AnimationEffect import CLOSE_VERTICAL as ANIMATION_EFFECT_CLOSE_VERTICAL
    from com.sun.star.presentation.AnimationEffect import COUNTERCLOCKWISE as ANIMATION_EFFECT_COUNTERCLOCKWISE
    from com.sun.star.presentation.AnimationEffect import DISSOLVE as ANIMATION_EFFECT_DISSOLVE
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_BOTTOM as ANIMATION_EFFECT_FADE_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_CENTER as ANIMATION_EFFECT_FADE_FROM_CENTER
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_LEFT as ANIMATION_EFFECT_FADE_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_LOWERLEFT as ANIMATION_EFFECT_FADE_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_LOWERRIGHT as ANIMATION_EFFECT_FADE_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_RIGHT as ANIMATION_EFFECT_FADE_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_TOP as ANIMATION_EFFECT_FADE_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_UPPERLEFT as ANIMATION_EFFECT_FADE_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import FADE_FROM_UPPERRIGHT as ANIMATION_EFFECT_FADE_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import FADE_TO_CENTER as ANIMATION_EFFECT_FADE_TO_CENTER
    from com.sun.star.presentation.AnimationEffect import HIDE as ANIMATION_EFFECT_HIDE
    from com.sun.star.presentation.AnimationEffect import HORIZONTAL_CHECKERBOARD as ANIMATION_EFFECT_HORIZONTAL_CHECKERBOARD
    from com.sun.star.presentation.AnimationEffect import HORIZONTAL_LINES as ANIMATION_EFFECT_HORIZONTAL_LINES
    from com.sun.star.presentation.AnimationEffect import HORIZONTAL_ROTATE as ANIMATION_EFFECT_HORIZONTAL_ROTATE
    from com.sun.star.presentation.AnimationEffect import HORIZONTAL_STRETCH as ANIMATION_EFFECT_HORIZONTAL_STRETCH
    from com.sun.star.presentation.AnimationEffect import HORIZONTAL_STRIPES as ANIMATION_EFFECT_HORIZONTAL_STRIPES
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_BOTTOM as ANIMATION_EFFECT_LASER_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_LEFT as ANIMATION_EFFECT_LASER_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_LOWERLEFT as ANIMATION_EFFECT_LASER_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_LOWERRIGHT as ANIMATION_EFFECT_LASER_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_RIGHT as ANIMATION_EFFECT_LASER_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_TOP as ANIMATION_EFFECT_LASER_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_UPPERLEFT as ANIMATION_EFFECT_LASER_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import LASER_FROM_UPPERRIGHT as ANIMATION_EFFECT_LASER_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_BOTTOM as ANIMATION_EFFECT_MOVE_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_LEFT as ANIMATION_EFFECT_MOVE_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_LOWERLEFT as ANIMATION_EFFECT_MOVE_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_LOWERRIGHT as ANIMATION_EFFECT_MOVE_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_RIGHT as ANIMATION_EFFECT_MOVE_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_TOP as ANIMATION_EFFECT_MOVE_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_UPPERLEFT as ANIMATION_EFFECT_MOVE_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_FROM_UPPERRIGHT as ANIMATION_EFFECT_MOVE_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_BOTTOM as ANIMATION_EFFECT_MOVE_SHORT_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_LEFT as ANIMATION_EFFECT_MOVE_SHORT_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_LOWERLEFT as ANIMATION_EFFECT_MOVE_SHORT_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_LOWERRIGHT as ANIMATION_EFFECT_MOVE_SHORT_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_RIGHT as ANIMATION_EFFECT_MOVE_SHORT_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_TOP as ANIMATION_EFFECT_MOVE_SHORT_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_UPPERLEFT as ANIMATION_EFFECT_MOVE_SHORT_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_FROM_UPPERRIGHT as ANIMATION_EFFECT_MOVE_SHORT_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_BOTTOM as ANIMATION_EFFECT_MOVE_SHORT_TO_BOTTOM
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_LEFT as ANIMATION_EFFECT_MOVE_SHORT_TO_LEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_LOWERLEFT as ANIMATION_EFFECT_MOVE_SHORT_TO_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_LOWERRIGHT as ANIMATION_EFFECT_MOVE_SHORT_TO_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_RIGHT as ANIMATION_EFFECT_MOVE_SHORT_TO_RIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_TOP as ANIMATION_EFFECT_MOVE_SHORT_TO_TOP
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_UPPERLEFT as ANIMATION_EFFECT_MOVE_SHORT_TO_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_SHORT_TO_UPPERRIGHT as ANIMATION_EFFECT_MOVE_SHORT_TO_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_BOTTOM as ANIMATION_EFFECT_MOVE_TO_BOTTOM
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_LEFT as ANIMATION_EFFECT_MOVE_TO_LEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_LOWERLEFT as ANIMATION_EFFECT_MOVE_TO_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_LOWERRIGHT as ANIMATION_EFFECT_MOVE_TO_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_RIGHT as ANIMATION_EFFECT_MOVE_TO_RIGHT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_TOP as ANIMATION_EFFECT_MOVE_TO_TOP
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_UPPERLEFT as ANIMATION_EFFECT_MOVE_TO_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import MOVE_TO_UPPERRIGHT as ANIMATION_EFFECT_MOVE_TO_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import NONE as ANIMATION_EFFECT_NONE
    from com.sun.star.presentation.AnimationEffect import OPEN_HORIZONTAL as ANIMATION_EFFECT_OPEN_HORIZONTAL
    from com.sun.star.presentation.AnimationEffect import OPEN_VERTICAL as ANIMATION_EFFECT_OPEN_VERTICAL
    from com.sun.star.presentation.AnimationEffect import PATH as ANIMATION_EFFECT_PATH
    from com.sun.star.presentation.AnimationEffect import RANDOM as ANIMATION_EFFECT_RANDOM
    from com.sun.star.presentation.AnimationEffect import SPIRALIN_LEFT as ANIMATION_EFFECT_SPIRALIN_LEFT
    from com.sun.star.presentation.AnimationEffect import SPIRALIN_RIGHT as ANIMATION_EFFECT_SPIRALIN_RIGHT
    from com.sun.star.presentation.AnimationEffect import SPIRALOUT_LEFT as ANIMATION_EFFECT_SPIRALOUT_LEFT
    from com.sun.star.presentation.AnimationEffect import SPIRALOUT_RIGHT as ANIMATION_EFFECT_SPIRALOUT_RIGHT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_BOTTOM as ANIMATION_EFFECT_STRETCH_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_LEFT as ANIMATION_EFFECT_STRETCH_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_LOWERLEFT as ANIMATION_EFFECT_STRETCH_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_LOWERRIGHT as ANIMATION_EFFECT_STRETCH_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_RIGHT as ANIMATION_EFFECT_STRETCH_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_TOP as ANIMATION_EFFECT_STRETCH_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_UPPERLEFT as ANIMATION_EFFECT_STRETCH_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import STRETCH_FROM_UPPERRIGHT as ANIMATION_EFFECT_STRETCH_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import VERTICAL_CHECKERBOARD as ANIMATION_EFFECT_VERTICAL_CHECKERBOARD
    from com.sun.star.presentation.AnimationEffect import VERTICAL_LINES as ANIMATION_EFFECT_VERTICAL_LINES
    from com.sun.star.presentation.AnimationEffect import VERTICAL_ROTATE as ANIMATION_EFFECT_VERTICAL_ROTATE
    from com.sun.star.presentation.AnimationEffect import VERTICAL_STRETCH as ANIMATION_EFFECT_VERTICAL_STRETCH
    from com.sun.star.presentation.AnimationEffect import VERTICAL_STRIPES as ANIMATION_EFFECT_VERTICAL_STRIPES
    from com.sun.star.presentation.AnimationEffect import WAVYLINE_FROM_BOTTOM as ANIMATION_EFFECT_WAVYLINE_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import WAVYLINE_FROM_LEFT as ANIMATION_EFFECT_WAVYLINE_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import WAVYLINE_FROM_RIGHT as ANIMATION_EFFECT_WAVYLINE_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import WAVYLINE_FROM_TOP as ANIMATION_EFFECT_WAVYLINE_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN as ANIMATION_EFFECT_ZOOM_IN
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_BOTTOM as ANIMATION_EFFECT_ZOOM_IN_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_CENTER as ANIMATION_EFFECT_ZOOM_IN_FROM_CENTER
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_LEFT as ANIMATION_EFFECT_ZOOM_IN_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_LOWERLEFT as ANIMATION_EFFECT_ZOOM_IN_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_LOWERRIGHT as ANIMATION_EFFECT_ZOOM_IN_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_RIGHT as ANIMATION_EFFECT_ZOOM_IN_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_TOP as ANIMATION_EFFECT_ZOOM_IN_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_UPPERLEFT as ANIMATION_EFFECT_ZOOM_IN_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_FROM_UPPERRIGHT as ANIMATION_EFFECT_ZOOM_IN_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_SMALL as ANIMATION_EFFECT_ZOOM_IN_SMALL
    from com.sun.star.presentation.AnimationEffect import ZOOM_IN_SPIRAL as ANIMATION_EFFECT_ZOOM_IN_SPIRAL
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT as ANIMATION_EFFECT_ZOOM_OUT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_BOTTOM as ANIMATION_EFFECT_ZOOM_OUT_FROM_BOTTOM
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_CENTER as ANIMATION_EFFECT_ZOOM_OUT_FROM_CENTER
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_LEFT as ANIMATION_EFFECT_ZOOM_OUT_FROM_LEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_LOWERLEFT as ANIMATION_EFFECT_ZOOM_OUT_FROM_LOWERLEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_LOWERRIGHT as ANIMATION_EFFECT_ZOOM_OUT_FROM_LOWERRIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_RIGHT as ANIMATION_EFFECT_ZOOM_OUT_FROM_RIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_TOP as ANIMATION_EFFECT_ZOOM_OUT_FROM_TOP
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_UPPERLEFT as ANIMATION_EFFECT_ZOOM_OUT_FROM_UPPERLEFT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_FROM_UPPERRIGHT as ANIMATION_EFFECT_ZOOM_OUT_FROM_UPPERRIGHT
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_SMALL as ANIMATION_EFFECT_ZOOM_OUT_SMALL
    from com.sun.star.presentation.AnimationEffect import ZOOM_OUT_SPIRAL as ANIMATION_EFFECT_ZOOM_OUT_SPIRAL

    class AnimationEffect(uno.Enum):
        """
        Enum Class


        See Also:
            `API AnimationEffect <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a10f2a3114ab31c0e6f7dc48f656fd260>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.presentation.AnimationEffect', value)

        __ooo_ns__: str = 'com.sun.star.presentation'
        __ooo_full_ns__: str = 'com.sun.star.presentation.AnimationEffect'
        __ooo_type_name__: str = 'enum'

        APPEAR = cast("AnimationEffect", ANIMATION_EFFECT_APPEAR)
        """
        use the animation effect \"Appear\".
        """
        CLOCKWISE = cast("AnimationEffect", ANIMATION_EFFECT_CLOCKWISE)
        """
        use the animation effect \"Clockwise\".
        
        use the fade effect \"Clockwise\".
        """
        CLOSE_HORIZONTAL = cast("AnimationEffect", ANIMATION_EFFECT_CLOSE_HORIZONTAL)
        """
        use the animation effect \"Close Horizontal\".
        
        use the fade effect \"Close Horizontal\".
        """
        CLOSE_VERTICAL = cast("AnimationEffect", ANIMATION_EFFECT_CLOSE_VERTICAL)
        """
        use the animation effect \"Close Vertical\".
        
        use the fade effect \"Close Vertical\".
        """
        COUNTERCLOCKWISE = cast("AnimationEffect", ANIMATION_EFFECT_COUNTERCLOCKWISE)
        """
        use the animation effect \"Counter Clockwise\".
        
        use the fade effect \"Counter Clockwise\".
        """
        DISSOLVE = cast("AnimationEffect", ANIMATION_EFFECT_DISSOLVE)
        """
        use the animation effect \"Spiral Inward Left\".
        
        use the fade effect \"Dissolve\".
        """
        FADE_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_BOTTOM)
        """
        use the animation effect \"Fade from Bottom\".
        
        use the fade effect \"Fade from Bottom\".
        """
        FADE_FROM_CENTER = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_CENTER)
        """
        use the animation effect \"Fade from Center\".
        
        use the fade effect \"Fade from Center\".
        """
        FADE_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_LEFT)
        """
        use the animation effect \"Fade from Left\".
        
        use the fade effect \"Fade from Left\".
        """
        FADE_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_LOWERLEFT)
        """
        use the animation effect \"Fade from Lower Left\".
        
        use the fade effect \"Fade from Lower Left\".
        """
        FADE_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_LOWERRIGHT)
        """
        use the animation effect \"Fade from Lower Right\".
        
        use the fade effect \"Fade from Lower Right\".
        """
        FADE_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_RIGHT)
        """
        use the animation effect \"Fade from Right\".
        
        use the fade effect \"Fade from Right\".
        """
        FADE_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_TOP)
        """
        use the animation effect \"Fade from Top\".
        
        use the fade effect \"Fade from Top\".
        """
        FADE_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_UPPERLEFT)
        """
        use the animation effect \"Fade from Upper Left\".
        
        use the fade effect \"Fade from Upper Left\".
        """
        FADE_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_FADE_FROM_UPPERRIGHT)
        """
        use the animation effect \"Fade from Upper Right\".
        
        use the fade effect \"Fade from Upper Right\".
        """
        FADE_TO_CENTER = cast("AnimationEffect", ANIMATION_EFFECT_FADE_TO_CENTER)
        """
        use the animation effect \"Fade to Center\".
        
        use the fade effect \"Fade to Center\".
        """
        HIDE = cast("AnimationEffect", ANIMATION_EFFECT_HIDE)
        """
        use the animation effect \"Hide\".
        """
        HORIZONTAL_CHECKERBOARD = cast("AnimationEffect", ANIMATION_EFFECT_HORIZONTAL_CHECKERBOARD)
        """
        use the animation effect \"Horizontal Checkerboard\".
        
        use the fade effect \"Horizontal Checkerboard\".
        """
        HORIZONTAL_LINES = cast("AnimationEffect", ANIMATION_EFFECT_HORIZONTAL_LINES)
        """
        use the animation effect \"Horizontal Lines\".
        
        use the fade effect \"Horizontal Lines\".
        """
        HORIZONTAL_ROTATE = cast("AnimationEffect", ANIMATION_EFFECT_HORIZONTAL_ROTATE)
        """
        use the animation effect \"Horizontal Rotate\".
        """
        HORIZONTAL_STRETCH = cast("AnimationEffect", ANIMATION_EFFECT_HORIZONTAL_STRETCH)
        """
        use the animation effect \"Horizontal Stretch\".
        """
        HORIZONTAL_STRIPES = cast("AnimationEffect", ANIMATION_EFFECT_HORIZONTAL_STRIPES)
        """
        use the animation effect \"Horizontal Stripes\".
        
        use the fade effect \"Horizontal Stripes\".
        """
        LASER_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_BOTTOM)
        """
        use the animation effect \"Laser from Bottom\".
        """
        LASER_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_LEFT)
        """
        use the animation effect \"Wavy Line from Left\".
        """
        LASER_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_LOWERLEFT)
        """
        use the animation effect \"Laser from Lower Left\".
        """
        LASER_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_LOWERRIGHT)
        """
        use the animation effect \"Laser from Lower Right\".
        """
        LASER_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_RIGHT)
        """
        use the animation effect \"Laser from Right\".
        """
        LASER_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_TOP)
        """
        use the animation effect \"Laser from Top\".
        """
        LASER_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_UPPERLEFT)
        """
        use the animation effect \"Laser from Upper Left\".
        """
        LASER_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_LASER_FROM_UPPERRIGHT)
        """
        use the animation effect \"Laser from Upper Right\".
        """
        MOVE_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_BOTTOM)
        """
        use the animation effect \"Move from Bottom\".
        
        use the fade effect \"Move from Bottom\".
        """
        MOVE_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_LEFT)
        """
        use the animation effect \"Move from Left\".
        
        use the fade effect \"Move from Left\".
        """
        MOVE_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_LOWERLEFT)
        """
        use the animation effect \"Move from Lower Left\".
        
        use the fade effect \"Move from Lower Left\".
        """
        MOVE_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_LOWERRIGHT)
        """
        use the animation effect \"Move from Lower Right\".
        
        use the fade effect \"Move from Lower Right\".
        """
        MOVE_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_RIGHT)
        """
        use the animation effect \"Move from Right\".
        
        use the fade effect \"Move from Right\".
        """
        MOVE_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_TOP)
        """
        use the animation effect \"Move from Top\".
        
        use the fade effect \"Move from Top\".
        """
        MOVE_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_UPPERLEFT)
        """
        use the animation effect \"Move from Upper Left\".
        
        use the fade effect \"Move from Upper Left\".
        """
        MOVE_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_FROM_UPPERRIGHT)
        """
        use the animation effect \"Move from Upper Right\".
        
        use the fade effect \"Move from Upper Right\".
        """
        MOVE_SHORT_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_BOTTOM)
        """
        use the animation effect \"Move Short from Bottom\".
        """
        MOVE_SHORT_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_LEFT)
        """
        use the animation effect \"Move Short from Left\".
        """
        MOVE_SHORT_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_LOWERLEFT)
        """
        use the animation effect \"Move Short from Lower Left\".
        """
        MOVE_SHORT_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_LOWERRIGHT)
        """
        use the animation effect \"Move Short from Lower Right\".
        """
        MOVE_SHORT_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_RIGHT)
        """
        use the animation effect \"Move Short from Right\".
        """
        MOVE_SHORT_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_TOP)
        """
        use the animation effect \"Move Short from Top\".
        """
        MOVE_SHORT_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_UPPERLEFT)
        """
        use the animation effect \"Move Short from Upper Left\".
        """
        MOVE_SHORT_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_FROM_UPPERRIGHT)
        """
        use the animation effect \"Move Short from Upper Right\".
        """
        MOVE_SHORT_TO_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_BOTTOM)
        """
        use the animation effect \"Move Short to Bottom\".
        """
        MOVE_SHORT_TO_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_LEFT)
        """
        use the animation effect \"Move Short to Left\".
        """
        MOVE_SHORT_TO_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_LOWERLEFT)
        """
        use the animation effect \"Move Short to Lower Left\".
        """
        MOVE_SHORT_TO_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_LOWERRIGHT)
        """
        use the animation effect \"Move Short to Lower Right\".
        """
        MOVE_SHORT_TO_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_RIGHT)
        """
        use the animation effect \"Move Short to Right\".
        """
        MOVE_SHORT_TO_TOP = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_TOP)
        """
        use the animation effect \"Move Short to Top\".
        """
        MOVE_SHORT_TO_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_UPPERLEFT)
        """
        use the animation effect \"Move Short to Upper Left\".
        """
        MOVE_SHORT_TO_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_SHORT_TO_UPPERRIGHT)
        """
        use the animation effect \"Move Short to Upper Right\".
        """
        MOVE_TO_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_BOTTOM)
        """
        use the animation effect \"Move to Bottom\".
        """
        MOVE_TO_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_LEFT)
        """
        use the animation effect \"Move to Left\".
        """
        MOVE_TO_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_LOWERLEFT)
        """
        use the animation effect \"Move to Lower Left\".
        """
        MOVE_TO_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_LOWERRIGHT)
        """
        use the animation effect \"Move to Lower Right\".
        """
        MOVE_TO_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_RIGHT)
        """
        use the animation effect \"Move to Right\".
        """
        MOVE_TO_TOP = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_TOP)
        """
        use the animation effect \"Move to Top\".
        """
        MOVE_TO_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_UPPERLEFT)
        """
        use the animation effect \"Move to Upper Left\".
        """
        MOVE_TO_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_MOVE_TO_UPPERRIGHT)
        """
        use the animation effect \"Move to Upper Right\".
        """
        NONE = cast("AnimationEffect", ANIMATION_EFFECT_NONE)
        """
        use no animation effects.
        
        use no fade effects.
        
        No action is performed on click.
        """
        OPEN_HORIZONTAL = cast("AnimationEffect", ANIMATION_EFFECT_OPEN_HORIZONTAL)
        """
        use the animation effect \"Open Horizontal\".
        
        use the fade effect \"Open Horizontal\".
        """
        OPEN_VERTICAL = cast("AnimationEffect", ANIMATION_EFFECT_OPEN_VERTICAL)
        """
        use the animation effect \"Open Vertical\".
        
        use the fade effect \"Open Vertical\".
        """
        PATH = cast("AnimationEffect", ANIMATION_EFFECT_PATH)
        """
        use the animation effect \"Path\".
        """
        RANDOM = cast("AnimationEffect", ANIMATION_EFFECT_RANDOM)
        """
        use the animation effect \"Random\".
        
        use the fade effect \"Random\".
        """
        SPIRALIN_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_SPIRALIN_LEFT)
        """
        use the animation effect \"Spiral Inward Left\".
        
        use the fade effect \"Spiral Inward Left\".
        """
        SPIRALIN_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_SPIRALIN_RIGHT)
        """
        use the animation effect \"Spiral Inward Right\".
        
        use the fade effect \"Spiral Inward Right\".
        """
        SPIRALOUT_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_SPIRALOUT_LEFT)
        """
        use the animation effect \"Spiral Outward Left\".
        
        use the fade effect \"Spiral Outward Left\".
        """
        SPIRALOUT_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_SPIRALOUT_RIGHT)
        """
        use the animation effect \"Spiral Outward Right\".
        
        use the fade effect \"Spiral Outward Right\".
        """
        STRETCH_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_BOTTOM)
        """
        use the animation effect \"Stretch From Bottom\".
        
        use the fade effect \"Stretch from Bottom\".
        """
        STRETCH_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_LEFT)
        """
        use the animation effect \"Stretch From Left\".
        
        use the fade effect \"Stretch from Left\".
        """
        STRETCH_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_LOWERLEFT)
        """
        use the animation effect \"Stretch From Lower Left\".
        """
        STRETCH_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_LOWERRIGHT)
        """
        use the animation effect \"Stretch From Lower Right\".
        """
        STRETCH_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_RIGHT)
        """
        use the animation effect \"Stretch From Right\".
        
        use the fade effect \"Stretch from Right\".
        """
        STRETCH_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_TOP)
        """
        use the animation effect \"Stretch From Top\".
        
        use the fade effect \"Stretch from Top\".
        """
        STRETCH_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_UPPERLEFT)
        """
        use the animation effect \"Stretch From Upper Left\".
        """
        STRETCH_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_STRETCH_FROM_UPPERRIGHT)
        """
        use the animation effect \"Stretch From Upper Right\".
        """
        VERTICAL_CHECKERBOARD = cast("AnimationEffect", ANIMATION_EFFECT_VERTICAL_CHECKERBOARD)
        """
        use the animation effect \"Vertical Checkerboard\".
        
        use the fade effect \"Vertical Checkerboard\".
        """
        VERTICAL_LINES = cast("AnimationEffect", ANIMATION_EFFECT_VERTICAL_LINES)
        """
        use the animation effect \"Vertical Lines\".
        
        use the fade effect \"Vertical Lines\".
        """
        VERTICAL_ROTATE = cast("AnimationEffect", ANIMATION_EFFECT_VERTICAL_ROTATE)
        """
        use the animation effect \"Vertical Rotate\".
        """
        VERTICAL_STRETCH = cast("AnimationEffect", ANIMATION_EFFECT_VERTICAL_STRETCH)
        """
        use the animation effect \"Vertical Stretch\".
        """
        VERTICAL_STRIPES = cast("AnimationEffect", ANIMATION_EFFECT_VERTICAL_STRIPES)
        """
        use the animation effect \"Vertical Stripes\".
        
        use the fade effect \"Vertical Stripes\".
        """
        WAVYLINE_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_WAVYLINE_FROM_BOTTOM)
        """
        use the animation effect \"Wavy Line from Button\".
        
        use the fade effect \"Wavy Line from Bottom\".
        """
        WAVYLINE_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_WAVYLINE_FROM_LEFT)
        """
        use the animation effect \"Wavy Line from Left\".
        
        use the fade effect \"Wavy Line from Left\".
        """
        WAVYLINE_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_WAVYLINE_FROM_RIGHT)
        """
        use the animation effect \"Wavy Line from Right\".
        
        use the fade effect \"Wavy Line from Right\".
        """
        WAVYLINE_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_WAVYLINE_FROM_TOP)
        """
        use the animation effect \"Wavy Line from Top\".
        
        use the fade effect \"Wavy Line from Top\".
        """
        ZOOM_IN = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN)
        """
        use the animation effect \"Zoom In\".
        """
        ZOOM_IN_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_BOTTOM)
        """
        use the animation effect \"Zoom In From Bottom\".
        """
        ZOOM_IN_FROM_CENTER = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_CENTER)
        """
        use the animation effect \"Zoom In From Center\".
        """
        ZOOM_IN_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_LEFT)
        """
        use the animation effect \"Zoom In From Left\".
        """
        ZOOM_IN_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_LOWERLEFT)
        """
        use the animation effect \"Zoom In From Lower Left\".
        """
        ZOOM_IN_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_LOWERRIGHT)
        """
        use the animation effect \"Zoom In From Lower Right\".
        """
        ZOOM_IN_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_RIGHT)
        """
        use the animation effect \"Zoom In From Right\".
        """
        ZOOM_IN_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_TOP)
        """
        use the animation effect \"Zoom In From Top\".
        """
        ZOOM_IN_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_UPPERLEFT)
        """
        use the animation effect \"Zoom In From Upper Left\".
        """
        ZOOM_IN_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_FROM_UPPERRIGHT)
        """
        use the animation effect \"Zoom In From Upper Right\".
        """
        ZOOM_IN_SMALL = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_SMALL)
        """
        use the animation effect \"Zoom In Small\".
        """
        ZOOM_IN_SPIRAL = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_IN_SPIRAL)
        """
        use the animation effect \"Zoom In Spiral\".
        """
        ZOOM_OUT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT)
        """
        use the animation effect \"Zoom Out\".
        """
        ZOOM_OUT_FROM_BOTTOM = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_BOTTOM)
        """
        use the animation effect \"Zoom Out From Bottom\".
        """
        ZOOM_OUT_FROM_CENTER = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_CENTER)
        """
        use the animation effect \"Zoom Out From Center\".
        """
        ZOOM_OUT_FROM_LEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_LEFT)
        """
        use the animation effect \"Zoom Out From Left\".
        """
        ZOOM_OUT_FROM_LOWERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_LOWERLEFT)
        """
        use the animation effect \"Zoom Out From Lower Left\".
        """
        ZOOM_OUT_FROM_LOWERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_LOWERRIGHT)
        """
        use the animation effect \"Zoom Out From Lower Right\".
        """
        ZOOM_OUT_FROM_RIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_RIGHT)
        """
        use the animation effect \"Zoom Out From Right\".
        """
        ZOOM_OUT_FROM_TOP = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_TOP)
        """
        use the animation effect \"Zoom Out From Top\".
        """
        ZOOM_OUT_FROM_UPPERLEFT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_UPPERLEFT)
        """
        use the animation effect \"Zoom Out From Upper Left\".
        """
        ZOOM_OUT_FROM_UPPERRIGHT = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_FROM_UPPERRIGHT)
        """
        use the animation effect \"Zoom Out From Upper Right\".
        """
        ZOOM_OUT_SMALL = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_SMALL)
        """
        use the animation effect \"Zoom Out Small\".
        """
        ZOOM_OUT_SPIRAL = cast("AnimationEffect", ANIMATION_EFFECT_ZOOM_OUT_SPIRAL)
        """
        use the animation effect \"Zoom Out Spiral\".
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class AnimationEffect(metaclass=UnoEnumMeta, type_name="com.sun.star.presentation.AnimationEffect", name_space="com.sun.star.presentation"):
        """Dynamically created class that represents ``com.sun.star.presentation.AnimationEffect`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['AnimationEffect']
