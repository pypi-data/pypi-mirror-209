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
# Namespace: com.sun.star.text
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from ..drawing.x_shape import XShape as XShape_8fd00a3d
from .base_frame_properties import BaseFrameProperties as BaseFrameProperties_b990e60
from .text_content import TextContent as TextContent_a6810b4d

class BaseFrame(BaseFrameProperties_b990e60, TextContent_a6810b4d, XPropertySet_bc180bfa, XNamed_a6520b08, XShape_8fd00a3d):
    """
    Service Class

    specifies the base service of text frames, graphic objects, and embedded objects

    See Also:
        `API BaseFrame <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1BaseFrame.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.BaseFrame'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def FrameStyleName(self) -> str:
        """
        contains the name of the frame style that is applied to this object.
        """
        ...


__all__ = ['BaseFrame']

