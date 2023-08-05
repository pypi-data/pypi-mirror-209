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
# Namespace: com.sun.star.reflection
from ..container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess_9e2611b5
from ..container.x_set import XSet as XSet_90c40a4f
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_type_description_enumeration_access import XTypeDescriptionEnumerationAccess as XTypeDescriptionEnumerationAccess_8417168a

class TypeDescriptionManager(XHierarchicalNameAccess_9e2611b5, XSet_90c40a4f, XComponent_98dc0ab5, XTypeDescriptionEnumerationAccess_8417168a):
    """
    Service Class

    This service manages type descriptions and acts as a central access point to every type description.
    
    It delegates calls for demanded types to subsequent com.sun.star.reflection.TypeDescriptionProviders and may cache type descriptions.Using cppuhelper's bootstrapping routines bootstrapping an initial component context, there is a singleton accessible via key \"/singletons/com.sun.star.reflection.theTypeDescriptionManager\". This singleton object is hooked into the C UNO runtime typelib and lives until the context is shut down.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TypeDescriptionManager <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1TypeDescriptionManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.TypeDescriptionManager'
    __ooo_type_name__: str = 'service'


__all__ = ['TypeDescriptionManager']

