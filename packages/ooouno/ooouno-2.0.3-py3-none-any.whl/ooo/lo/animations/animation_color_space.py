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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.animations


class AnimationColorSpace(object):
    """
    Const Class

    defines the color space that is used for interpolation.
    
    This does not change how colors are interpreted but how to interpolate from one color to another.

    See Also:
        `API AnimationColorSpace <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationColorSpace.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.AnimationColorSpace'
    __ooo_type_name__: str = 'const'

    RGB = 0
    """
    defines that the RGB color space is used for interpolation.
    """
    HSL = 1
    """
    defines that the HSL color space is used for interpolation.
    """

__all__ = ['AnimationColorSpace']
