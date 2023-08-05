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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .date import Date as Date_60040844


class DateWithTimezone(object):
    """
    Struct Class

    represents a date value with time zone.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateWithTimezone <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateWithTimezone.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.DateWithTimezone'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.DateWithTimezone'
    """Literal Constant ``com.sun.star.util.DateWithTimezone``"""

    def __init__(self, DateInTZ: typing.Optional[Date_60040844] = UNO_NONE, Timezone: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            DateInTZ (Date, optional): DateInTZ value.
            Timezone (int, optional): Timezone value.
        """
        super().__init__()

        if isinstance(DateInTZ, DateWithTimezone):
            oth: DateWithTimezone = DateInTZ
            self.DateInTZ = oth.DateInTZ
            self.Timezone = oth.Timezone
            return

        kargs = {
            "DateInTZ": DateInTZ,
            "Timezone": Timezone,
        }
        if kargs["DateInTZ"] is UNO_NONE:
            kargs["DateInTZ"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._date_in_tz = kwargs["DateInTZ"]
        self._timezone = kwargs["Timezone"]


    @property
    def DateInTZ(self) -> Date_60040844:
        """
        the date.
        """
        return self._date_in_tz

    @DateInTZ.setter
    def DateInTZ(self, value: Date_60040844) -> None:
        self._date_in_tz = value

    @property
    def Timezone(self) -> int:
        """
        contains the time zone, as signed offset in minutes from UTC, that is east of UTC, that is the amount of minutes that should be added to UTC time to obtain time in that timezone.
        """
        return self._timezone

    @Timezone.setter
    def Timezone(self, value: int) -> None:
        self._timezone = value


__all__ = ['DateWithTimezone']
