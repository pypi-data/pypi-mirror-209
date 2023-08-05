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
# Namespace: com.sun.star.xml
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class AttributeContainer(XNameContainer_cb90e47):
    """
    Service Class

    This service describes a container for XML attributes.
    
    Each attribute is accessed with its local name, or optionally, its local name with its namespace prefix. The type and value of an attribute is stored in a AttributeData struct. If you use a namespace in the AttributeData, you must use a prefix in the name and you must use a namespace, if you use a prefix.

    See Also:
        `API AttributeContainer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1AttributeContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.AttributeContainer'
    __ooo_type_name__: str = 'service'


__all__ = ['AttributeContainer']

