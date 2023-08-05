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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ItemEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event occurred to an item of a menu, a list box etc.

    See Also:
        `API ItemEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ItemEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.ItemEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.ItemEvent'
    """Literal Constant ``com.sun.star.awt.ItemEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Selected: typing.Optional[int] = 0, Highlighted: typing.Optional[int] = 0, ItemId: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Selected (int, optional): Selected value.
            Highlighted (int, optional): Highlighted value.
            ItemId (int, optional): ItemId value.
        """

        if isinstance(Source, ItemEvent):
            oth: ItemEvent = Source
            self.Source = oth.Source
            self.Selected = oth.Selected
            self.Highlighted = oth.Highlighted
            self.ItemId = oth.ItemId
            return

        kargs = {
            "Source": Source,
            "Selected": Selected,
            "Highlighted": Highlighted,
            "ItemId": ItemId,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._selected = kwargs["Selected"]
        self._highlighted = kwargs["Highlighted"]
        self._item_id = kwargs["ItemId"]
        inst_keys = ('Selected', 'Highlighted', 'ItemId')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Selected(self) -> int:
        """
        specifies which item is newly selected.
        """
        return self._selected

    @Selected.setter
    def Selected(self, value: int) -> None:
        self._selected = value

    @property
    def Highlighted(self) -> int:
        """
        specifies which item is newly highlighted.
        """
        return self._highlighted

    @Highlighted.setter
    def Highlighted(self, value: int) -> None:
        self._highlighted = value

    @property
    def ItemId(self) -> int:
        """
        specifies the id of the item.
        """
        return self._item_id

    @ItemId.setter
    def ItemId(self, value: int) -> None:
        self._item_id = value


__all__ = ['ItemEvent']
