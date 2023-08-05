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
# Namespace: com.sun.star.table
import typing
from abc import abstractproperty
from ..form.binding.list_entry_source import ListEntrySource as ListEntrySource_48260fe4
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
if typing.TYPE_CHECKING:
    from .cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class CellRangeListSource(ListEntrySource_48260fe4, XInitialization_d46c0cca):
    """
    Service Class

    defines the a source of list entries coming from a cell range in a table document
    
    The component cannot be instantiated at a global service factory, instead it's usually provided by a document instance.

    See Also:
        `API CellRangeListSource <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1CellRangeListSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.CellRangeListSource'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CellRange(self) -> 'CellRangeAddress_ec450d43':
        """
        specifies the cell range within a document to which the component is bound.
        """
        ...


__all__ = ['CellRangeListSource']

