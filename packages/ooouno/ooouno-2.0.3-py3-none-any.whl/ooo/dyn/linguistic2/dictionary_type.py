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
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.linguistic2.DictionaryType import MIXED as DICTIONARY_TYPE_MIXED
    from com.sun.star.linguistic2.DictionaryType import NEGATIVE as DICTIONARY_TYPE_NEGATIVE
    from com.sun.star.linguistic2.DictionaryType import POSITIVE as DICTIONARY_TYPE_POSITIVE

    class DictionaryType(uno.Enum):
        """
        Enum Class


        See Also:
            `API DictionaryType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2.html#a281c5a7578308b66c77c9e0de51b806a>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.linguistic2.DictionaryType', value)

        __ooo_ns__: str = 'com.sun.star.linguistic2'
        __ooo_full_ns__: str = 'com.sun.star.linguistic2.DictionaryType'
        __ooo_type_name__: str = 'enum'

        MIXED = cast("DictionaryType", DICTIONARY_TYPE_MIXED)
        """
        """
        NEGATIVE = cast("DictionaryType", DICTIONARY_TYPE_NEGATIVE)
        """
        all entries in the dictionary are negative.
        """
        POSITIVE = cast("DictionaryType", DICTIONARY_TYPE_POSITIVE)
        """
        all entries in the dictionary are positive.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DictionaryType(metaclass=UnoEnumMeta, type_name="com.sun.star.linguistic2.DictionaryType", name_space="com.sun.star.linguistic2"):
        """Dynamically created class that represents ``com.sun.star.linguistic2.DictionaryType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DictionaryType']
