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
# Namespace: com.sun.star.uno
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .x_interface import XInterface as XInterface_8f010a43

class Exception(Exception):
    """
    Exception Class

    the base of all UNO exceptions
    
    All exceptions defined in UNO idl should derive from this exception.

    See Also:
        `API Exception <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1Exception.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.Exception'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.uno.Exception'
    __pyunostruct__: str = 'com.sun.star.uno.Exception'

    typeName: str = 'com.sun.star.uno.Exception'
    """Literal Constant ``com.sun.star.uno.Exception``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        super().__init__()
        kargs = {
            "Message": Message,
            "Context": Context,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._message = kwargs["Message"]
        self._context = kwargs["Context"]

    @property
    def Message(self) -> str:
        """
        gives a detailed description of the reason, why the exception was thrown.
        
        The description should be as detailed as possible.
        """
        return self._message
    
    @Message.setter
    def Message(self, value: str) -> None:
        self._message = value

    @property
    def Context(self) -> XInterface_8f010a43:
        """
        should contain a reference to the original, which raised the exception.
        
        May be NULL.
        """
        return self._context
    
    @Context.setter
    def Context(self, value: XInterface_8f010a43) -> None:
        self._context = value


__all__ = ['Exception']

