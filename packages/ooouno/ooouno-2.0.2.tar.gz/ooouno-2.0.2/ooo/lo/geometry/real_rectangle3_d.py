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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class RealRectangle3D(object):
    """
    Struct Class

    This structure contains the necessary information for a three-dimensional cube.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealRectangle3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealRectangle3D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.RealRectangle3D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.RealRectangle3D'
    """Literal Constant ``com.sun.star.geometry.RealRectangle3D``"""

    def __init__(self, X1: typing.Optional[float] = 0.0, Y1: typing.Optional[float] = 0.0, Z1: typing.Optional[float] = 0.0, X2: typing.Optional[float] = 0.0, Y2: typing.Optional[float] = 0.0, Z2: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            X1 (float, optional): X1 value.
            Y1 (float, optional): Y1 value.
            Z1 (float, optional): Z1 value.
            X2 (float, optional): X2 value.
            Y2 (float, optional): Y2 value.
            Z2 (float, optional): Z2 value.
        """
        super().__init__()

        if isinstance(X1, RealRectangle3D):
            oth: RealRectangle3D = X1
            self.X1 = oth.X1
            self.Y1 = oth.Y1
            self.Z1 = oth.Z1
            self.X2 = oth.X2
            self.Y2 = oth.Y2
            self.Z2 = oth.Z2
            return

        kargs = {
            "X1": X1,
            "Y1": Y1,
            "Z1": Z1,
            "X2": X2,
            "Y2": Y2,
            "Z2": Z2,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._x1 = kwargs["X1"]
        self._y1 = kwargs["Y1"]
        self._z1 = kwargs["Z1"]
        self._x2 = kwargs["X2"]
        self._y2 = kwargs["Y2"]
        self._z2 = kwargs["Z2"]


    @property
    def X1(self) -> float:
        """
        minimum X coordinate.
        """
        return self._x1

    @X1.setter
    def X1(self, value: float) -> None:
        self._x1 = value

    @property
    def Y1(self) -> float:
        """
        minimum Y coordinate.
        """
        return self._y1

    @Y1.setter
    def Y1(self, value: float) -> None:
        self._y1 = value

    @property
    def Z1(self) -> float:
        """
        minimum Z coordinate.
        """
        return self._z1

    @Z1.setter
    def Z1(self, value: float) -> None:
        self._z1 = value

    @property
    def X2(self) -> float:
        """
        maximum X coordinate.
        
        Must be greater than X1 for non-empty cubes.
        
        .
        """
        return self._x2

    @X2.setter
    def X2(self, value: float) -> None:
        self._x2 = value

    @property
    def Y2(self) -> float:
        """
        maximum Y coordinate.
        
        Must be greater than Y1 for non-empty cubes.
        """
        return self._y2

    @Y2.setter
    def Y2(self, value: float) -> None:
        self._y2 = value

    @property
    def Z2(self) -> float:
        """
        maximum Z coordinate.
        
        Must be greater than Z1 for non-empty cubes.
        """
        return self._z2

    @Z2.setter
    def Z2(self, value: float) -> None:
        self._z2 = value


__all__ = ['RealRectangle3D']
