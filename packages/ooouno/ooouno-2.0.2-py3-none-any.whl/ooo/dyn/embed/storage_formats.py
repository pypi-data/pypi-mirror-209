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
# Namespace: com.sun.star.embed
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class StorageFormats(metaclass=UnoConstMeta, type_name="com.sun.star.embed.StorageFormats", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.StorageFormats``"""
        pass

    class StorageFormatsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.StorageFormats", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.StorageFormats`` as Enum values"""
        pass

else:
    from com.sun.star.embed import StorageFormats as StorageFormats

    class StorageFormatsEnum(IntEnum):
        """
        Enum of Const Class StorageFormats

        The constant set contains IDs of formats that are supported by StorageFactory.
        
        **since**
        
            OOo 3.3
        """
        PACKAGE = StorageFormats.PACKAGE
        """
        specifies package format
        """
        ZIP = StorageFormats.ZIP
        """
        specifies zip format
        """
        OFOPXML = StorageFormats.OFOPXML
        """
        specifies Office Open XML format
        """

__all__ = ['StorageFormats', 'StorageFormatsEnum']
