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
from .shape import Shape as Shape_85cc09e5
from .x_shape_group import XShapeGroup as XShapeGroup_c8d30c4a
from .x_shapes import XShapes as XShapes_9a800ab0

class GroupShape(Shape_85cc09e5, XShapeGroup_c8d30c4a, XShapes_9a800ab0):
    """
    Service Class

    This service is for a group of Shapes.

    See Also:
        `API GroupShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1GroupShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.GroupShape'
    __ooo_type_name__: str = 'service'


__all__ = ['GroupShape']

