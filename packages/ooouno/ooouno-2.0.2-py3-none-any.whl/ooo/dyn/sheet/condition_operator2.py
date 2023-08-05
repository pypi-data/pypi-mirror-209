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
# Namespace: com.sun.star.sheet
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ConditionOperator2(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.ConditionOperator2", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.ConditionOperator2``"""
        pass

    class ConditionOperator2Enum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.ConditionOperator2", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.ConditionOperator2`` as Enum values"""
        pass

else:
    from com.sun.star.sheet import ConditionOperator2 as ConditionOperator2

    class ConditionOperator2Enum(IntEnum):
        """
        Enum of Const Class ConditionOperator2

        is used to specify the type of XSheetCondition2.
        """
        NONE = ConditionOperator2.NONE
        """
        no condition is specified.
        """
        EQUAL = ConditionOperator2.EQUAL
        """
        value has to be equal to the specified value.
        """
        NOT_EQUAL = ConditionOperator2.NOT_EQUAL
        """
        the value must not be equal to the specified value.
        """
        GREATER = ConditionOperator2.GREATER
        """
        the value has to be greater than the specified value.
        """
        GREATER_EQUAL = ConditionOperator2.GREATER_EQUAL
        """
        the value has to be greater than or equal to the specified value.
        """
        LESS = ConditionOperator2.LESS
        """
        the value has to be less than the specified value.
        """
        LESS_EQUAL = ConditionOperator2.LESS_EQUAL
        """
        the value has to be less than or equal to the specified value.
        """
        BETWEEN = ConditionOperator2.BETWEEN
        """
        the value has to be between the two specified values.
        """
        NOT_BETWEEN = ConditionOperator2.NOT_BETWEEN
        """
        the value has to be outside of the two specified values.
        """
        FORMULA = ConditionOperator2.FORMULA
        """
        the specified formula has to give a non-zero result.
        """
        DUPLICATE = ConditionOperator2.DUPLICATE
        """
        Conditionally format duplicate values.
        """
        NOT_DUPLICATE = ConditionOperator2.NOT_DUPLICATE
        """
        Conditionally format non-duplicate values.
        """

__all__ = ['ConditionOperator2', 'ConditionOperator2Enum']
