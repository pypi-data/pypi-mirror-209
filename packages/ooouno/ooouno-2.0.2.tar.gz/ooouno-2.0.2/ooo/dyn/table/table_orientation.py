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
# Namespace: com.sun.star.table
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.table.TableOrientation import COLUMNS as TABLE_ORIENTATION_COLUMNS
    from com.sun.star.table.TableOrientation import ROWS as TABLE_ORIENTATION_ROWS

    class TableOrientation(uno.Enum):
        """
        Enum Class


        See Also:
            `API TableOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#a2b2c6150472f0123357a2273c315401c>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.table.TableOrientation', value)

        __ooo_ns__: str = 'com.sun.star.table'
        __ooo_full_ns__: str = 'com.sun.star.table.TableOrientation'
        __ooo_type_name__: str = 'enum'

        COLUMNS: TableOrientation = TABLE_ORIENTATION_COLUMNS
        """
        operations are carried out on columns.
        """
        ROWS: TableOrientation = TABLE_ORIENTATION_ROWS
        """
        operations are carried out on rows.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TableOrientation(metaclass=UnoEnumMeta, type_name="com.sun.star.table.TableOrientation", name_space="com.sun.star.table"):
        """Dynamically created class that represents ``com.sun.star.table.TableOrientation`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TableOrientation']
