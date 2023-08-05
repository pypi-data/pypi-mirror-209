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
# Namespace: com.sun.star.uri
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.uri.RelativeUriExcessParentSegments import ERROR as RELATIVE_URI_EXCESS_PARENT_SEGMENTS_ERROR
    from com.sun.star.uri.RelativeUriExcessParentSegments import REMOVE as RELATIVE_URI_EXCESS_PARENT_SEGMENTS_REMOVE
    from com.sun.star.uri.RelativeUriExcessParentSegments import RETAIN as RELATIVE_URI_EXCESS_PARENT_SEGMENTS_RETAIN

    class RelativeUriExcessParentSegments(uno.Enum):
        """
        Enum Class


        See Also:
            `API RelativeUriExcessParentSegments <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uri.html#ac4782e395626cbc2118cab947e07af22>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.uri.RelativeUriExcessParentSegments', value)

        __ooo_ns__: str = 'com.sun.star.uri'
        __ooo_full_ns__: str = 'com.sun.star.uri.RelativeUriExcessParentSegments'
        __ooo_type_name__: str = 'enum'

        ERROR: RelativeUriExcessParentSegments = RELATIVE_URI_EXCESS_PARENT_SEGMENTS_ERROR
        """
        causes excess special parent segments to be treated as an error.
        """
        REMOVE: RelativeUriExcessParentSegments = RELATIVE_URI_EXCESS_PARENT_SEGMENTS_REMOVE
        """
        causes excess special parent segments to be removed.
        """
        RETAIN: RelativeUriExcessParentSegments = RELATIVE_URI_EXCESS_PARENT_SEGMENTS_RETAIN
        """
        causes excess special parent segments to be retained, treating them like ordinary segments.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class RelativeUriExcessParentSegments(metaclass=UnoEnumMeta, type_name="com.sun.star.uri.RelativeUriExcessParentSegments", name_space="com.sun.star.uri"):
        """Dynamically created class that represents ``com.sun.star.uri.RelativeUriExcessParentSegments`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['RelativeUriExcessParentSegments']
