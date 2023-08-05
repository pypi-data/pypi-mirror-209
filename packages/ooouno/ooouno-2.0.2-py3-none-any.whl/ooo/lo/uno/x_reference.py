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
# Namespace: com.sun.star.uno
from abc import abstractmethod
from .x_interface import XInterface as XInterface_8f010a43

class XReference(XInterface_8f010a43):
    """
    must be implemented by anyone who holds the adapter on the client side.

    See Also:
        `API XReference <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XReference.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.XReference'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uno.XReference'

    @abstractmethod
    def dispose(self) -> None:
        """
        removes all references to the adapter.
        
        This method is called when the adapted object dies. The implementation of the client-side's weak reference must include removal of all references to the adapter. Otherwise, the adapted object will be destroyed, but the adapter will be alive.
        """
        ...

__all__ = ['XReference']

