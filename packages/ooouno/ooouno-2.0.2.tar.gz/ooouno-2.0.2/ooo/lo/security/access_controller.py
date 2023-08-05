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
# Namespace: com.sun.star.security
from .x_access_controller import XAccessController as XAccessController_2cc60f4e

class AccessController(XAccessController_2cc60f4e):
    """
    Service Class

    This meta service supports the XAccessController interface for checking security permissions.
    
    Also, it obviously has also to be ensured that the object is process-local to assure that permission checks are not corrupted via insecure inter-process communication.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1security_1_1AccessController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.AccessController'
    __ooo_type_name__: str = 'service'


__all__ = ['AccessController']

