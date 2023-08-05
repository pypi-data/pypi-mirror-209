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
# Namespace: com.sun.star.sdbc
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ColumnValue(metaclass=UnoConstMeta, type_name="com.sun.star.sdbc.ColumnValue", name_space="com.sun.star.sdbc"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbc.ColumnValue``"""
        pass

    class ColumnValueEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbc.ColumnValue", name_space="com.sun.star.sdbc"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbc.ColumnValue`` as Enum values"""
        pass

else:
    from com.sun.star.sdbc import ColumnValue as ColumnValue

    class ColumnValueEnum(IntEnum):
        """
        Enum of Const Class ColumnValue

        determines whether a column allows SQL NULL values or not.
        """
        NO_NULLS = ColumnValue.NO_NULLS
        """
        indicates that a column does not allow NULL values.
        """
        NULLABLE = ColumnValue.NULLABLE
        """
        indicates that a column does allow NULL values.
        """
        NULLABLE_UNKNOWN = ColumnValue.NULLABLE_UNKNOWN
        """
        indicates that the nullability of the column is unknown.
        """

__all__ = ['ColumnValue', 'ColumnValueEnum']
