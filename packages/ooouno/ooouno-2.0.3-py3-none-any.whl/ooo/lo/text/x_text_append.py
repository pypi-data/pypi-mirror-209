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
# Namespace: com.sun.star.text
from .x_paragraph_append import XParagraphAppend as XParagraphAppend_e2930d13
from .x_text import XText as XText_690408ca
from .x_text_portion_append import XTextPortionAppend as XTextPortionAppend_170e0d

class XTextAppend(XParagraphAppend_e2930d13, XText_690408ca, XTextPortionAppend_170e0d):
    """
    is a meta-interface for manipulating and inserting text.

    See Also:
        `API XTextAppend <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextAppend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XTextAppend'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XTextAppend'


__all__ = ['XTextAppend']

