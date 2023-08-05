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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XLabelRange(XInterface_8f010a43):
    """
    provides access to the settings of a label range in a spreadsheet document.
    
    These can be column or row labels, depending on where they are used.

    See Also:
        `API XLabelRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XLabelRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XLabelRange'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XLabelRange'

    @abstractmethod
    def getDataArea(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the cell range address for which the labels are valid.
        """
        ...
    @abstractmethod
    def getLabelArea(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the cell range address that contains the labels.
        """
        ...
    @abstractmethod
    def setDataArea(self, aDataArea: 'CellRangeAddress_ec450d43') -> None:
        """
        sets the cell range address for which the labels are valid.
        """
        ...
    @abstractmethod
    def setLabelArea(self, aLabelArea: 'CellRangeAddress_ec450d43') -> None:
        """
        sets the cell range address that contains the labels.
        """
        ...

__all__ = ['XLabelRange']

