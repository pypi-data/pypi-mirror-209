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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe

class ActionTrigger(ABC):
    """
    Service Class

    describes a trigger for an (user inter-)action.
    
    Common examples for such triggers are menu entries or toolbar icons.

    See Also:
        `API ActionTrigger <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1ActionTrigger.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ActionTrigger'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CommandURL(self) -> str:
        """
        contains the command URL for the menu entry.
        """
        ...

    @abstractproperty
    def HelpURL(self) -> str:
        """
        contains the a URL that points to a help text.
        """
        ...

    @abstractproperty
    def Image(self) -> 'XBitmap_70cd0909':
        """
        contains the menu item image.
        """
        ...

    @abstractproperty
    def SubContainer(self) -> 'XIndexContainer_1c040ebe':
        """
        contains a sub menu.
        """
        ...

    @abstractproperty
    def Text(self) -> str:
        """
        contains the text of the menu entry.
        """
        ...


__all__ = ['ActionTrigger']

