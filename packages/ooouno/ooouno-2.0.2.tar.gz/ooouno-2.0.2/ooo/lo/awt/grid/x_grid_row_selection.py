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
# Namespace: com.sun.star.awt.grid
import typing
import uno
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_grid_selection_listener import XGridSelectionListener as XGridSelectionListener_759e10f2

class XGridRowSelection(ABC):
    """
    This interfaces provides access to the selection of row for UnoControlGrid.
    
    **since**
    
        LibreOffice 3.4

    See Also:
        `API XGridRowSelection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridRowSelection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XGridRowSelection'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridRowSelection'

    @abstractmethod
    def addSelectionListener(self, listener: 'XGridSelectionListener_759e10f2') -> None:
        """
        Adds a listener for the GridSelectionEvent posted after the grid changes.
        """
        ...
    @abstractmethod
    def deselectAllRows(self) -> None:
        """
        Deselects all selected rows.
        """
        ...
    @abstractmethod
    def deselectRow(self, RowIndex: int) -> None:
        """
        removes the selection for a given row

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getSelectedRows(self) -> uno.ByteSequence:
        """
        Returns the indices of all selected rows.
        """
        ...
    @abstractmethod
    def hasSelectedRows(self) -> bool:
        """
        Returns whether rows are selected.
        """
        ...
    @abstractmethod
    def isRowSelected(self, RowIndex: int) -> bool:
        """
        Returns whether a specific row is selected.
        """
        ...
    @abstractmethod
    def removeSelectionListener(self, listener: 'XGridSelectionListener_759e10f2') -> None:
        """
        Removes a listener previously added with addSelectionListener().
        """
        ...
    @abstractmethod
    def selectAllRows(self) -> None:
        """
        Selects all rows.
        """
        ...
    @abstractmethod
    def selectRow(self, RowIndex: int) -> None:
        """
        selects a given row

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...

__all__ = ['XGridRowSelection']

