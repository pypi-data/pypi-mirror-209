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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class AuthenticationRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    An error specifying lack of correct authentication data (e.g., to log into an account).

    See Also:
        `API AuthenticationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1AuthenticationRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.AuthenticationRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.AuthenticationRequest'
    __pyunostruct__: str = 'com.sun.star.ucb.AuthenticationRequest'

    typeName: str = 'com.sun.star.ucb.AuthenticationRequest'
    """Literal Constant ``com.sun.star.ucb.AuthenticationRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, ServerName: typing.Optional[str] = '', Diagnostic: typing.Optional[str] = '', HasRealm: typing.Optional[bool] = False, Realm: typing.Optional[str] = '', HasUserName: typing.Optional[bool] = False, UserName: typing.Optional[str] = '', HasPassword: typing.Optional[bool] = False, Password: typing.Optional[str] = '', HasAccount: typing.Optional[bool] = False, Account: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            ServerName (str, optional): ServerName value.
            Diagnostic (str, optional): Diagnostic value.
            HasRealm (bool, optional): HasRealm value.
            Realm (str, optional): Realm value.
            HasUserName (bool, optional): HasUserName value.
            UserName (str, optional): UserName value.
            HasPassword (bool, optional): HasPassword value.
            Password (str, optional): Password value.
            HasAccount (bool, optional): HasAccount value.
            Account (str, optional): Account value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "ServerName": ServerName,
            "Diagnostic": Diagnostic,
            "HasRealm": HasRealm,
            "Realm": Realm,
            "HasUserName": HasUserName,
            "UserName": UserName,
            "HasPassword": HasPassword,
            "Password": Password,
            "HasAccount": HasAccount,
            "Account": Account,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._server_name = kwargs["ServerName"]
        self._diagnostic = kwargs["Diagnostic"]
        self._has_realm = kwargs["HasRealm"]
        self._realm = kwargs["Realm"]
        self._has_user_name = kwargs["HasUserName"]
        self._user_name = kwargs["UserName"]
        self._has_password = kwargs["HasPassword"]
        self._password = kwargs["Password"]
        self._has_account = kwargs["HasAccount"]
        self._account = kwargs["Account"]
        inst_keys = ('ServerName', 'Diagnostic', 'HasRealm', 'Realm', 'HasUserName', 'UserName', 'HasPassword', 'Password', 'HasAccount', 'Account')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def ServerName(self) -> str:
        """
        The name of the server (if applicable).
        """
        return self._server_name
    
    @ServerName.setter
    def ServerName(self, value: str) -> None:
        self._server_name = value

    @property
    def Diagnostic(self) -> str:
        """
        Any diagnostic message about the failure to log in (if applicable; it will typically be an English phrase or sentence).
        """
        return self._diagnostic
    
    @Diagnostic.setter
    def Diagnostic(self, value: str) -> None:
        self._diagnostic = value

    @property
    def HasRealm(self) -> bool:
        """
        Specifies if the authentication involves a \"realm\" (as can be the case for HTTP).
        """
        return self._has_realm
    
    @HasRealm.setter
    def HasRealm(self, value: bool) -> None:
        self._has_realm = value

    @property
    def Realm(self) -> str:
        """
        Any already specified realm.
        
        If HasRealm is false, this member should be ignored.
        """
        return self._realm
    
    @Realm.setter
    def Realm(self, value: str) -> None:
        self._realm = value

    @property
    def HasUserName(self) -> bool:
        """
        Specifies if the authentication involves a \"user name\" (as is almost always the case).
        """
        return self._has_user_name
    
    @HasUserName.setter
    def HasUserName(self, value: bool) -> None:
        self._has_user_name = value

    @property
    def UserName(self) -> str:
        """
        Any already specified user name.
        
        If HasUserName is false, this member should be ignored.
        """
        return self._user_name
    
    @UserName.setter
    def UserName(self, value: str) -> None:
        self._user_name = value

    @property
    def HasPassword(self) -> bool:
        """
        Specifies if the authentication involves a \"password\" (as is almost always the case).
        """
        return self._has_password
    
    @HasPassword.setter
    def HasPassword(self, value: bool) -> None:
        self._has_password = value

    @property
    def Password(self) -> str:
        """
        Any already specified password.
        
        If HasPassword is false, this member should be ignored.
        """
        return self._password
    
    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value

    @property
    def HasAccount(self) -> bool:
        """
        Specifies if the authentication involves an \"account\" (as can be the case for FTP).
        """
        return self._has_account
    
    @HasAccount.setter
    def HasAccount(self, value: bool) -> None:
        self._has_account = value

    @property
    def Account(self) -> str:
        """
        Any already specified account.
        
        If HasAccount is false, this member should be ignored.
        """
        return self._account
    
    @Account.setter
    def Account(self, value: str) -> None:
        self._account = value


__all__ = ['AuthenticationRequest']

