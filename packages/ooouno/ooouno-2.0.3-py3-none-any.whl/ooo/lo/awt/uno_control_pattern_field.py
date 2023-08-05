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
# Namespace: com.sun.star.awt
from .uno_control_edit import UnoControlEdit as UnoControlEdit_bc4e0bed
from .x_pattern_field import XPatternField as XPatternField_afc10b6e
from .x_spin_field import XSpinField as XSpinField_8e3a0a2a

class UnoControlPatternField(UnoControlEdit_bc4e0bed, XPatternField_afc10b6e, XSpinField_8e3a0a2a):
    """
    Service Class

    specifies a pattern field control.
    
    A pattern field makes it possible to enter, display and edit text which conforms to a specified pattern.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API UnoControlPatternField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlPatternField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlPatternField'
    __ooo_type_name__: str = 'service'


__all__ = ['UnoControlPatternField']

