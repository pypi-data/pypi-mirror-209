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
# Namespace: com.sun.star.gallery
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class GalleryItemType(metaclass=UnoConstMeta, type_name="com.sun.star.gallery.GalleryItemType", name_space="com.sun.star.gallery"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.gallery.GalleryItemType``"""
        pass

    class GalleryItemTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.gallery.GalleryItemType", name_space="com.sun.star.gallery"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.gallery.GalleryItemType`` as Enum values"""
        pass

else:
    from com.sun.star.gallery import GalleryItemType as GalleryItemType

    class GalleryItemTypeEnum(IntEnum):
        """
        Enum of Const Class GalleryItemType

        Constants that describe the type of graphic.
        """
        EMPTY = GalleryItemType.EMPTY
        """
        Item is empty.
        """
        GRAPHIC = GalleryItemType.GRAPHIC
        """
        Item represents a graphic.
        """
        MEDIA = GalleryItemType.MEDIA
        """
        Item represents a media file.
        """
        DRAWING = GalleryItemType.DRAWING
        """
        Item represents a drawing.
        """

__all__ = ['GalleryItemType', 'GalleryItemTypeEnum']
