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
# Namespace: com.sun.star.text
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .text_content import TextContent as TextContent_a6810b4d
from .x_text_field import XTextField as XTextField_9a630aae

class TextField(TextContent_a6810b4d, XPropertySet_bc180bfa, XTextField_9a630aae):
    """
    Service Class

    A TextField is a TextContent which fades its textual representation into the text range to which it is anchored.
    
    **since**
    
        OOo 2.0.1

    See Also:
        `API TextField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextField'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def IsFieldDisplayed(self) -> bool:
        """
        specifies if the text field is actually displayed.
        
        Not all available text fields are actually displayed even when they are used. For example hidden fields or fields in hidden text are used in the document but get not displayed.
        
        **since**
        
            OOo 2.0.1
        """
        ...

    @abstractproperty
    def IsFieldUsed(self) -> bool:
        """
        specifies if the text field is actually used in the document.
        
        Not all available text fields are used, for example fields that are part of unused styles.
        
        **since**
        
            OOo 2.0.1
        """
        ...

    @abstractproperty
    def Title(self) -> str:
        """
        Contains short title for the field, used to for tooltip purposes if it's non-empty.
        
        **since**
        
            LibreOffice 7.4
        """
        ...


__all__ = ['TextField']

