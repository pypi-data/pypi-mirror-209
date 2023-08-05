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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .param_mode import ParamMode as ParamMode_d7260ca9
from .x_idl_class import XIdlClass as XIdlClass_d63a0c9a


class ParamInfo(object):
    """
    Struct Class

    Provides information about a formal parameter of a method.

    See Also:
        `API ParamInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1reflection_1_1ParamInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.ParamInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.reflection.ParamInfo'
    """Literal Constant ``com.sun.star.reflection.ParamInfo``"""

    def __init__(self, aName: typing.Optional[str] = '', aMode: typing.Optional[ParamMode_d7260ca9] = ParamMode_d7260ca9.IN, aType: typing.Optional[XIdlClass_d63a0c9a] = None) -> None:
        """
        Constructor

        Arguments:
            aName (str, optional): aName value.
            aMode (ParamMode, optional): aMode value.
            aType (XIdlClass, optional): aType value.
        """
        super().__init__()

        if isinstance(aName, ParamInfo):
            oth: ParamInfo = aName
            self.aName = oth.aName
            self.aMode = oth.aMode
            self.aType = oth.aType
            return

        kargs = {
            "aName": aName,
            "aMode": aMode,
            "aType": aType,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._a_name = kwargs["aName"]
        self._a_mode = kwargs["aMode"]
        self._a_type = kwargs["aType"]


    @property
    def aName(self) -> str:
        """
        name of the parameter
        """
        return self._a_name

    @aName.setter
    def aName(self, value: str) -> None:
        self._a_name = value

    @property
    def aMode(self) -> ParamMode_d7260ca9:
        """
        parameter mode: in, out, inout
        """
        return self._a_mode

    @aMode.setter
    def aMode(self, value: ParamMode_d7260ca9) -> None:
        self._a_mode = value

    @property
    def aType(self) -> XIdlClass_d63a0c9a:
        """
        formal type of the parameter
        """
        return self._a_type

    @aType.setter
    def aType(self, value: XIdlClass_d63a0c9a) -> None:
        self._a_type = value


__all__ = ['ParamInfo']
