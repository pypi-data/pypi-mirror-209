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


class DataPilotFieldReferenceType(object):
    """
    Const Class

    These constants select different types of References to calculate the data fields.

    See Also:
        `API DataPilotFieldReferenceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldReferenceType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldReferenceType'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    This type means, that the results in the data fields are displayed like they are.
    """
    ITEM_DIFFERENCE = 1
    """
    From each result, its reference value (see below) is subtracted, and the difference is shown.
    
    Totals outside of the base field are shown as empty results.
    
    Named Item
    
    If a base item name is specified, the reference value for a combination of field items is the result where the item in the base field is replaced by the specified base item.
    
    If the reference value isn't shown in the DataPilot table because of hidden details for a parent field, the difference isn't calculated and an error value is shown.
    
    If the result for an item combination is empty, the value 0 is used for the difference, even if the summary function is undefined without values, like average or variance. The difference is shown in the result table even if the original result was empty.
    
    The difference for item combinations containing the base item is shown as empty result.
    
    Previous or Next
    
    If \"previous\" or \"next\" is specified as the base item, the reference value is the result for the next visible member of the base field, in the base field's sort order. If details for one item in the base field are hidden, that item is skipped. The difference for the item with hidden details isn't calculated, not even for the item's summary, to have a consistent order of previous and next items.
    
    Empty results are handled as for named items (see above).
    
    The difference for the first (for com.sun.star.sheet.DataPilotFieldReferenceItemType.PREVIOUS) or last (for com.sun.star.sheet.DataPilotFieldReferenceItemType.NEXT ) item of the base field is shown as empty result.
    """
    ITEM_PERCENTAGE = 2
    """
    Each result is divided by its reference value.
    
    The reference value is determined in the same way as for com.sun.star.sheet.DataPilotFieldReferenceType.ITEM_DIFFERENCE. Totals outside of the base field are shown as empty results.
    
    Division by zero results in an error. Otherwise, empty results are shown as 0. Results for the base item, first (for com.sun.star.sheet.DataPilotFieldReferenceItemType.PREVIOUS) or last (for com.sun.star.sheet.DataPilotFieldReferenceItemType.NEXT) item of the base field are shown as 1 if not empty.
    """
    ITEM_PERCENTAGE_DIFFERENCE = 3
    """
    From each result, its reference value is subtracted, and the difference divided by the reference value.
    
    The reference value is determined in the same way as for com.sun.star.sheet.DataPilotFieldReferenceType.ITEM_DIFFERENCE. Totals outside of the base field are shown as empty results.
    
    Division by zero results in an error. Otherwise, the rules for com.sun.star.sheet.DataPilotFieldReferenceType.ITEM_DIFFERENCE apply.
    """
    RUNNING_TOTAL = 4
    """
    Each result is added to the sum of the results for preceding items in the base field, in the base field's sort order, and the total sum is shown.
    
    If details for one item in the base field are hidden, that item isn't included in calculating the sum, and results for that item are shown as error, to ensure consistency between details and subtotals for the following items.
    
    Results are always summed, even if a different summary function was used to get each result.
    
    Totals outside of the base field are shown as empty results.
    """
    ROW_PERCENTAGE = 5
    """
    Each result is divided by the total result for its row in the DataPilot table.
    
    If there are several data fields, the total for the result's data field is used.
    
    If there are subtotals with manually selected summary functions, still the total with the data field's summary function is used.
    
    Division by zero results in an error.
    
    Otherwise, empty results remain empty.
    """
    COLUMN_PERCENTAGE = 6
    """
    Same as com.sun.star.sheet.DataPilotFieldReferenceType.ROW_PERCENTAGE, but the total for the result's column is used.
    """
    TOTAL_PERCENTAGE = 7
    """
    Same as com.sun.star.sheet.DataPilotFieldReferenceType.ROW_PERCENTAGE, but the grand total for the result's data field is used.
    """
    INDEX = 8
    """
    The row and column totals and the grand total, following the same rules as above, are used to calculate the following expression.
    
    ( original result * grand total ) / ( row total * column total )
    
    Division by zero results in an error. Otherwise, empty results remain empty.
    """

__all__ = ['DataPilotFieldReferenceType']
