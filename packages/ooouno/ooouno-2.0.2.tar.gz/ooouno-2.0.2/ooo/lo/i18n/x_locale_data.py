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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .calendar import Calendar as Calendar_7f2d0962
    from .currency import Currency as Currency_80230993
    from .forbidden_characters import ForbiddenCharacters as ForbiddenCharacters_ce0dd5
    from .format_element import FormatElement as FormatElement_b4c70b7b
    from .implementation import Implementation as Implementation_c1d50c0e
    from .language_country_info import LanguageCountryInfo as LanguageCountryInfo_1f20dec
    from .locale_data_item import LocaleDataItem as LocaleDataItem_beff0ba1
    from ..lang.locale import Locale as Locale_70d308fa

class XLocaleData(XInterface_8f010a43):
    """
    Access locale specific data as it is defined in XML locale data files compiled into the binary data libraries liblocaledata*.so respectively localedata*.dll.
    
    For XML locale data files definitions see the DTD file.

    See Also:
        `API XLocaleData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XLocaleData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XLocaleData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XLocaleData'

    @abstractmethod
    def getAllCalendars(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[Calendar_7f2d0962, ...]':
        """
        returns all LC_CALENDAR calendars for a locale.
        """
        ...
    @abstractmethod
    def getAllCurrencies(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[Currency_80230993, ...]':
        """
        returns all LC_CURRENCY currencies for a locale.
        """
        ...
    @abstractmethod
    def getAllFormats(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[FormatElement_b4c70b7b, ...]':
        """
        returns all LC_FORMAT format elements for a locale.
        """
        ...
    @abstractmethod
    def getAllInstalledLocaleNames(self) -> 'typing.Tuple[Locale_70d308fa, ...]':
        """
        returns all available locales.
        """
        ...
    @abstractmethod
    def getCollationOptions(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        returns all LC_COLLATION collation options for a locale.
        """
        ...
    @abstractmethod
    def getCollatorImplementations(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[Implementation_c1d50c0e, ...]':
        """
        returns all LC_COLLATION collators for a locale.
        """
        ...
    @abstractmethod
    def getForbiddenCharacters(self, aLocale: 'Locale_70d308fa') -> 'ForbiddenCharacters_ce0dd5':
        """
        returns all LC_MISC forbidden characters for a locale.
        """
        ...
    @abstractmethod
    def getLanguageCountryInfo(self, aLocale: 'Locale_70d308fa') -> 'LanguageCountryInfo_1f20dec':
        """
        returns the LC_INFO locale information.
        """
        ...
    @abstractmethod
    def getLocaleItem(self, aLocale: 'Locale_70d308fa') -> 'LocaleDataItem_beff0ba1':
        """
        returns LC_CTYPE separators and markers.
        """
        ...
    @abstractmethod
    def getReservedWord(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        returns all LC_MISC reserved words for a locale.
        """
        ...
    @abstractmethod
    def getSearchOptions(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        returns all LC_SEARCH search options for a locale.
        """
        ...
    @abstractmethod
    def getTransliterations(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        returns all LC_TRANSLITERATION transliterations for a locale.
        """
        ...

__all__ = ['XLocaleData']

