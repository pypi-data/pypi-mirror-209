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
# Namespace: com.sun.star.formula
from ..accessibility.x_accessible import XAccessible as XAccessible_1cbc0eb6
from ..accessibility.x_accessible_component import XAccessibleComponent as XAccessibleComponent_b2f21269
from ..accessibility.x_accessible_context import XAccessibleContext as XAccessibleContext_8eae119b
from ..accessibility.x_accessible_event_broadcaster import XAccessibleEventBroadcaster as XAccessibleEventBroadcaster_3d811522
from ..accessibility.x_accessible_text import XAccessibleText as XAccessibleText_5b77105b

class AccessibleFormulaView(XAccessible_1cbc0eb6, XAccessibleComponent_b2f21269, XAccessibleContext_8eae119b, XAccessibleEventBroadcaster_3d811522, XAccessibleText_5b77105b):
    """
    Service Class

    The accessible view of a formula documents visual representation.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleFormulaView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1formula_1_1AccessibleFormulaView.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.formula'
    __ooo_full_ns__: str = 'com.sun.star.formula.AccessibleFormulaView'
    __ooo_type_name__: str = 'service'


__all__ = ['AccessibleFormulaView']

