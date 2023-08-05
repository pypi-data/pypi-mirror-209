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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.sheet.DataPilotFieldOrientation import COLUMN as DATA_PILOT_FIELD_ORIENTATION_COLUMN
    from com.sun.star.sheet.DataPilotFieldOrientation import DATA as DATA_PILOT_FIELD_ORIENTATION_DATA
    from com.sun.star.sheet.DataPilotFieldOrientation import HIDDEN as DATA_PILOT_FIELD_ORIENTATION_HIDDEN
    from com.sun.star.sheet.DataPilotFieldOrientation import PAGE as DATA_PILOT_FIELD_ORIENTATION_PAGE
    from com.sun.star.sheet.DataPilotFieldOrientation import ROW as DATA_PILOT_FIELD_ORIENTATION_ROW

    class DataPilotFieldOrientation(uno.Enum):
        """
        Enum Class


        See Also:
            `API DataPilotFieldOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a686c797e7cb837947558aa11c946245a>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.sheet.DataPilotFieldOrientation', value)

        __ooo_ns__: str = 'com.sun.star.sheet'
        __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldOrientation'
        __ooo_type_name__: str = 'enum'

        COLUMN = cast("DataPilotFieldOrientation", DATA_PILOT_FIELD_ORIENTATION_COLUMN)
        """
        the field is used as a column field.
        
        is applied to the columns.
        """
        DATA = cast("DataPilotFieldOrientation", DATA_PILOT_FIELD_ORIENTATION_DATA)
        """
        the field is used as a data field.
        """
        HIDDEN = cast("DataPilotFieldOrientation", DATA_PILOT_FIELD_ORIENTATION_HIDDEN)
        """
        the field is not used in the table.
        """
        PAGE = cast("DataPilotFieldOrientation", DATA_PILOT_FIELD_ORIENTATION_PAGE)
        """
        the field is used as a page field.
        """
        ROW = cast("DataPilotFieldOrientation", DATA_PILOT_FIELD_ORIENTATION_ROW)
        """
        the field is used as a row field.
        
        is applied to the rows.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DataPilotFieldOrientation(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.DataPilotFieldOrientation", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.DataPilotFieldOrientation`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DataPilotFieldOrientation']
