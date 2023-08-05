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
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XUniqueCellFormatRangesSupplier(XInterface_8f010a43):
    """
    provides access to a collection of collections of equal-formatted cell ranges.

    See Also:
        `API XUniqueCellFormatRangesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XUniqueCellFormatRangesSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XUniqueCellFormatRangesSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XUniqueCellFormatRangesSupplier'

    @abstractmethod
    def getUniqueCellFormatRanges(self) -> 'XIndexAccess_f0910d6d':
        """
        returns a collection of equal-formatted cell range collections.
        
        Each cell of the original range is contained in one of the ranges (even unformatted cells). If there is a non-rectangular equal-formatted cell area, it will be split into several rectangular ranges.
        
        All equal-formatted ranges are consolidated into one collection. These collections are the members contained in a UniqueCellFormatRanges collection.
        """
        ...

__all__ = ['XUniqueCellFormatRangesSupplier']

