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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility


class AccessibleTextType(object):
    """
    Const Class

    Collection of types of text portions.
    
    This collection describes the types of text portions that can be accessed with the help of the methods of the XAccessibleText interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleTextType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleTextType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.AccessibleTextType'
    __ooo_type_name__: str = 'const'

    CHARACTER = 1
    """
    Single character.
    
    Indicates that single (multibyte) characters are used.
    """
    WORD = 2
    """
    Single word.
    
    Indicates that single words are used. The definition of what a word is, is implementation and language/locale dependent. While in English a word is ended by a space or a special character like a comma or a period, this is not necessarily true in other languages.
    """
    SENTENCE = 3
    """
    Single sentence.
    
    Indicates that single sentences are used. The definition of what a sentence is, is implementation and language/locale dependent. While in English a sentence is ended by a period, this is not necessarily true in other languages.
    """
    PARAGRAPH = 4
    """
    Single paragraph.
    
    Indicates that single paragraphs are used. The definition of what a paragraph is, is implementation and language/locale dependent.
    """
    LINE = 5
    """
    Single line.
    
    Indicates that single lines, as displayed on the screen, are used. In contrast to the constants CHARACTER, WORD, SENTENCE, and PARAGRAPH which are content oriented this constant is view oriented. It can be used to retrieve hyphenation information.
    """
    GLYPH = 6
    """
    Single glyph.
    
    Glyphs are runs of one or more (multibyte) characters which are displayed as one symbol.
    """
    ATTRIBUTE_RUN = 7
    """
    Attribute run.
    
    Each attribute run is a character run of maximal length where all characters have the same attributes set.
    """

__all__ = ['AccessibleTextType']
