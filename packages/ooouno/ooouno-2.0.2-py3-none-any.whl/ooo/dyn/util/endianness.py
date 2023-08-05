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
# Namespace: com.sun.star.util
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class Endianness(metaclass=UnoConstMeta, type_name="com.sun.star.util.Endianness", name_space="com.sun.star.util"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.util.Endianness``"""
        pass

    class EndiannessEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.util.Endianness", name_space="com.sun.star.util"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.util.Endianness`` as Enum values"""
        pass

else:
    from com.sun.star.util import Endianness as Endianness

    class EndiannessEnum(IntEnum):
        """
        Enum of Const Class Endianness

        These constants describe the endianness of data structures.
        
        The endianness specifies the order in which the bytes of larger types are laid out in memory.
        
        **since**
        
            OOo 2.0
        """
        LITTLE = Endianness.LITTLE
        """
        Little endian.
        
        The values are stored in little endian format, i.e. the bytes of the long word 0xAABBCCDD are laid out like 0xDD, 0xCC, 0xBB, 0xAA in memory. That is, data of arbitrary machine word lengths always starts with the least significant byte, and ends with the most significant one.
        """
        BIG = Endianness.BIG
        """
        Big endian.
        
        The values are stored in big endian format, i.e. the bytes of the long word 0xAABBCCDD are laid out like 0xAA, 0xBB, 0xCC, 0xDD in memory. That is, data of arbitrary machine word lengths always start with the most significant byte, and ends with the least significant one.
        """

__all__ = ['Endianness', 'EndiannessEnum']
