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
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.reflection.TypeDescriptionSearchDepth import INFINITE as TYPE_DESCRIPTION_SEARCH_DEPTH_INFINITE
    from com.sun.star.reflection.TypeDescriptionSearchDepth import ONE as TYPE_DESCRIPTION_SEARCH_DEPTH_ONE

    class TypeDescriptionSearchDepth(uno.Enum):
        """
        Enum Class


        See Also:
            `API TypeDescriptionSearchDepth <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1reflection.html#a19627c9e2873087a7d672cd9e0913000>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.reflection.TypeDescriptionSearchDepth', value)

        __ooo_ns__: str = 'com.sun.star.reflection'
        __ooo_full_ns__: str = 'com.sun.star.reflection.TypeDescriptionSearchDepth'
        __ooo_type_name__: str = 'enum'

        INFINITE = cast("TypeDescriptionSearchDepth", TYPE_DESCRIPTION_SEARCH_DEPTH_INFINITE)
        """
        Infinite search depth.
        
        Search through all children including direct children, grand children, grand children's children, ...
        """
        ONE = cast("TypeDescriptionSearchDepth", TYPE_DESCRIPTION_SEARCH_DEPTH_ONE)
        """
        Search only through direct children.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TypeDescriptionSearchDepth(metaclass=UnoEnumMeta, type_name="com.sun.star.reflection.TypeDescriptionSearchDepth", name_space="com.sun.star.reflection"):
        """Dynamically created class that represents ``com.sun.star.reflection.TypeDescriptionSearchDepth`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TypeDescriptionSearchDepth']
