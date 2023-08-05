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
import typing


class TimeInterval(object):
    """
    Struct Class

    Describes an interval on a date-axis.
    
    **since**
    
        OOo 3.4

    See Also:
        `API TimeInterval <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1TimeInterval.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.TimeInterval'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart.TimeInterval'
    """Literal Constant ``com.sun.star.chart.TimeInterval``"""

    def __init__(self, Number: typing.Optional[int] = 0, TimeUnit: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Number (int, optional): Number value.
            TimeUnit (int, optional): TimeUnit value.
        """
        super().__init__()

        if isinstance(Number, TimeInterval):
            oth: TimeInterval = Number
            self.Number = oth.Number
            self.TimeUnit = oth.TimeUnit
            return

        kargs = {
            "Number": Number,
            "TimeUnit": TimeUnit,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._number = kwargs["Number"]
        self._time_unit = kwargs["TimeUnit"]


    @property
    def Number(self) -> int:
        """
        specifies the number of units
        """
        return self._number

    @Number.setter
    def Number(self, value: int) -> None:
        self._number = value

    @property
    def TimeUnit(self) -> int:
        """
        specifies a unit for the interval
        
        is a value out of the constant group com.sun.star.chart.TimeUnit.
        """
        return self._time_unit

    @TimeUnit.setter
    def TimeUnit(self, value: int) -> None:
        self._time_unit = value


__all__ = ['TimeInterval']
