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
# Namespace: com.sun.star.inspection
from .x_property_handler import XPropertyHandler as XPropertyHandler_3e950fbf

class GenericPropertyHandler(XPropertyHandler_3e950fbf):
    """
    Service Class

    implements a general-purpose XPropertyHandler
    
    The property handler implemented by this service will do an introspection on the provided components, and expose the properties obtained via XIntrospectionAccess.getProperties.
    
    The handler will automatically determine the best type of property control to represent a certain property, depending on the property type. This includes, for example, list box controls to represent enumeration properties.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API GenericPropertyHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1inspection_1_1GenericPropertyHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.GenericPropertyHandler'
    __ooo_type_name__: str = 'service'


__all__ = ['GenericPropertyHandler']

