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
# Namespace: com.sun.star.registry
from .x_implementation_registration import XImplementationRegistration as XImplementationRegistration_df8c139a

class ImplementationRegistration(XImplementationRegistration_df8c139a):
    """
    Service Class

    is the implementation of the interface XImplementationRegistration.
    
    This service can be used to install or uninstall components (implementations). Further, it is possible to check if all runtime dependencies (needed services) are available to use a specified component.
    
    Guarantees:

    See Also:
        `API ImplementationRegistration <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1registry_1_1ImplementationRegistration.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.registry'
    __ooo_full_ns__: str = 'com.sun.star.registry.ImplementationRegistration'
    __ooo_type_name__: str = 'service'


__all__ = ['ImplementationRegistration']

