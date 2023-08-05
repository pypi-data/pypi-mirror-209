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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from .date import Date as Date_60040844

class NumberFormatSettings(XPropertySet_bc180bfa):
    """
    Service Class

    specifies the settings for number formatting.

    See Also:
        `API NumberFormatSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1NumberFormatSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.NumberFormatSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def NoZero(self) -> bool:
        """
        is set to indicate that a zero value should be formatted as an empty string.
        """
        ...

    @abstractproperty
    def NullDate(self) -> 'Date_60040844':
        """
        specifies the date which is represented by the value 0.
        
        The most common value for this is 12/30/1899.
        """
        ...

    @abstractproperty
    def StandardDecimals(self) -> int:
        """
        specifies the maximum number of decimals used for the standard number format (\"General\").
        """
        ...

    @abstractproperty
    def TwoDigitDateStart(self) -> int:
        """
        specifies the first year to be generated from a two-digit year input.
        """
        ...


__all__ = ['NumberFormatSettings']

