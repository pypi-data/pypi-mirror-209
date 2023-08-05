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

    from com.sun.star.sheet.FillMode import AUTO as FILL_MODE_AUTO
    from com.sun.star.sheet.FillMode import DATE as FILL_MODE_DATE
    from com.sun.star.sheet.FillMode import GROWTH as FILL_MODE_GROWTH
    from com.sun.star.sheet.FillMode import LINEAR as FILL_MODE_LINEAR
    from com.sun.star.sheet.FillMode import SIMPLE as FILL_MODE_SIMPLE

    class FillMode(uno.Enum):
        """
        Enum Class


        See Also:
            `API FillMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a75a9acd74effffae38daed55136b0980>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.sheet.FillMode', value)

        __ooo_ns__: str = 'com.sun.star.sheet'
        __ooo_full_ns__: str = 'com.sun.star.sheet.FillMode'
        __ooo_type_name__: str = 'enum'

        AUTO = cast("FillMode", FILL_MODE_AUTO)
        """
        specifies the use of a user-defined list.
        
        function is determined automatically.
        """
        DATE = cast("FillMode", FILL_MODE_DATE)
        """
        specifies an arithmetic series for date values.
        
        any date value matching the specified condition is valid.
        """
        GROWTH = cast("FillMode", FILL_MODE_GROWTH)
        """
        specifies a geometric series.
        """
        LINEAR = cast("FillMode", FILL_MODE_LINEAR)
        """
        specifies an arithmetic series.
        """
        SIMPLE = cast("FillMode", FILL_MODE_SIMPLE)
        """
        specifies a constant series.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FillMode(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FillMode", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.FillMode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FillMode']
