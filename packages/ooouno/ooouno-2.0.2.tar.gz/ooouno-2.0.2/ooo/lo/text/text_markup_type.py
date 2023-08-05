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
# Namespace: com.sun.star.text


class TextMarkupType(object):
    """
    Const Class

    Constants to specify the type of text markup.
    
    These constants are used with XTextMarkup.commitTextMarkup()
    
    **since**
    
        OOo 2.3

    See Also:
        `API TextMarkupType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1TextMarkupType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextMarkupType'
    __ooo_type_name__: str = 'const'

    SPELLCHECK = 1
    """
    Markup originates from spell checking.
    """
    PROOFREADING = 2
    """
    Markup originates from proofreading.
    
    **since**
    
        OOo 3.0.1
    """
    SMARTTAG = 3
    """
    Markup originates from smart tag checking.
    """
    SENTENCE = 4
    """
    Markup originates from proofreading An invisible markup type used in proofreading API calls.
    
    **since**
    
        OOo 3.0.1
    """
    TRACK_CHANGE_INSERTION = 5
    """
    Markups originates from change tracking.
    
    **since**
    
        OOo 3.3
    """
    TRACK_CHANGE_DELETION = 6
    TRACK_CHANGE_FORMATCHANGE = 7

__all__ = ['TextMarkupType']
