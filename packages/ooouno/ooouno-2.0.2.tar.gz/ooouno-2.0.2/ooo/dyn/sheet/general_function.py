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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.sheet.GeneralFunction import AUTO as GENERAL_FUNCTION_AUTO
    from com.sun.star.sheet.GeneralFunction import AVERAGE as GENERAL_FUNCTION_AVERAGE
    from com.sun.star.sheet.GeneralFunction import COUNT as GENERAL_FUNCTION_COUNT
    from com.sun.star.sheet.GeneralFunction import COUNTNUMS as GENERAL_FUNCTION_COUNTNUMS
    from com.sun.star.sheet.GeneralFunction import MAX as GENERAL_FUNCTION_MAX
    from com.sun.star.sheet.GeneralFunction import MIN as GENERAL_FUNCTION_MIN
    from com.sun.star.sheet.GeneralFunction import NONE as GENERAL_FUNCTION_NONE
    from com.sun.star.sheet.GeneralFunction import PRODUCT as GENERAL_FUNCTION_PRODUCT
    from com.sun.star.sheet.GeneralFunction import STDEV as GENERAL_FUNCTION_STDEV
    from com.sun.star.sheet.GeneralFunction import STDEVP as GENERAL_FUNCTION_STDEVP
    from com.sun.star.sheet.GeneralFunction import SUM as GENERAL_FUNCTION_SUM
    from com.sun.star.sheet.GeneralFunction import VAR as GENERAL_FUNCTION_VAR
    from com.sun.star.sheet.GeneralFunction import VARP as GENERAL_FUNCTION_VARP

    class GeneralFunction(uno.Enum):
        """
        Enum Class


        See Also:
            `API GeneralFunction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#ad184d5bd9055f3b4fd57ce72c781758d>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.sheet.GeneralFunction', value)

        __ooo_ns__: str = 'com.sun.star.sheet'
        __ooo_full_ns__: str = 'com.sun.star.sheet.GeneralFunction'
        __ooo_type_name__: str = 'enum'

        AUTO: GeneralFunction = GENERAL_FUNCTION_AUTO
        """
        specifies the use of a user-defined list.
        
        function is determined automatically.
        """
        AVERAGE: GeneralFunction = GENERAL_FUNCTION_AVERAGE
        """
        average of all numerical values is calculated.
        """
        COUNT: GeneralFunction = GENERAL_FUNCTION_COUNT
        """
        all values, including non-numerical values, are counted.
        """
        COUNTNUMS: GeneralFunction = GENERAL_FUNCTION_COUNTNUMS
        """
        numerical values are counted.
        """
        MAX: GeneralFunction = GENERAL_FUNCTION_MAX
        """
        maximum value of all numerical values is calculated.
        """
        MIN: GeneralFunction = GENERAL_FUNCTION_MIN
        """
        minimum value of all numerical values is calculated.
        """
        NONE: GeneralFunction = GENERAL_FUNCTION_NONE
        """
        no cells are moved.
        
        sheet is not linked.
        
        new values are used without changes.
        
        nothing is calculated.
        
        nothing is imported.
        
        no condition is specified.
        """
        PRODUCT: GeneralFunction = GENERAL_FUNCTION_PRODUCT
        """
        product of all numerical values is calculated.
        """
        STDEV: GeneralFunction = GENERAL_FUNCTION_STDEV
        """
        standard deviation is calculated based on a sample.
        """
        STDEVP: GeneralFunction = GENERAL_FUNCTION_STDEVP
        """
        standard deviation is calculated based on the entire population.
        """
        SUM: GeneralFunction = GENERAL_FUNCTION_SUM
        """
        sum of all numerical values is calculated.
        """
        VAR: GeneralFunction = GENERAL_FUNCTION_VAR
        """
        variance is calculated based on a sample.
        """
        VARP: GeneralFunction = GENERAL_FUNCTION_VARP
        """
        variance is calculated based on the entire population.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class GeneralFunction(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.GeneralFunction", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.GeneralFunction`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['GeneralFunction']
