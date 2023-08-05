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
from enum import Enum


class TransliterationModules(Enum):
    """
    Enum Class


    See Also:
        `API TransliterationModules <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n.html#a9c57a33dd757352c82923f4c7f6cf93c>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.TransliterationModules'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.i18n.TransliterationModules'

    END_OF_MODULE = 'END_OF_MODULE'
    """
    """
    FULLWIDTH_HALFWIDTH = 'FULLWIDTH_HALFWIDTH'
    """
    Transliterate a string from full width character to half width character.
    """
    HALFWIDTH_FULLWIDTH = 'HALFWIDTH_FULLWIDTH'
    """
    Transliterate a string from half width character to full width character.
    """
    HIRAGANA_KATAKANA = 'HIRAGANA_KATAKANA'
    """
    Transliterate a Japanese string from Hiragana to Katakana.
    """
    IGNORE_CASE = 'IGNORE_CASE'
    """
    Ignore case when comparing strings by transliteration service.
    """
    IGNORE_KANA = 'IGNORE_KANA'
    """
    Ignore Hiragana and Katakana when comparing strings by transliteration service.
    """
    IGNORE_MASK = 'IGNORE_MASK'
    """
    """
    IGNORE_WIDTH = 'IGNORE_WIDTH'
    """
    Ignore full width and half width character when comparing strings by transliteration service.
    
    Ignore full width and half width characters when comparing strings by transliteration service.
    """
    IgnoreBaFa_ja_JP = 'IgnoreBaFa_ja_JP'
    """
    Ignore Katakana and Hiragana Ba/Gua and Ha/Fa in Japanese fuzzy search.
    """
    IgnoreHyuByu_ja_JP = 'IgnoreHyuByu_ja_JP'
    """
    Ignore Katakana and Hiragana Hyu/Fyu and Byu/Gyu in Japanese fuzzy search.
    """
    IgnoreIandEfollowedByYa_ja_JP = 'IgnoreIandEfollowedByYa_ja_JP'
    """
    Ignore Katakana YA/A which follows the character in either I or E row in Japanese fuzzy search.
    
    Ignore Katakana YA/A following the character in either I or E row in Japanese fuzzy search.
    """
    IgnoreIterationMark_ja_JP = 'IgnoreIterationMark_ja_JP'
    """
    Ignore Hiragana and Katakana iteration mark in Japanese fuzzy search.
    """
    IgnoreKiKuFollowedBySa_ja_JP = 'IgnoreKiKuFollowedBySa_ja_JP'
    """
    Ignore Katakana KI/KU which follows the character in SA column in Japanese fuzzy search.
    
    Ignore Katakana KI/KU following the character in SA column in Japanese fuzzy search.
    """
    IgnoreMiddleDot_ja_JP = 'IgnoreMiddleDot_ja_JP'
    """
    Ignore middle dot in Japanese fuzzy search.
    """
    IgnoreMinusSign_ja_JP = 'IgnoreMinusSign_ja_JP'
    """
    Ignore dash or minus sign in Japanese fuzzy search.
    """
    IgnoreProlongedSoundMark_ja_JP = 'IgnoreProlongedSoundMark_ja_JP'
    """
    Ignore Japanese prolonged sound mark in Japanese fuzzy search.
    """
    IgnoreSeZe_ja_JP = 'IgnoreSeZe_ja_JP'
    """
    Ignore Katakana and Hiragana Se/Sye and Ze/Je in Japanese fuzzy search.
    """
    IgnoreSeparator_ja_JP = 'IgnoreSeparator_ja_JP'
    """
    Ignore separator punctuations in Japanese fuzzy search.
    """
    IgnoreSize_ja_JP = 'IgnoreSize_ja_JP'
    """
    Ignore Japanese normal and small sized character in Japanese fuzzy search.
    """
    IgnoreSpace_ja_JP = 'IgnoreSpace_ja_JP'
    """
    Ignore white space characters, include space, TAB, return, etc. in Japanese fuzzy search.
    """
    IgnoreTiJi_ja_JP = 'IgnoreTiJi_ja_JP'
    """
    Ignore Katakana and Hiragana Tsui/Tea/Ti and Dyi/Ji in Japanese fuzzy search.
    """
    IgnoreTraditionalKana_ja_JP = 'IgnoreTraditionalKana_ja_JP'
    """
    Ignore Japanese traditional Katakana and Hiragana character in Japanese fuzzy search.
    
    Ignore Japanese traditional Katakana and Hiragana characters in Japanese fuzzy search.
    """
    IgnoreTraditionalKanji_ja_JP = 'IgnoreTraditionalKanji_ja_JP'
    """
    Ignore Japanese traditional Kanji character in Japanese fuzzy search.
    
    Ignore Japanese traditional Kanji characters in Japanese fuzzy search.
    """
    IgnoreZiZu_ja_JP = 'IgnoreZiZu_ja_JP'
    """
    Ignore Katakana and Hiragana Zi/Zi and Zu/Zu in Japanese fuzzy search.
    """
    KATAKANA_HIRAGANA = 'KATAKANA_HIRAGANA'
    """
    Transliterate a Japanese string from Katakana to Hiragana.
    """
    LOWERCASE_UPPERCASE = 'LOWERCASE_UPPERCASE'
    """
    Transliterate a string from lower case to upper case.
    """
    LargeToSmall_ja_JP = 'LargeToSmall_ja_JP'
    """
    transliterate Japanese normal sized character to small sized character
    """
    NON_IGNORE_MASK = 'NON_IGNORE_MASK'
    """
    """
    NumToTextFormalHangul_ko = 'NumToTextFormalHangul_ko'
    """
    Transliterate an ASCII number string to formal Korean Hangul number string in spellout format.
    """
    NumToTextFormalLower_ko = 'NumToTextFormalLower_ko'
    """
    Transliterate an ASCII number string to formal Korean Hanja lower case number string in spellout format.
    """
    NumToTextFormalUpper_ko = 'NumToTextFormalUpper_ko'
    """
    Transliterate an ASCII number string to formal Korean Hanja upper case number string in spellout format.
    """
    NumToTextLower_zh_CN = 'NumToTextLower_zh_CN'
    """
    Transliterate an ASCII number string to Simplified Chinese lower case number string in spellout format.
    """
    NumToTextLower_zh_TW = 'NumToTextLower_zh_TW'
    """
    Transliterate an ASCII number string to Traditional Chinese lower case number string in spellout format.
    """
    NumToTextUpper_zh_CN = 'NumToTextUpper_zh_CN'
    """
    Transliterate an ASCII number string to Simplified Chinese upper case number string in spellout format.
    """
    NumToTextUpper_zh_TW = 'NumToTextUpper_zh_TW'
    """
    Transliterate an ASCII number string to Traditional Chinese upper case number string in spellout format.
    """
    SmallToLarge_ja_JP = 'SmallToLarge_ja_JP'
    """
    transliterate Japanese small sized character to normal sized character
    """
    UPPERCASE_LOWERCASE = 'UPPERCASE_LOWERCASE'
    """
    Transliterate a string from upper case to lower case.
    """

__all__ = ['TransliterationModules']

