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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class EnhancedCustomShapeSegment(object):
    """
    Struct Class


    See Also:
        `API EnhancedCustomShapeSegment <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeSegment.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeSegment'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeSegment'
    """Literal Constant ``com.sun.star.drawing.EnhancedCustomShapeSegment``"""

    def __init__(self, Command: typing.Optional[int] = 0, Count: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Command (int, optional): Command value.
            Count (int, optional): Count value.
        """
        super().__init__()

        if isinstance(Command, EnhancedCustomShapeSegment):
            oth: EnhancedCustomShapeSegment = Command
            self.Command = oth.Command
            self.Count = oth.Count
            return

        kargs = {
            "Command": Command,
            "Count": Count,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._command = kwargs["Command"]
        self._count = kwargs["Count"]


    @property
    def Command(self) -> int:
        return self._command

    @Command.setter
    def Command(self, value: int) -> None:
        self._command = value

    @property
    def Count(self) -> int:
        return self._count

    @Count.setter
    def Count(self, value: int) -> None:
        self._count = value


__all__ = ['EnhancedCustomShapeSegment']
