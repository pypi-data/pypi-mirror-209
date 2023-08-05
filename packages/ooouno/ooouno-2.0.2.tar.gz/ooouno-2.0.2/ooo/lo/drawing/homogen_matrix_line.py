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


class HomogenMatrixLine(object):
    """
    Struct Class

    specifies a single line for a HomogenMatrix.

    See Also:
        `API HomogenMatrixLine <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrixLine.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.HomogenMatrixLine'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.HomogenMatrixLine'
    """Literal Constant ``com.sun.star.drawing.HomogenMatrixLine``"""

    def __init__(self, Column1: typing.Optional[float] = 0.0, Column2: typing.Optional[float] = 0.0, Column3: typing.Optional[float] = 0.0, Column4: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Column1 (float, optional): Column1 value.
            Column2 (float, optional): Column2 value.
            Column3 (float, optional): Column3 value.
            Column4 (float, optional): Column4 value.
        """
        super().__init__()

        if isinstance(Column1, HomogenMatrixLine):
            oth: HomogenMatrixLine = Column1
            self.Column1 = oth.Column1
            self.Column2 = oth.Column2
            self.Column3 = oth.Column3
            self.Column4 = oth.Column4
            return

        kargs = {
            "Column1": Column1,
            "Column2": Column2,
            "Column3": Column3,
            "Column4": Column4,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._column1 = kwargs["Column1"]
        self._column2 = kwargs["Column2"]
        self._column3 = kwargs["Column3"]
        self._column4 = kwargs["Column4"]


    @property
    def Column1(self) -> float:
        return self._column1

    @Column1.setter
    def Column1(self, value: float) -> None:
        self._column1 = value

    @property
    def Column2(self) -> float:
        return self._column2

    @Column2.setter
    def Column2(self, value: float) -> None:
        self._column2 = value

    @property
    def Column3(self) -> float:
        return self._column3

    @Column3.setter
    def Column3(self, value: float) -> None:
        self._column3 = value

    @property
    def Column4(self) -> float:
        return self._column4

    @Column4.setter
    def Column4(self, value: float) -> None:
        self._column4 = value


__all__ = ['HomogenMatrixLine']
