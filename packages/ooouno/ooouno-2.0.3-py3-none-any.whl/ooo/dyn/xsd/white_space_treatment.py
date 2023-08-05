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
# Namespace: com.sun.star.xsd
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class WhiteSpaceTreatment(metaclass=UnoConstMeta, type_name="com.sun.star.xsd.WhiteSpaceTreatment", name_space="com.sun.star.xsd"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.xsd.WhiteSpaceTreatment``"""
        pass

    class WhiteSpaceTreatmentEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.xsd.WhiteSpaceTreatment", name_space="com.sun.star.xsd"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.xsd.WhiteSpaceTreatment`` as Enum values"""
        pass

else:
    from com.sun.star.xsd import WhiteSpaceTreatment as WhiteSpaceTreatment

    class WhiteSpaceTreatmentEnum(IntEnum):
        """
        Enum of Const Class WhiteSpaceTreatment

        specifies possibilities how to treat whitespace in strings
        """
        Preserve = WhiteSpaceTreatment.Preserve
        """
        White spaces should be preserved when processing the string.
        """
        Replace = WhiteSpaceTreatment.Replace
        """
        White spaces should be replaced with TODO when processing the string.
        """
        Collapse = WhiteSpaceTreatment.Collapse
        """
        Multiple successive white spaces should be collapsed to a single white space when processing the string.
        """

__all__ = ['WhiteSpaceTreatment', 'WhiteSpaceTreatmentEnum']
