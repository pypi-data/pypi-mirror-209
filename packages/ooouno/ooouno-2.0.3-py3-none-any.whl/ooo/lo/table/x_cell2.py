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
# Namespace: com.sun.star.table
from abc import abstractmethod
from .x_cell import XCell as XCell_70d408e8

class XCell2(XCell_70d408e8):
    """
    extends XCell methods to access the contents of a cell in a table.

    See Also:
        `API XCell2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XCell2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.XCell2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.table.XCell2'

    @abstractmethod
    def setFormulaResult(self, nValue: float) -> None:
        """
        sets a formula result into the cell.
        
        When assigned, the formula cell's result will be set to this value and will not be calculated - unless a HardRecalc is executed.
        """
        ...
    @abstractmethod
    def setFormulaString(self, aFormula: str) -> None:
        """
        sets a formula string into the cell.
        
        When assigned, the formula is set into the string. But is not compiled, tokenized or calculated. Its useful when loading a document and setFormulaResult() is used. Otherwise it is compiled on trying to fetch a result value.
        """
        ...

__all__ = ['XCell2']

