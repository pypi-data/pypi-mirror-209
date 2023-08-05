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
# Namespace: com.sun.star.embed
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..datatransfer.data_flavor import DataFlavor as DataFlavor_ffd30deb


class VisualRepresentation(object):
    """
    Struct Class

    can contain a graphical representation in an arbitrary format.

    See Also:
        `API VisualRepresentation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1embed_1_1VisualRepresentation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.VisualRepresentation'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.embed.VisualRepresentation'
    """Literal Constant ``com.sun.star.embed.VisualRepresentation``"""

    def __init__(self, Flavor: typing.Optional[DataFlavor_ffd30deb] = UNO_NONE, Data: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Flavor (DataFlavor, optional): Flavor value.
            Data (object, optional): Data value.
        """
        super().__init__()

        if isinstance(Flavor, VisualRepresentation):
            oth: VisualRepresentation = Flavor
            self.Flavor = oth.Flavor
            self.Data = oth.Data
            return

        kargs = {
            "Flavor": Flavor,
            "Data": Data,
        }
        if kargs["Flavor"] is UNO_NONE:
            kargs["Flavor"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._flavor = kwargs["Flavor"]
        self._data = kwargs["Data"]


    @property
    def Flavor(self) -> DataFlavor_ffd30deb:
        """
        The format of the visual representation.
        """
        return self._flavor

    @Flavor.setter
    def Flavor(self, value: DataFlavor_ffd30deb) -> None:
        self._flavor = value

    @property
    def Data(self) -> object:
        """
        The data in the format specified by Flavor.
        """
        return self._data

    @Data.setter
    def Data(self, value: object) -> None:
        self._data = value


__all__ = ['VisualRepresentation']
