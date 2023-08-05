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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .chart_data_change_type import ChartDataChangeType as ChartDataChangeType_16cc0e6e


class ChartDataChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes a change that was applied to the data.

    See Also:
        `API ChartDataChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart.ChartDataChangeEvent'
    """Literal Constant ``com.sun.star.chart.ChartDataChangeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Type: typing.Optional[ChartDataChangeType_16cc0e6e] = ChartDataChangeType_16cc0e6e.ALL, StartColumn: typing.Optional[int] = 0, EndColumn: typing.Optional[int] = 0, StartRow: typing.Optional[int] = 0, EndRow: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Type (ChartDataChangeType, optional): Type value.
            StartColumn (int, optional): StartColumn value.
            EndColumn (int, optional): EndColumn value.
            StartRow (int, optional): StartRow value.
            EndRow (int, optional): EndRow value.
        """

        if isinstance(Source, ChartDataChangeEvent):
            oth: ChartDataChangeEvent = Source
            self.Source = oth.Source
            self.Type = oth.Type
            self.StartColumn = oth.StartColumn
            self.EndColumn = oth.EndColumn
            self.StartRow = oth.StartRow
            self.EndRow = oth.EndRow
            return

        kargs = {
            "Source": Source,
            "Type": Type,
            "StartColumn": StartColumn,
            "EndColumn": EndColumn,
            "StartRow": StartRow,
            "EndRow": EndRow,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._start_column = kwargs["StartColumn"]
        self._end_column = kwargs["EndColumn"]
        self._start_row = kwargs["StartRow"]
        self._end_row = kwargs["EndRow"]
        inst_keys = ('Type', 'StartColumn', 'EndColumn', 'StartRow', 'EndRow')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Type(self) -> ChartDataChangeType_16cc0e6e:
        """
        specifies the type of change to the data.
        """
        return self._type

    @Type.setter
    def Type(self, value: ChartDataChangeType_16cc0e6e) -> None:
        self._type = value

    @property
    def StartColumn(self) -> int:
        """
        specifies the column number in which the changes begin.
        """
        return self._start_column

    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def EndColumn(self) -> int:
        """
        specifies the column number in which the changes end.
        """
        return self._end_column

    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def StartRow(self) -> int:
        """
        specifies the row number in which the changes begin.
        """
        return self._start_row

    @StartRow.setter
    def StartRow(self, value: int) -> None:
        self._start_row = value

    @property
    def EndRow(self) -> int:
        """
        specifies the row number in which the changes end.
        """
        return self._end_row

    @EndRow.setter
    def EndRow(self, value: int) -> None:
        self._end_row = value


__all__ = ['ChartDataChangeEvent']
