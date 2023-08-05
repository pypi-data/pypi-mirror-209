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
# Namespace: com.sun.star.accessibility
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_accessible import XAccessible as XAccessible_1cbc0eb6

class XAccessibleTable(XInterface_8f010a43):
    """
    Implement this interface to give access to a two-dimensional table.
    
    The XAccessibleTable interface is used to represent two-dimensional tables. This interface combines the two interfaces javax.accessibility.AccessibleTable and javax.accessibility.AccessibleExtendedTable of the Java Accessibility API (version 1.4).
    
    All XAccessible objects that represent cells or cell-clusters of a table have to be at the same time children of the table. This is necessary to be able to convert row and column indices into child indices and vice versa with the methods XAccessibleTable.getAccessibleIndex(), XAccessibleTable.getAccessibleRow(), and XAccessibleTable.getAccessibleColumn().
    
    The range of valid coordinates for this interface are implementation dependent. However, that range includes at least the intervals from the from the first row or column with the index 0 up to the last (but not including) used row or column as returned by XAccessibleTable.getAccessibleRowCount() and XAccessibleTable.getAccessibleColumnCount(). In case of the Calc the current range of valid indices for retrieving data include the maximal table size–256 columns and 32000 rows–minus one.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleTable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleTable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleTable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleTable'

    @abstractmethod
    def getAccessibleCaption(self) -> 'XAccessible_1cbc0eb6':
        """
        Returns the caption for the table.
        """
        ...
    @abstractmethod
    def getAccessibleCellAt(self, nRow: int, nColumn: int) -> 'XAccessible_1cbc0eb6':
        """
        Returns the XAccessible object at the specified row and column in the table.
        
        This method has been renamed from the Java name getAccessibleAt to XAccessibleTable.getAccessibleCellAt() to avoid ambiguities with the XAccessibleComponent.getAccessibleAt() method when accessed, for instance, from StarBasic.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleColumn(self, nChildIndex: int) -> int:
        """
        Translate the given child index into the corresponding column index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleColumnCount(self) -> int:
        """
        Returns the number of used columns in the table.
        
        The implementation, however, may allow the access of columns beyond this number.
        """
        ...
    @abstractmethod
    def getAccessibleColumnDescription(self, nColumn: int) -> str:
        """
        Returns the description text of the specified column in the table.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleColumnExtentAt(self, nRow: int, nColumn: int) -> int:
        """
        Returns the number of columns occupied by the Accessible at the specified row and column in the table.
        
        The result differs from 1 if the specified cell spans multiple columns.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleColumnHeaders(self) -> 'XAccessibleTable':
        """
        Returns the column headers as an XAccessibleTable object.
        
        Content and size of the returned table are implementation dependent.
        """
        ...
    @abstractmethod
    def getAccessibleIndex(self, nRow: int, nColumn: int) -> int:
        """
        Returns the child index of the accessible object that spans the specified cell.
        
        This is the same index that would be returned by calling XAccessibleContext.getAccessibleIndexInParent() for that accessible object.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleRow(self, nChildIndex: int) -> int:
        """
        Translate the given child index into the corresponding row index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleRowCount(self) -> int:
        """
        Returns the number of used rows in the table.
        
        The implementation, however, may allow the access of columns beyond this number.
        """
        ...
    @abstractmethod
    def getAccessibleRowDescription(self, nRow: int) -> str:
        """
        Returns the description text of the specified row in the table.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleRowExtentAt(self, nRow: int, nColumn: int) -> int:
        """
        Returns the number of rows occupied by the Accessible at the specified row and column in the table.
        
        The result differs from 1 if the specified cell spans multiple rows.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getAccessibleRowHeaders(self) -> 'XAccessibleTable':
        """
        Returns the row headers as an XAccessibleTable object.
        
        Content and size of the returned table are implementation dependent.
        """
        ...
    @abstractmethod
    def getAccessibleSummary(self) -> 'XAccessible_1cbc0eb6':
        """
        Returns the summary description of the table.
        """
        ...
    @abstractmethod
    def getSelectedAccessibleColumns(self) -> uno.ByteSequence:
        """
        Returns a list of the indices of completely selected columns in a table.
        """
        ...
    @abstractmethod
    def getSelectedAccessibleRows(self) -> uno.ByteSequence:
        """
        Returns a list of the indices of completely selected rows in a table.
        """
        ...
    @abstractmethod
    def isAccessibleColumnSelected(self, nColumn: int) -> bool:
        """
        Returns a boolean value indicating whether the specified column is completely selected.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def isAccessibleRowSelected(self, nRow: int) -> bool:
        """
        Returns a boolean value indicating whether the specified row is completely selected.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def isAccessibleSelected(self, nRow: int, nColumn: int) -> bool:
        """
        Returns a boolean value indicating whether the accessible at the specified row and column is selected.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...

__all__ = ['XAccessibleTable']

