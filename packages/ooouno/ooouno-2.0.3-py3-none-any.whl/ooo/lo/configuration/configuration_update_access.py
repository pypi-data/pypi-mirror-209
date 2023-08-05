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
# Namespace: com.sun.star.configuration
from .configuration_access import ConfigurationAccess as ConfigurationAccess_a5d4122a
from .group_update import GroupUpdate as GroupUpdate_20340ef0
from .set_update import SetUpdate as SetUpdate_2530e0f
from .update_root_element import UpdateRootElement as UpdateRootElement_814f1151

class ConfigurationUpdateAccess(ConfigurationAccess_a5d4122a, GroupUpdate_20340ef0, SetUpdate_2530e0f, UpdateRootElement_814f1151):
    """
    Service Class

    provides modifying access to a fragment of the configuration hierarchy.
    
    Extends ConfigurationAccess to support modifying values or inserting and removing elements.
    
    Descendants of this service also implement this service unless they are marked read-only (which is indicated by attribute com.sun.star.beans.PropertyAttribute.READONLY), in which case they only need implement ConfigurationAccess.
    
    The classification of implementations that is described for ConfigurationAccess applies to implementations of this service as well. Therefore an implementation will support one of several alternate services describing its Container role and one of several alternate services describing its Element role. These services are extensions of the respective services documented for ConfigurationAccess.

    See Also:
        `API ConfigurationUpdateAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1ConfigurationUpdateAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.ConfigurationUpdateAccess'
    __ooo_type_name__: str = 'service'


__all__ = ['ConfigurationUpdateAccess']

