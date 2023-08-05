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
# Namespace: com.sun.star.rendering


class FloatingPointBitmapFormat(object):
    """
    Const Class

    This structure describes format of a floating point bitmap.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FloatingPointBitmapFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1FloatingPointBitmapFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FloatingPointBitmapFormat'
    __ooo_type_name__: str = 'const'

    HALFFLOAT = 0
    """
    Half-float format.
    
    The color components are stored in the half-float format, i.e. in a 16 bit value, with 5 bit exponent, 10 bit mantissa and a sign bit. See also OpenEXR for a format employing half-floats.
    """
    FLOAT = 1
    """
    IEEE float format.
    
    The color components are stored in the IEEE single-precision floating point format, i.e. in a 32 bit value, with 8 bit exponent, 23 bit mantissa and a sign bit.
    """
    DOUBLE = 2
    """
    IEEE double format.
    
    The color components are stored in the IEEE double-precision floating point format, i.e. in a 64 bit value, with 16 bit exponent, 47 bit mantissa and a sign bit.
    """

__all__ = ['FloatingPointBitmapFormat']
