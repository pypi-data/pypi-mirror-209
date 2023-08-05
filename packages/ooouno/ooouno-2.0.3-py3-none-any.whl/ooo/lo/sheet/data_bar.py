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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from .x_condition_entry import XConditionEntry as XConditionEntry_e2340d32
if typing.TYPE_CHECKING:
    from .x_data_bar_entry import XDataBarEntry as XDataBarEntry_c61d0c1a
    from ..util.color import Color as Color_68e908c5

class DataBar(XConditionEntry_e2340d32):
    """
    Service Class


    See Also:
        `API DataBar <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataBar.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataBar'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DataBarEntries(self) -> 'typing.Tuple[XDataBarEntry_c61d0c1a, ...]':
        """
        """
        ...

    @abstractproperty
    def AxisColor(self) -> 'Color_68e908c5':
        """
        """
        ...

    @abstractproperty
    def AxisPosition(self) -> int:
        """
        See com.sun.star.sheet.DataBarAxis for possible values.
        """
        ...

    @abstractproperty
    def Color(self) -> 'Color_68e908c5':
        """
        """
        ...

    @abstractproperty
    def MaximumLength(self) -> float:
        """
        Maximum databar length in percent of cell width.
        
        Allowed values are (0, 1000) but larger than MinimumLength.
        """
        ...

    @abstractproperty
    def MinimumLength(self) -> float:
        """
        Minimum databar length in percent of cell width.
        
        Allowed values are [0, 100) but smaller than MaximumLength.
        """
        ...

    @abstractproperty
    def NegativeColor(self) -> 'Color_68e908c5':
        """
        """
        ...

    @abstractproperty
    def ShowValue(self) -> bool:
        """
        """
        ...

    @abstractproperty
    def UseGradient(self) -> bool:
        """
        """
        ...

    @abstractproperty
    def UseNegativeColor(self) -> bool:
        """
        """
        ...


__all__ = ['DataBar']

