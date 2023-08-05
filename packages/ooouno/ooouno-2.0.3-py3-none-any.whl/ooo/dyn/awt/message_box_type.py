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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.awt.MessageBoxType import ERRORBOX as MESSAGE_BOX_TYPE_ERRORBOX
    from com.sun.star.awt.MessageBoxType import INFOBOX as MESSAGE_BOX_TYPE_INFOBOX
    from com.sun.star.awt.MessageBoxType import MESSAGEBOX as MESSAGE_BOX_TYPE_MESSAGEBOX
    from com.sun.star.awt.MessageBoxType import QUERYBOX as MESSAGE_BOX_TYPE_QUERYBOX
    from com.sun.star.awt.MessageBoxType import WARNINGBOX as MESSAGE_BOX_TYPE_WARNINGBOX

    class MessageBoxType(uno.Enum):
        """
        Enum Class


        See Also:
            `API MessageBoxType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.awt.MessageBoxType', value)

        __ooo_ns__: str = 'com.sun.star.awt'
        __ooo_full_ns__: str = 'com.sun.star.awt.MessageBoxType'
        __ooo_type_name__: str = 'enum'

        ERRORBOX = cast("MessageBoxType", MESSAGE_BOX_TYPE_ERRORBOX)
        """
        A message box to provide an error message to the user.
        """
        INFOBOX = cast("MessageBoxType", MESSAGE_BOX_TYPE_INFOBOX)
        """
        A message box to inform the user about a certain event.
        """
        MESSAGEBOX = cast("MessageBoxType", MESSAGE_BOX_TYPE_MESSAGEBOX)
        """
        A normal message box.
        """
        QUERYBOX = cast("MessageBoxType", MESSAGE_BOX_TYPE_QUERYBOX)
        """
        A message box to query information from the user.
        """
        WARNINGBOX = cast("MessageBoxType", MESSAGE_BOX_TYPE_WARNINGBOX)
        """
        A message to warn the user about a certain problem.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class MessageBoxType(metaclass=UnoEnumMeta, type_name="com.sun.star.awt.MessageBoxType", name_space="com.sun.star.awt"):
        """Dynamically created class that represents ``com.sun.star.awt.MessageBoxType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['MessageBoxType']
