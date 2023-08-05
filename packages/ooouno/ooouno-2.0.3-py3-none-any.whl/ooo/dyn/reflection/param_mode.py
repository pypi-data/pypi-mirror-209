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

    from com.sun.star.reflection.ParamMode import IN as PARAM_MODE_IN
    from com.sun.star.reflection.ParamMode import INOUT as PARAM_MODE_INOUT
    from com.sun.star.reflection.ParamMode import OUT as PARAM_MODE_OUT

    class ParamMode(uno.Enum):
        """
        Enum Class


        See Also:
            `API ParamMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1reflection.html#ada880a15fc14bc0e53c3dd7c3c8a34eb>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.reflection.ParamMode', value)

        __ooo_ns__: str = 'com.sun.star.reflection'
        __ooo_full_ns__: str = 'com.sun.star.reflection.ParamMode'
        __ooo_type_name__: str = 'enum'

        IN = cast("ParamMode", PARAM_MODE_IN)
        """
        parameter serves as pure input for a called method
        """
        INOUT = cast("ParamMode", PARAM_MODE_INOUT)
        """
        parameter serves as input as well as output; data can transferred in both directions
        """
        OUT = cast("ParamMode", PARAM_MODE_OUT)
        """
        parameter serves as pure output for the callee (in addition to the return value)
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ParamMode(metaclass=UnoEnumMeta, type_name="com.sun.star.reflection.ParamMode", name_space="com.sun.star.reflection"):
        """Dynamically created class that represents ``com.sun.star.reflection.ParamMode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ParamMode']
