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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.task
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .document_ms_password_request import DocumentMSPasswordRequest as DocumentMSPasswordRequest_69f810d6
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from .password_request_mode import PasswordRequestMode as PasswordRequestMode_ec10e7c

class DocumentMSPasswordRequest2(DocumentMSPasswordRequest_69f810d6):
    """
    Exception Class

    this request specifies if a password for opening or modifying of an encrypted Microsoft Office document is requested.
    
    It is supported by InteractionHandler service, and can be used to interact for a document password. Continuations for using with the mentioned service are Abort and Approve.
    
    **since**
    
        OOo 3.3

    See Also:
        `API DocumentMSPasswordRequest2 <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentMSPasswordRequest2.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.DocumentMSPasswordRequest2'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.DocumentMSPasswordRequest2'
    __pyunostruct__: str = 'com.sun.star.task.DocumentMSPasswordRequest2'

    typeName: str = 'com.sun.star.task.DocumentMSPasswordRequest2'
    """Literal Constant ``com.sun.star.task.DocumentMSPasswordRequest2``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Mode: typing.Optional[PasswordRequestMode_ec10e7c] = PasswordRequestMode_ec10e7c.PASSWORD_CREATE, Name: typing.Optional[str] = '', IsRequestPasswordToModify: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Mode (PasswordRequestMode, optional): Mode value.
            Name (str, optional): Name value.
            IsRequestPasswordToModify (bool, optional): IsRequestPasswordToModify value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Mode": Mode,
            "Name": Name,
            "IsRequestPasswordToModify": IsRequestPasswordToModify,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._is_request_password_to_modify = kwargs["IsRequestPasswordToModify"]
        inst_keys = ('IsRequestPasswordToModify',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def IsRequestPasswordToModify(self) -> bool:
        """
        specifies if the requested password is for opening a document or for modifying it.
        """
        return self._is_request_password_to_modify
    
    @IsRequestPasswordToModify.setter
    def IsRequestPasswordToModify(self, value: bool) -> None:
        self._is_request_password_to_modify = value


__all__ = ['DocumentMSPasswordRequest2']

