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
# Namespace: com.sun.star.text.textfield
from abc import abstractproperty
from ..dependent_text_field import DependentTextField as DependentTextField_fed90ded

class Database(DependentTextField_fed90ded):
    """
    Service Class

    specifies service of a database text field which is used as mail merge field.

    See Also:
        `API Database <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1Database.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.Database'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Content(self) -> str:
        """
        contains the database content that was merged in the last database merge action.
        
        Initially it contains the column name in parenthesis (<>).
        """
        ...

    @abstractproperty
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is especially useful for import/export purposes.
        """
        ...

    @abstractproperty
    def DataBaseFormat(self) -> bool:
        """
        determines whether the number format is number display format is read from the database settings.
        """
        ...

    @abstractproperty
    def NumberFormat(self) -> int:
        """
        this is the number format for this field.
        """
        ...


__all__ = ['Database']

