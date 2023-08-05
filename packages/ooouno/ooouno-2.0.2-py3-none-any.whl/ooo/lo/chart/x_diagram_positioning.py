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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9

class XDiagramPositioning(XInterface_8f010a43):
    """
    allow for different positioning options for a diagram

    See Also:
        `API XDiagramPositioning <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XDiagramPositioning.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.XDiagramPositioning'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart.XDiagramPositioning'

    @abstractmethod
    def calculateDiagramPositionExcludingAxes(self) -> 'Rectangle_84b109e9':
        """
        """
        ...
    @abstractmethod
    def calculateDiagramPositionIncludingAxes(self) -> 'Rectangle_84b109e9':
        """
        """
        ...
    @abstractmethod
    def calculateDiagramPositionIncludingAxesAndAxisTitles(self) -> 'Rectangle_84b109e9':
        """
        """
        ...
    @abstractmethod
    def isAutomaticDiagramPositioning(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def isExcludingDiagramPositioning(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def setAutomaticDiagramPositioning(self) -> None:
        """
        the diagram will be placed automatically
        """
        ...
    @abstractmethod
    def setDiagramPositionExcludingAxes(self, PositionRect: 'Rectangle_84b109e9') -> None:
        """
        place the inner diagram part excluding any axes, labels and titles
        """
        ...
    @abstractmethod
    def setDiagramPositionIncludingAxes(self, PositionRect: 'Rectangle_84b109e9') -> None:
        """
        place the outer diagram part including the axes and axes labels, but excluding the axes titles.
        """
        ...
    @abstractmethod
    def setDiagramPositionIncludingAxesAndAxisTitles(self, PositionRect: 'Rectangle_84b109e9') -> None:
        """
        place the diagram including the axes, axes labels and axes titles.
        
        For the placement the current axis titles are taken into account, so the titles must be initialized properly before this method is called.
        """
        ...

__all__ = ['XDiagramPositioning']

