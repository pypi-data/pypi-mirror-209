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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
import typing
from abc import abstractmethod
from ..frame.x_model import XModel as XModel_7a6e095c
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_chart_data import XChartData as XChartData_a3580ade
    from .x_diagram import XDiagram as XDiagram_8e1e0a27
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XChartDocument(XModel_7a6e095c):
    """
    manages the chart document.

    See Also:
        `API XChartDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XChartDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.XChartDocument'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart.XChartDocument'

    @abstractmethod
    def attachData(self, xData: 'XChartData_a3580ade') -> None:
        """
        attaches data to the chart.
        
        The given object needs to support interface XChartDataArray.
        
        Since OOo 3.3 if the given object might support interface XComplexDescriptionAccess which allows to set complex hierarchical axis descriptions.
        
        Since OOo 3.4 if the given object might support interface XDateCategories which allows to set date values as x values for category charts.
        
        The given data is copied before it is applied to the chart. So changing xData after this call will have no effect on the chart.
        """
        ...
    @abstractmethod
    def getArea(self) -> 'XPropertySet_bc180bfa':
        """
        The area's extent is equal to the document size. If you want to access properties of the background area of the diagram, in which the actual data is represented, you have to change the chart wall which you get from the X3DDisplay.
        """
        ...
    @abstractmethod
    def getData(self) -> 'XChartData_a3580ade':
        """
        The returned object supports interface XChartDataArray which can be used to access the concrete data.
        
        Since OOo 3.3 the returned object also supports interface XComplexDescriptionAccess which can be used to access complex hierarchical axis descriptions.
        
        Since OOo 3.4 the returned object also supports interface XDateCategories.
        """
        ...
    @abstractmethod
    def getDiagram(self) -> 'XDiagram_8e1e0a27':
        """
        """
        ...
    @abstractmethod
    def getLegend(self) -> 'XShape_8fd00a3d':
        """
        """
        ...
    @abstractmethod
    def getSubTitle(self) -> 'XShape_8fd00a3d':
        """
        Usually the subtitle is smaller than the main title by default. And it is most commonly placed below the main title by default.
        """
        ...
    @abstractmethod
    def getTitle(self) -> 'XShape_8fd00a3d':
        """
        """
        ...
    @abstractmethod
    def setDiagram(self, xDiagram: 'XDiagram_8e1e0a27') -> None:
        """
        sets the diagram for the chart document.
        
        Setting a new diagram implicitly disposes the previous diagram.
        """
        ...

__all__ = ['XChartDocument']

