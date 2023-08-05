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
# Namespace: com.sun.star.sdbcx
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class Descriptor(XPropertySet_bc180bfa):
    """
    Service Class

    is used to create a new object within a database.
    
    A descriptor is commonly created by the container of a specific object, such as, tables or views. After the creation of the descriptor the properties have to be filled. Afterwards, you append the descriptor to the container and the container creates a new object based on the information of the descriptor. The descriptor can be used to create several objects.
    
    A descriptor contains at least the information of the name of an object.

    See Also:
        `API Descriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Descriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Descriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Name(self) -> str:
        """
        is the name for the object to create.
        """
        ...


__all__ = ['Descriptor']

