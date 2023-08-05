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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from enum import Enum


class ChartDataChangeType(Enum):
    """
    Enum Class


    See Also:
        `API ChartDataChangeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a37b4d47e7d1600aa406ad115a39fe1da>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataChangeType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart.ChartDataChangeType'

    ALL = 'ALL'
    """
    Major changes were applied to the data.
    """
    COLUMN_DELETED = 'COLUMN_DELETED'
    """
    The column given in the ChartDataChangeEvent, was deleted.
    """
    COLUMN_INSERTED = 'COLUMN_INSERTED'
    """
    The column given in the ChartDataChangeEvent, was inserted.
    """
    DATA_RANGE = 'DATA_RANGE'
    """
    The range of columns and rows, given in the ChartDataChangeEvent, has changed.
    """
    ROW_DELETED = 'ROW_DELETED'
    """
    The row given in the ChartDataChangeEvent, was deleted.
    """
    ROW_INSERTED = 'ROW_INSERTED'
    """
    The row given in the ChartDataChangeEvent, was inserted.
    """

__all__ = ['ChartDataChangeType']

