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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Locale(object):
    """
    Struct Class

    object represents a specific geographical, political, or cultural region.
    
    An operation that requires a Locale to perform its task is called locale-sensitive and uses the Locale to tailor information for the user. For example, displaying a number is a locale-sensitive operation; the number should be formatted according to the customs/conventions of the user's native country, region, or culture.

    See Also:
        `API Locale <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1lang_1_1Locale.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.Locale'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.lang.Locale'
    """Literal Constant ``com.sun.star.lang.Locale``"""

    def __init__(self, Language: typing.Optional[str] = '', Country: typing.Optional[str] = '', Variant: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Language (str, optional): Language value.
            Country (str, optional): Country value.
            Variant (str, optional): Variant value.
        """
        super().__init__()

        if isinstance(Language, Locale):
            oth: Locale = Language
            self.Language = oth.Language
            self.Country = oth.Country
            self.Variant = oth.Variant
            return

        kargs = {
            "Language": Language,
            "Country": Country,
            "Variant": Variant,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._language = kwargs["Language"]
        self._country = kwargs["Country"]
        self._variant = kwargs["Variant"]


    @property
    def Language(self) -> str:
        """
        specifies an ISO 639 Language Code.
        
        These codes are preferably the lower-case two-letter codes as defined by ISO 639-1, or three-letter codes as defined by ISO 639-3. You can find a full list of these codes at a number of sites, such as: https://iso639-3.sil.org/code_tables/639/data.
        
        If this field contains an empty string, the meaning depends on the context.
        
        Since LibreOffice 4.2, if the locale can not be represented using only ISO 639 and ISO 3166 codes this field contains the ISO 639-3 reserved for local use code \"qlt\" and a BCP 47 language tag is present in the Variant field.
        """
        return self._language

    @Language.setter
    def Language(self, value: str) -> None:
        self._language = value

    @property
    def Country(self) -> str:
        """
        specifies an ISO 3166 Country Code.
        
        These codes are the upper-case two-letter codes as defined by ISO 3166-1. You can find a full list of these codes at a number of sites, such as: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.
        
        If this field contains an empty string, the meaning depends on the context.
        """
        return self._country

    @Country.setter
    def Country(self, value: str) -> None:
        self._country = value

    @property
    def Variant(self) -> str:
        """
        specifies a BCP 47 Language Tag.
        
        Since LibreOffice 4.2, if the Language field is the code \"qlt\" this field contains the full BCP 47 language tag. If the Language field is not \"qlt\" this field is empty.
        
        You can find BCP 47 language tag resources at https://en.wikipedia.org/wiki/IETF_language_tag and https://www.w3.org/International/articles/language-tags/.
        
        Earlier versions of the documentation mentioned \"vendor andbrowser-specific\" codes but that was never supported. Use of any arbitrary strings in the Variant field that do not form a valid BCP 47 language tag is strongly deprecated.
        """
        return self._variant

    @Variant.setter
    def Variant(self, value: str) -> None:
        self._variant = value


__all__ = ['Locale']
