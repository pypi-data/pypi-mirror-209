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
# Namespace: com.sun.star.scanner
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.scanner.ScanError import InvalidContext as SCAN_ERROR_InvalidContext
    from com.sun.star.scanner.ScanError import ScanCanceled as SCAN_ERROR_ScanCanceled
    from com.sun.star.scanner.ScanError import ScanErrorNone as SCAN_ERROR_ScanErrorNone
    from com.sun.star.scanner.ScanError import ScanFailed as SCAN_ERROR_ScanFailed
    from com.sun.star.scanner.ScanError import ScanInProgress as SCAN_ERROR_ScanInProgress
    from com.sun.star.scanner.ScanError import ScannerNotAvailable as SCAN_ERROR_ScannerNotAvailable

    class ScanError(uno.Enum):
        """
        Enum Class


        See Also:
            `API ScanError <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1scanner.html#abd1619ea132004db8599d9529755e9ab>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.scanner.ScanError', value)

        __ooo_ns__: str = 'com.sun.star.scanner'
        __ooo_full_ns__: str = 'com.sun.star.scanner.ScanError'
        __ooo_type_name__: str = 'enum'

        InvalidContext = cast("ScanError", SCAN_ERROR_InvalidContext)
        """
        InvalidContext: a device was requested that does not exist.
        """
        ScanCanceled = cast("ScanError", SCAN_ERROR_ScanCanceled)
        """
        ScanCanceled: the scan was canceled by the user.
        """
        ScanErrorNone = cast("ScanError", SCAN_ERROR_ScanErrorNone)
        """
        ScanErrorNone: no error occurred.
        """
        ScanFailed = cast("ScanError", SCAN_ERROR_ScanFailed)
        """
        ScanFailed: an error occurred during scanning.
        """
        ScanInProgress = cast("ScanError", SCAN_ERROR_ScanInProgress)
        """
        ScanInProgress: a scan is already in progress on this device that has to end before a new one can be started.
        """
        ScannerNotAvailable = cast("ScanError", SCAN_ERROR_ScannerNotAvailable)
        """
        ScannerNotAvailable: the requested device could not be opened.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ScanError(metaclass=UnoEnumMeta, type_name="com.sun.star.scanner.ScanError", name_space="com.sun.star.scanner"):
        """Dynamically created class that represents ``com.sun.star.scanner.ScanError`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ScanError']
