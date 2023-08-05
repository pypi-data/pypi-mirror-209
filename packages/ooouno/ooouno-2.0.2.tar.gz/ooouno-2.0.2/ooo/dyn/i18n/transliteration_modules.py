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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.i18n.TransliterationModules import END_OF_MODULE as TRANSLITERATION_MODULES_END_OF_MODULE
    from com.sun.star.i18n.TransliterationModules import FULLWIDTH_HALFWIDTH as TRANSLITERATION_MODULES_FULLWIDTH_HALFWIDTH
    from com.sun.star.i18n.TransliterationModules import HALFWIDTH_FULLWIDTH as TRANSLITERATION_MODULES_HALFWIDTH_FULLWIDTH
    from com.sun.star.i18n.TransliterationModules import HIRAGANA_KATAKANA as TRANSLITERATION_MODULES_HIRAGANA_KATAKANA
    from com.sun.star.i18n.TransliterationModules import IGNORE_CASE as TRANSLITERATION_MODULES_IGNORE_CASE
    from com.sun.star.i18n.TransliterationModules import IGNORE_KANA as TRANSLITERATION_MODULES_IGNORE_KANA
    from com.sun.star.i18n.TransliterationModules import IGNORE_MASK as TRANSLITERATION_MODULES_IGNORE_MASK
    from com.sun.star.i18n.TransliterationModules import IGNORE_WIDTH as TRANSLITERATION_MODULES_IGNORE_WIDTH
    from com.sun.star.i18n.TransliterationModules import IgnoreBaFa_ja_JP as TRANSLITERATION_MODULES_IgnoreBaFa_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreHyuByu_ja_JP as TRANSLITERATION_MODULES_IgnoreHyuByu_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreIandEfollowedByYa_ja_JP as TRANSLITERATION_MODULES_IgnoreIandEfollowedByYa_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreIterationMark_ja_JP as TRANSLITERATION_MODULES_IgnoreIterationMark_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreKiKuFollowedBySa_ja_JP as TRANSLITERATION_MODULES_IgnoreKiKuFollowedBySa_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreMiddleDot_ja_JP as TRANSLITERATION_MODULES_IgnoreMiddleDot_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreMinusSign_ja_JP as TRANSLITERATION_MODULES_IgnoreMinusSign_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreProlongedSoundMark_ja_JP as TRANSLITERATION_MODULES_IgnoreProlongedSoundMark_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreSeZe_ja_JP as TRANSLITERATION_MODULES_IgnoreSeZe_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreSeparator_ja_JP as TRANSLITERATION_MODULES_IgnoreSeparator_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreSize_ja_JP as TRANSLITERATION_MODULES_IgnoreSize_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreSpace_ja_JP as TRANSLITERATION_MODULES_IgnoreSpace_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreTiJi_ja_JP as TRANSLITERATION_MODULES_IgnoreTiJi_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreTraditionalKana_ja_JP as TRANSLITERATION_MODULES_IgnoreTraditionalKana_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreTraditionalKanji_ja_JP as TRANSLITERATION_MODULES_IgnoreTraditionalKanji_ja_JP
    from com.sun.star.i18n.TransliterationModules import IgnoreZiZu_ja_JP as TRANSLITERATION_MODULES_IgnoreZiZu_ja_JP
    from com.sun.star.i18n.TransliterationModules import KATAKANA_HIRAGANA as TRANSLITERATION_MODULES_KATAKANA_HIRAGANA
    from com.sun.star.i18n.TransliterationModules import LOWERCASE_UPPERCASE as TRANSLITERATION_MODULES_LOWERCASE_UPPERCASE
    from com.sun.star.i18n.TransliterationModules import LargeToSmall_ja_JP as TRANSLITERATION_MODULES_LargeToSmall_ja_JP
    from com.sun.star.i18n.TransliterationModules import NON_IGNORE_MASK as TRANSLITERATION_MODULES_NON_IGNORE_MASK
    from com.sun.star.i18n.TransliterationModules import NumToTextFormalHangul_ko as TRANSLITERATION_MODULES_NumToTextFormalHangul_ko
    from com.sun.star.i18n.TransliterationModules import NumToTextFormalLower_ko as TRANSLITERATION_MODULES_NumToTextFormalLower_ko
    from com.sun.star.i18n.TransliterationModules import NumToTextFormalUpper_ko as TRANSLITERATION_MODULES_NumToTextFormalUpper_ko
    from com.sun.star.i18n.TransliterationModules import NumToTextLower_zh_CN as TRANSLITERATION_MODULES_NumToTextLower_zh_CN
    from com.sun.star.i18n.TransliterationModules import NumToTextLower_zh_TW as TRANSLITERATION_MODULES_NumToTextLower_zh_TW
    from com.sun.star.i18n.TransliterationModules import NumToTextUpper_zh_CN as TRANSLITERATION_MODULES_NumToTextUpper_zh_CN
    from com.sun.star.i18n.TransliterationModules import NumToTextUpper_zh_TW as TRANSLITERATION_MODULES_NumToTextUpper_zh_TW
    from com.sun.star.i18n.TransliterationModules import SmallToLarge_ja_JP as TRANSLITERATION_MODULES_SmallToLarge_ja_JP
    from com.sun.star.i18n.TransliterationModules import UPPERCASE_LOWERCASE as TRANSLITERATION_MODULES_UPPERCASE_LOWERCASE

    class TransliterationModules(uno.Enum):
        """
        Enum Class


        See Also:
            `API TransliterationModules <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n.html#a9c57a33dd757352c82923f4c7f6cf93c>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.i18n.TransliterationModules', value)

        __ooo_ns__: str = 'com.sun.star.i18n'
        __ooo_full_ns__: str = 'com.sun.star.i18n.TransliterationModules'
        __ooo_type_name__: str = 'enum'

        END_OF_MODULE: TransliterationModules = TRANSLITERATION_MODULES_END_OF_MODULE
        """
        """
        FULLWIDTH_HALFWIDTH: TransliterationModules = TRANSLITERATION_MODULES_FULLWIDTH_HALFWIDTH
        """
        Transliterate a string from full width character to half width character.
        """
        HALFWIDTH_FULLWIDTH: TransliterationModules = TRANSLITERATION_MODULES_HALFWIDTH_FULLWIDTH
        """
        Transliterate a string from half width character to full width character.
        """
        HIRAGANA_KATAKANA: TransliterationModules = TRANSLITERATION_MODULES_HIRAGANA_KATAKANA
        """
        Transliterate a Japanese string from Hiragana to Katakana.
        """
        IGNORE_CASE: TransliterationModules = TRANSLITERATION_MODULES_IGNORE_CASE
        """
        Ignore case when comparing strings by transliteration service.
        """
        IGNORE_KANA: TransliterationModules = TRANSLITERATION_MODULES_IGNORE_KANA
        """
        Ignore Hiragana and Katakana when comparing strings by transliteration service.
        """
        IGNORE_MASK: TransliterationModules = TRANSLITERATION_MODULES_IGNORE_MASK
        """
        """
        IGNORE_WIDTH: TransliterationModules = TRANSLITERATION_MODULES_IGNORE_WIDTH
        """
        Ignore full width and half width character when comparing strings by transliteration service.
        
        Ignore full width and half width characters when comparing strings by transliteration service.
        """
        IgnoreBaFa_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreBaFa_ja_JP
        """
        Ignore Katakana and Hiragana Ba/Gua and Ha/Fa in Japanese fuzzy search.
        """
        IgnoreHyuByu_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreHyuByu_ja_JP
        """
        Ignore Katakana and Hiragana Hyu/Fyu and Byu/Gyu in Japanese fuzzy search.
        """
        IgnoreIandEfollowedByYa_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreIandEfollowedByYa_ja_JP
        """
        Ignore Katakana YA/A which follows the character in either I or E row in Japanese fuzzy search.
        
        Ignore Katakana YA/A following the character in either I or E row in Japanese fuzzy search.
        """
        IgnoreIterationMark_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreIterationMark_ja_JP
        """
        Ignore Hiragana and Katakana iteration mark in Japanese fuzzy search.
        """
        IgnoreKiKuFollowedBySa_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreKiKuFollowedBySa_ja_JP
        """
        Ignore Katakana KI/KU which follows the character in SA column in Japanese fuzzy search.
        
        Ignore Katakana KI/KU following the character in SA column in Japanese fuzzy search.
        """
        IgnoreMiddleDot_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreMiddleDot_ja_JP
        """
        Ignore middle dot in Japanese fuzzy search.
        """
        IgnoreMinusSign_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreMinusSign_ja_JP
        """
        Ignore dash or minus sign in Japanese fuzzy search.
        """
        IgnoreProlongedSoundMark_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreProlongedSoundMark_ja_JP
        """
        Ignore Japanese prolonged sound mark in Japanese fuzzy search.
        """
        IgnoreSeZe_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreSeZe_ja_JP
        """
        Ignore Katakana and Hiragana Se/Sye and Ze/Je in Japanese fuzzy search.
        """
        IgnoreSeparator_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreSeparator_ja_JP
        """
        Ignore separator punctuations in Japanese fuzzy search.
        """
        IgnoreSize_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreSize_ja_JP
        """
        Ignore Japanese normal and small sized character in Japanese fuzzy search.
        """
        IgnoreSpace_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreSpace_ja_JP
        """
        Ignore white space characters, include space, TAB, return, etc. in Japanese fuzzy search.
        """
        IgnoreTiJi_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreTiJi_ja_JP
        """
        Ignore Katakana and Hiragana Tsui/Tea/Ti and Dyi/Ji in Japanese fuzzy search.
        """
        IgnoreTraditionalKana_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreTraditionalKana_ja_JP
        """
        Ignore Japanese traditional Katakana and Hiragana character in Japanese fuzzy search.
        
        Ignore Japanese traditional Katakana and Hiragana characters in Japanese fuzzy search.
        """
        IgnoreTraditionalKanji_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreTraditionalKanji_ja_JP
        """
        Ignore Japanese traditional Kanji character in Japanese fuzzy search.
        
        Ignore Japanese traditional Kanji characters in Japanese fuzzy search.
        """
        IgnoreZiZu_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_IgnoreZiZu_ja_JP
        """
        Ignore Katakana and Hiragana Zi/Zi and Zu/Zu in Japanese fuzzy search.
        """
        KATAKANA_HIRAGANA: TransliterationModules = TRANSLITERATION_MODULES_KATAKANA_HIRAGANA
        """
        Transliterate a Japanese string from Katakana to Hiragana.
        """
        LOWERCASE_UPPERCASE: TransliterationModules = TRANSLITERATION_MODULES_LOWERCASE_UPPERCASE
        """
        Transliterate a string from lower case to upper case.
        """
        LargeToSmall_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_LargeToSmall_ja_JP
        """
        transliterate Japanese normal sized character to small sized character
        """
        NON_IGNORE_MASK: TransliterationModules = TRANSLITERATION_MODULES_NON_IGNORE_MASK
        """
        """
        NumToTextFormalHangul_ko: TransliterationModules = TRANSLITERATION_MODULES_NumToTextFormalHangul_ko
        """
        Transliterate an ASCII number string to formal Korean Hangul number string in spellout format.
        """
        NumToTextFormalLower_ko: TransliterationModules = TRANSLITERATION_MODULES_NumToTextFormalLower_ko
        """
        Transliterate an ASCII number string to formal Korean Hanja lower case number string in spellout format.
        """
        NumToTextFormalUpper_ko: TransliterationModules = TRANSLITERATION_MODULES_NumToTextFormalUpper_ko
        """
        Transliterate an ASCII number string to formal Korean Hanja upper case number string in spellout format.
        """
        NumToTextLower_zh_CN: TransliterationModules = TRANSLITERATION_MODULES_NumToTextLower_zh_CN
        """
        Transliterate an ASCII number string to Simplified Chinese lower case number string in spellout format.
        """
        NumToTextLower_zh_TW: TransliterationModules = TRANSLITERATION_MODULES_NumToTextLower_zh_TW
        """
        Transliterate an ASCII number string to Traditional Chinese lower case number string in spellout format.
        """
        NumToTextUpper_zh_CN: TransliterationModules = TRANSLITERATION_MODULES_NumToTextUpper_zh_CN
        """
        Transliterate an ASCII number string to Simplified Chinese upper case number string in spellout format.
        """
        NumToTextUpper_zh_TW: TransliterationModules = TRANSLITERATION_MODULES_NumToTextUpper_zh_TW
        """
        Transliterate an ASCII number string to Traditional Chinese upper case number string in spellout format.
        """
        SmallToLarge_ja_JP: TransliterationModules = TRANSLITERATION_MODULES_SmallToLarge_ja_JP
        """
        transliterate Japanese small sized character to normal sized character
        """
        UPPERCASE_LOWERCASE: TransliterationModules = TRANSLITERATION_MODULES_UPPERCASE_LOWERCASE
        """
        Transliterate a string from upper case to lower case.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TransliterationModules(metaclass=UnoEnumMeta, type_name="com.sun.star.i18n.TransliterationModules", name_space="com.sun.star.i18n"):
        """Dynamically created class that represents ``com.sun.star.i18n.TransliterationModules`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TransliterationModules']
