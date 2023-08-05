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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .cell_content_type import CellContentType as CellContentType_e08c0d0d

class XCell(XInterface_8f010a43):
    """
    provides methods to access the contents of a cell in a table.

    See Also:
        `API XCell <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XCell.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.XCell'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.table.XCell'

    @abstractmethod
    def getError(self) -> int:
        """
        returns the error value of the cell.
        
        If the cell does not contain a formula, the error is always zero.
        """
        ...
    @abstractmethod
    def getFormula(self) -> str:
        """
        returns the formula string of a cell.
        
        Even if the cell does not contain a formula, an assignment of this attribute's value to another cell's formula attribute would create the same cell content. This is because this attribute contains the original text value of a string cell. The value of a value cell will be formatted using the number format's default format or the formula string, including \"=\", of a formula cell.
        """
        ...
    @abstractmethod
    def getType(self) -> 'CellContentType_e08c0d0d':
        """
        returns the type of the cell.
        """
        ...
    @abstractmethod
    def getValue(self) -> float:
        """
        returns the floating point value of the cell.
        
        For a value cell the value is returned, for a string cell zero is returned and for a formula cell the result value of a formula is returned.
        """
        ...
    @abstractmethod
    def setFormula(self, aFormula: str) -> None:
        """
        sets a formula into the cell.
        
        When assigned, the string will be interpreted and a value, text or formula cell is created, depending on the text and the number format.
        """
        ...
    @abstractmethod
    def setValue(self, nValue: float) -> None:
        """
        sets a floating point value into the cell.
        
        After a call to this method the type of the cell is CellContentType.VALUE.
        """
        ...

__all__ = ['XCell']

