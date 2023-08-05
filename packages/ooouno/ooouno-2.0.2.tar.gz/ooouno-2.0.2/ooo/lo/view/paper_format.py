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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 7.4
from enum import Enum


class PaperFormat(Enum):
    """
    Enum Class


    See Also:
        `API PaperFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#a12ab04987d08416f8347a9790c7abf3e>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.PaperFormat'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.view.PaperFormat'

    A3 = 'A3'
    """
    specifies the paper format as A3.
    """
    A4 = 'A4'
    """
    specifies the paper format as A4.
    """
    A5 = 'A5'
    """
    specifies the paper format as A5.
    """
    B4 = 'B4'
    """
    specifies the paper format as B4.
    """
    B5 = 'B5'
    """
    specifies the paper format as B5.
    """
    LEGAL = 'LEGAL'
    """
    specifies the paper format as Legal.
    """
    LETTER = 'LETTER'
    """
    specifies the paper format as Letter.
    """
    TABLOID = 'TABLOID'
    """
    specifies the paper format as Tabloid.
    """
    USER = 'USER'
    """
    The real paper size is user defined in 100th mm.
    """

__all__ = ['PaperFormat']

