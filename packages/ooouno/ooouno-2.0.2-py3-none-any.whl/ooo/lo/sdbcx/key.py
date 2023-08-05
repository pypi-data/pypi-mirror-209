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
from .x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from .x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5

class Key(XPropertySet_bc180bfa, XColumnsSupplier_f0600da9, XDataDescriptorFactory_46170fe5):
    """
    Service Class

    is used to define a new key for a table.

    See Also:
        `API Key <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Key.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Key'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DeleteRule(self) -> int:
        """
        is the rule which is applied for deletions; only used for foreign keys.
        """
        ...

    @abstractproperty
    def Name(self) -> str:
        """
        is the name of the key
        """
        ...

    @abstractproperty
    def ReferencedTable(self) -> str:
        """
        is the name of the referenced table, only used for foreign keys.
        """
        ...

    @abstractproperty
    def Type(self) -> int:
        """
        indicates the type of the key.
        """
        ...

    @abstractproperty
    def UpdateRule(self) -> int:
        """
        is the rule which is applied for updates; only used for foreign keys.
        """
        ...


__all__ = ['Key']

