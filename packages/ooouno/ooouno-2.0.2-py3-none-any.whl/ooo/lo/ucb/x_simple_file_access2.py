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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from .x_simple_file_access import XSimpleFileAccess as XSimpleFileAccess_dede0cd6
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XSimpleFileAccess2(XSimpleFileAccess_dede0cd6):
    """
    This is an extension to the interface XSimpleFileAccess.

    See Also:
        `API XSimpleFileAccess2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XSimpleFileAccess2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XSimpleFileAccess2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XSimpleFileAccess2'

    @abstractmethod
    def writeFile(self, FileURL: str, data: 'XInputStream_98d40ab4') -> None:
        """
        Overwrites the file content with the given data.
        
        If the file does not exist, it will be created.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XSimpleFileAccess2']

