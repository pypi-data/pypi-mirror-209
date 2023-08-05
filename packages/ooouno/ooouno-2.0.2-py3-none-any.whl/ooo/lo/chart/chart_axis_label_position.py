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
from enum import Enum


class ChartAxisLabelPosition(Enum):
    """
    Enum Class


    See Also:
        `API ChartAxisLabelPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a693b6b549818a6055effeaf72501bd26>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisLabelPosition'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart.ChartAxisLabelPosition'

    NEAR_AXIS = 'NEAR_AXIS'
    """
    The labels are placed adjacent to the axis.
    
    When the axis itself is placed at the minimum or maximum of the scale ( that is when the property CrossoverPosition equals ChartAxisPosition_MINIMUM or ChartAxisPosition_MAXIMUM) the labels are placed outside the coordinate system. Otherwise the labels are placed adjacent to the axis on that side that belongs to the lower values on the crossing axis. E.g. when the ChartAxisLabelPosition is set to NEAR_AXIS for an y axis the labels are placed adjacent to the y axis on that side that belongs to the lower x values.
    """
    NEAR_AXIS_OTHER_SIDE = 'NEAR_AXIS_OTHER_SIDE'
    """
    The labels are placed adjacent to the axis on the opposite side as for NEAR_AXIS.
    """
    OUTSIDE_END = 'OUTSIDE_END'
    """
    The labels are placed outside the coordinate region on that side where the crossing axis has its maximum value.
    
    E.g. when this is set for an y axis the labels are placed outside the diagram on that side where to the x axis has its maximum value.
    """
    OUTSIDE_START = 'OUTSIDE_START'
    """
    The labels are placed outside the coordinate region on that side where the crossing axis has its minimum value.
    
    E.g. when this is set for an y axis the labels are placed outside the diagram on that side where to the x axis has its minimum value.
    """

__all__ = ['ChartAxisLabelPosition']

