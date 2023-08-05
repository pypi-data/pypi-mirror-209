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
# Namespace: com.sun.star.reflection
import typing
from abc import abstractmethod
from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1

class XCompoundTypeDescription(XTypeDescription_3c210fb1):
    """
    Reflects a compound type, i.e.
    
    a struct or exception.
    
    For struct types, this type is superseded by XStructTypeDescription, which supports polymorphic struct types.

    See Also:
        `API XCompoundTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XCompoundTypeDescription.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.XCompoundTypeDescription'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.reflection.XCompoundTypeDescription'

    @abstractmethod
    def getBaseType(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the type of the base type of the compound type.
        
        If the compound does not have a base type, the method returns a null interface.
        """
        ...
    @abstractmethod
    def getMemberNames(self) -> 'typing.Tuple[str, ...]':
        """
        Returns the member names of the struct/exception in IDL declaration order.
        """
        ...
    @abstractmethod
    def getMemberTypes(self) -> 'typing.Tuple[XTypeDescription_3c210fb1, ...]':
        """
        Returns the member types of the struct/exception in IDL declaration order.
        
        For a polymorphic struct type template, a member of parameterized type is represented by an instance of com.sun.star.reflection.XTypeDescription whose type class is UNKNOWN and whose name is the name of the type parameter.
        """
        ...

__all__ = ['XCompoundTypeDescription']

