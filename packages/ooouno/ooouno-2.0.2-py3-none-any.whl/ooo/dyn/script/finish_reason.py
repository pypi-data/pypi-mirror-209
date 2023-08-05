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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.script.FinishReason import Cancel as FINISH_REASON_Cancel
    from com.sun.star.script.FinishReason import Error as FINISH_REASON_Error
    from com.sun.star.script.FinishReason import OK as FINISH_REASON_OK

    class FinishReason(uno.Enum):
        """
        Enum Class


        See Also:
            `API FinishReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script.html#a8ab52fac6ca48179fe55e9a6aa3a345d>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.script.FinishReason', value)

        __ooo_ns__: str = 'com.sun.star.script'
        __ooo_full_ns__: str = 'com.sun.star.script.FinishReason'
        __ooo_type_name__: str = 'enum'

        Cancel: FinishReason = FINISH_REASON_Cancel
        """
        script in the engine was cancelled.
        
        script execution was cancelled.
        """
        Error: FinishReason = FINISH_REASON_Error
        """
        error occurred during script execution or compiling.
        """
        OK: FinishReason = FINISH_REASON_OK
        """
        script in the engine terminated normally.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FinishReason(metaclass=UnoEnumMeta, type_name="com.sun.star.script.FinishReason", name_space="com.sun.star.script"):
        """Dynamically created class that represents ``com.sun.star.script.FinishReason`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FinishReason']
