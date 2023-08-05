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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet


class FilterOperator2(object):
    """
    Const Class

    specifies the type of a single condition in a filter descriptor.
    
    This constants group extends the FilterOperator enum by additional filter operators.
    
    **since**
    
        OOo 3.2

    See Also:
        `API FilterOperator2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FilterOperator2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FilterOperator2'
    __ooo_type_name__: str = 'const'

    EMPTY = 0
    """
    selects empty entries.
    """
    NOT_EMPTY = 1
    """
    selects non-empty entries.
    """
    EQUAL = 2
    """
    value has to be equal to the specified value.
    """
    NOT_EQUAL = 3
    """
    value must not be equal to the specified value.
    """
    GREATER = 4
    """
    value has to be greater than the specified value.
    """
    GREATER_EQUAL = 5
    """
    value has to be greater than or equal to the specified value.
    """
    LESS = 6
    """
    value has to be less than the specified value.
    """
    LESS_EQUAL = 7
    """
    value has to be less than or equal to the specified value.
    """
    TOP_VALUES = 8
    """
    selects a specified number of entries with the greatest values.
    """
    TOP_PERCENT = 9
    """
    selects a specified percentage of entries with the greatest values.
    """
    BOTTOM_VALUES = 10
    """
    selects a specified number of entries with the lowest values.
    """
    BOTTOM_PERCENT = 11
    """
    selects a specified percentage of entries with the lowest values.
    """
    CONTAINS = 12
    """
    selects contains entries.
    """
    DOES_NOT_CONTAIN = 13
    """
    selects does-not-contain entries.
    """
    BEGINS_WITH = 14
    """
    selects begins-with entries.
    """
    DOES_NOT_BEGIN_WITH = 15
    """
    selects does-not-begin-with entries.
    """
    ENDS_WITH = 16
    """
    selects ends-with entries.
    """
    DOES_NOT_END_WITH = 17
    """
    selects does-not-end-with entries.
    """

__all__ = ['FilterOperator2']
