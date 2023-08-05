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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .range_selection_event import RangeSelectionEvent as RangeSelectionEvent_1a2b0eb6

class XRangeSelectionChangeListener(XEventListener_c7230c4a):
    """
    allows notification when the selected range is changed.

    See Also:
        `API XRangeSelectionChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XRangeSelectionChangeListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XRangeSelectionChangeListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XRangeSelectionChangeListener'

    @abstractmethod
    def descriptorChanged(self, aEvent: 'RangeSelectionEvent_1a2b0eb6') -> None:
        """
        is called when the selected range is changed while range selection is active.
        """
        ...

__all__ = ['XRangeSelectionChangeListener']

