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
# Namespace: com.sun.star.xml.crypto.sax
import typing
from abc import abstractmethod
from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..security_operation_status import SecurityOperationStatus as SecurityOperationStatus_b66e12b5

class XDecryptionResultListener(XInterface_8f010a43):
    """
    Interface of Decryption Result Listener.
    
    This interface is used to receive the result information of a decryption operation.

    See Also:
        `API XDecryptionResultListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XDecryptionResultListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.sax.XDecryptionResultListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XDecryptionResultListener'

    @abstractmethod
    def decrypted(self, securityId: int, decryptionResult: 'SecurityOperationStatus_b66e12b5') -> None:
        """
        Notifies the decryption result.
        """
        ...

__all__ = ['XDecryptionResultListener']

