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
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class UnsupportedOpenModeException(Exception_85530a09):
    """
    Exception Class

    This exception is used to indicate that the requested OpenMode is not supported.
    
    For example, each OpenCommandArgument supplied as argument of the command \"open\" contains such an open mode.

    See Also:
        `API UnsupportedOpenModeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1UnsupportedOpenModeException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.UnsupportedOpenModeException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.UnsupportedOpenModeException'
    __pyunostruct__: str = 'com.sun.star.ucb.UnsupportedOpenModeException'

    typeName: str = 'com.sun.star.ucb.UnsupportedOpenModeException'
    """Literal Constant ``com.sun.star.ucb.UnsupportedOpenModeException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Mode: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Mode (int, optional): Mode value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Mode": Mode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mode = kwargs["Mode"]
        inst_keys = ('Mode',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Mode(self) -> int:
        """
        contains the OpenMode that is not supported.
        """
        return self._mode
    
    @Mode.setter
    def Mode(self, value: int) -> None:
        self._mode = value


__all__ = ['UnsupportedOpenModeException']

