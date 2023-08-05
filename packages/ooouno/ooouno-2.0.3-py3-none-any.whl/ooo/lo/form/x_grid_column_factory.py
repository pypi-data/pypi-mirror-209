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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.form
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XGridColumnFactory(XInterface_8f010a43):
    """
    allows to create columns to be added into a grid control model.
    
    Grid columns (more precise: models of grid columns) are direct children of the grid control model they belong to. Grid columns can't be created on a global service factory, instead, you need to create them on the grid, where you want to insert them later on.

    See Also:
        `API XGridColumnFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XGridColumnFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XGridColumnFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XGridColumnFactory'

    @abstractmethod
    def createColumn(self, aColumnType: str) -> 'XPropertySet_bc180bfa':
        """
        creates a new column object

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getColumnTypes(self) -> 'typing.Tuple[str, ...]':
        """
        returns a list of available column types.
        """
        ...

__all__ = ['XGridColumnFactory']

