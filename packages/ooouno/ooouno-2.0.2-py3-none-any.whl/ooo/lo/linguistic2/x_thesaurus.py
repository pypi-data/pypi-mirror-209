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
# Namespace: com.sun.star.linguistic2
import typing
from abc import abstractmethod
from .x_supported_locales import XSupportedLocales as XSupportedLocales_5bda1056
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..lang.locale import Locale as Locale_70d308fa
    from .x_meaning import XMeaning as XMeaning_d65e0c8c

class XThesaurus(XSupportedLocales_5bda1056):
    """
    allows for the retrieval of possible meanings for a given word and language.
    
    The meaning of a word is in essence a descriptive text for that word. Each meaning may have several synonyms where a synonym is a word (or small text) with the same or similar meaning.

    See Also:
        `API XThesaurus <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XThesaurus.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XThesaurus'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XThesaurus'

    @abstractmethod
    def queryMeanings(self, aTerm: str, aLocale: 'Locale_70d308fa', aProperties: 'PropertyValues_d6470ce6') -> 'typing.Tuple[XMeaning_d65e0c8c, ...]':
        """
        If the language is not supported, an com.sun.star.lang.IllegalArgumentException exception is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XThesaurus']

