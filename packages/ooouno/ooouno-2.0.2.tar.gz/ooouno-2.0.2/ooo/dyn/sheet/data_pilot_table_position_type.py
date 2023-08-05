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

    class DataPilotTablePositionType(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.DataPilotTablePositionType", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.DataPilotTablePositionType``"""
        pass

    class DataPilotTablePositionTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.DataPilotTablePositionType", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.DataPilotTablePositionType`` as Enum values"""
        pass

else:
    from com.sun.star.sheet import DataPilotTablePositionType as DataPilotTablePositionType

    class DataPilotTablePositionTypeEnum(IntEnum):
        """
        Enum of Const Class DataPilotTablePositionType

        specifies in which sub-area a cell is positioned within a DataPilot table.
        
        **since**
        
            OOo 3.0
        """
        NOT_IN_TABLE = DataPilotTablePositionType.NOT_IN_TABLE
        """
        indicates that the specified cell is not in the DataPilot table.
        """
        RESULT = DataPilotTablePositionType.RESULT
        """
        indicates that the specified cell is within the result area.
        """
        ROW_HEADER = DataPilotTablePositionType.ROW_HEADER
        """
        indicates that the specified cell is within the row header area.
        """
        COLUMN_HEADER = DataPilotTablePositionType.COLUMN_HEADER
        """
        indicates that the specified cell is within the column header area.
        """
        OTHER = DataPilotTablePositionType.OTHER
        """
        indicates that the specified cell is within the table but in areas other than the result or header areas.
        """

__all__ = ['DataPilotTablePositionType', 'DataPilotTablePositionTypeEnum']
