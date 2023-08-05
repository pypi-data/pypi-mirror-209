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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.util.DataEditorEventType import CANCELED as DATA_EDITOR_EVENT_TYPE_CANCELED
    from com.sun.star.util.DataEditorEventType import DONE as DATA_EDITOR_EVENT_TYPE_DONE

    class DataEditorEventType(uno.Enum):
        """
        Enum Class


        See Also:
            `API DataEditorEventType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util.html#a78015743cb8b25dbfc2b64889f6bd261>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.util.DataEditorEventType', value)

        __ooo_ns__: str = 'com.sun.star.util'
        __ooo_full_ns__: str = 'com.sun.star.util.DataEditorEventType'
        __ooo_type_name__: str = 'enum'

        CANCELED = cast("DataEditorEventType", DATA_EDITOR_EVENT_TYPE_CANCELED)
        """
        specifies that the data editing was canceled by the user (data not stored).
        """
        DONE = cast("DataEditorEventType", DATA_EDITOR_EVENT_TYPE_DONE)
        """
        specifies that the data editing is done (data stored).
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DataEditorEventType(metaclass=UnoEnumMeta, type_name="com.sun.star.util.DataEditorEventType", name_space="com.sun.star.util"):
        """Dynamically created class that represents ``com.sun.star.util.DataEditorEventType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DataEditorEventType']
