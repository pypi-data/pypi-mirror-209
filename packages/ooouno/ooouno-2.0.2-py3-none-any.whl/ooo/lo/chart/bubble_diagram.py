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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from .chart_axis_x_supplier import ChartAxisXSupplier as ChartAxisXSupplier_a950e4d
from .chart_statistics import ChartStatistics as ChartStatistics_e2190d37
from .chart_two_axis_y_supplier import ChartTwoAxisYSupplier as ChartTwoAxisYSupplier_380d0f88
from .diagram import Diagram as Diagram_844409cf

class BubbleDiagram(ChartAxisXSupplier_a950e4d, ChartStatistics_e2190d37, ChartTwoAxisYSupplier_380d0f88, Diagram_844409cf):
    """
    Service Class

    a service for bubble diagrams.
    
    **since**
    
        OOo 3.2

    See Also:
        `API BubbleDiagram <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1BubbleDiagram.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.BubbleDiagram'
    __ooo_type_name__: str = 'service'


__all__ = ['BubbleDiagram']

