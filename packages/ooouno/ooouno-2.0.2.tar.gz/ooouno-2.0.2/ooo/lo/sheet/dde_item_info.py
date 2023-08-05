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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class DDEItemInfo(object):
    """
    Struct Class

    describes an item of a DDE connection.
    
    A DDE connection consists of the DDE service name, the DDE topic and a list of DDE items which may contain cached result sets.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DDEItemInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DDEItemInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DDEItemInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DDEItemInfo'
    """Literal Constant ``com.sun.star.sheet.DDEItemInfo``"""

    def __init__(self, Results: typing.Optional[typing.Tuple[typing.Tuple[object, ...], ...]] = (), Item: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Results (typing.Tuple[typing.Tuple[object, ...], ...], optional): Results value.
            Item (str, optional): Item value.
        """
        super().__init__()

        if isinstance(Results, DDEItemInfo):
            oth: DDEItemInfo = Results
            self.Results = oth.Results
            self.Item = oth.Item
            return

        kargs = {
            "Results": Results,
            "Item": Item,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._results = kwargs["Results"]
        self._item = kwargs["Item"]


    @property
    def Results(self) -> typing.Tuple[typing.Tuple[object, ...], ...]:
        """
        The results of the item cached from the last update of the DDE link if available.
        
        This sequence may be empty.
        """
        return self._results

    @Results.setter
    def Results(self, value: typing.Tuple[typing.Tuple[object, ...], ...]) -> None:
        self._results = value

    @property
    def Item(self) -> str:
        """
        The name of the DDE item.
        """
        return self._item

    @Item.setter
    def Item(self, value: str) -> None:
        self._item = value


__all__ = ['DDEItemInfo']
