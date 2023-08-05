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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.chart.ChartAxisPosition import END as CHART_AXIS_POSITION_END
    from com.sun.star.chart.ChartAxisPosition import START as CHART_AXIS_POSITION_START
    from com.sun.star.chart.ChartAxisPosition import VALUE as CHART_AXIS_POSITION_VALUE
    from com.sun.star.chart.ChartAxisPosition import ZERO as CHART_AXIS_POSITION_ZERO

    class ChartAxisPosition(uno.Enum):
        """
        Enum Class


        See Also:
            `API ChartAxisPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#aa2815fba34da31acb139c7be75fda078>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.chart.ChartAxisPosition', value)

        __ooo_ns__: str = 'com.sun.star.chart'
        __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisPosition'
        __ooo_type_name__: str = 'enum'

        END = cast("ChartAxisPosition", CHART_AXIS_POSITION_END)
        """
        Cross the other axes at their maximum scale value.
        """
        START = cast("ChartAxisPosition", CHART_AXIS_POSITION_START)
        """
        Cross the other axes at their minimum scale value.
        """
        VALUE = cast("ChartAxisPosition", CHART_AXIS_POSITION_VALUE)
        """
        Cross the other axes at the value specified in the property CrossoverValue.
        """
        ZERO = cast("ChartAxisPosition", CHART_AXIS_POSITION_ZERO)
        """
        Cross the other axes at zero.
        
        If zero is not contained in the current scale the value is used which is nearest to zero.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ChartAxisPosition(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartAxisPosition", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartAxisPosition`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ChartAxisPosition']
