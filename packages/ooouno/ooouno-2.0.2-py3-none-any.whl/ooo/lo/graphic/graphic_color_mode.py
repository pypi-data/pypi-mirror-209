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
# Namespace: com.sun.star.graphic


class GraphicColorMode(object):
    """
    Const Class

    describes different color modes which can be specified when requesting a graphic.

    See Also:
        `API GraphicColorMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1graphic_1_1GraphicColorMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.GraphicColorMode'
    __ooo_type_name__: str = 'const'

    NORMAL = 0
    """
    describes normal graphic colors, no particular color transformation is applied to the graphics.
    """
    HIGH_CONTRAST = 1
    """
    used when requesting graphics which are suitable for a high-contrast environment.
    """

__all__ = ['GraphicColorMode']
