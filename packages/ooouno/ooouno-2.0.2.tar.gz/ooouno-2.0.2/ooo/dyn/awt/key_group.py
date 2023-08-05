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
# Namespace: com.sun.star.awt
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class KeyGroup(metaclass=UnoConstMeta, type_name="com.sun.star.awt.KeyGroup", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.KeyGroup``"""
        pass

    class KeyGroupEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.KeyGroup", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.KeyGroup`` as Enum values"""
        pass

else:
    from com.sun.star.awt import KeyGroup as KeyGroup

    class KeyGroupEnum(IntEnum):
        """
        Enum of Const Class KeyGroup

        These values are used to specify functional groups of keys.
        
        .. deprecated::
        
            Class is deprecated.
        """
        NUM = KeyGroup.NUM
        """
        specifies a numeric key.
        """
        ALPHA = KeyGroup.ALPHA
        """
        specifies an alphabetic key.
        """
        FKEYS = KeyGroup.FKEYS
        """
        specifies a function key.
        """
        CURSOR = KeyGroup.CURSOR
        """
        specifies a cursor key.
        """
        MISC = KeyGroup.MISC
        """
        specifies other keys.
        """
        TYPE = KeyGroup.TYPE
        """
        specifies the group mask.
        """

__all__ = ['KeyGroup', 'KeyGroupEnum']
