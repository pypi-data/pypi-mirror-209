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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Command(object):
    """
    Struct Class

    contains a command.

    See Also:
        `API Command <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Command.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.Command'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.Command'
    """Literal Constant ``com.sun.star.ucb.Command``"""

    def __init__(self, Name: typing.Optional[str] = '', Handle: typing.Optional[int] = 0, Argument: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            Argument (object, optional): Argument value.
        """
        super().__init__()

        if isinstance(Name, Command):
            oth: Command = Name
            self.Name = oth.Name
            self.Handle = oth.Handle
            self.Argument = oth.Argument
            return

        kargs = {
            "Name": Name,
            "Handle": Handle,
            "Argument": Argument,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._handle = kwargs["Handle"]
        self._argument = kwargs["Argument"]


    @property
    def Name(self) -> str:
        """
        contains the name of the command.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Handle(self) -> int:
        """
        contains an implementation specific handle for the command.
        
        It must be -1 if the implementation has no handle. 0 is a valid command handle.
        """
        return self._handle

    @Handle.setter
    def Handle(self, value: int) -> None:
        self._handle = value

    @property
    def Argument(self) -> object:
        """
        contains the argument of the command
        """
        return self._argument

    @Argument.setter
    def Argument(self, value: object) -> None:
        self._argument = value


__all__ = ['Command']
