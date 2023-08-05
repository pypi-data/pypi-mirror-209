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
# Namespace: com.sun.star.view
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_selection_change_listener import XSelectionChangeListener as XSelectionChangeListener_58bf104d

class XSelectionSupplier(XInterface_8f010a43):
    """
    makes it possible to access and change the selection in a view.

    See Also:
        `API XSelectionSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XSelectionSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.XSelectionSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.view.XSelectionSupplier'

    @abstractmethod
    def addSelectionChangeListener(self, xListener: 'XSelectionChangeListener_58bf104d') -> None:
        """
        registers an event listener, which is called when the selection changes.
        """
        ...
    @abstractmethod
    def getSelection(self) -> object:
        """
        The selection is either specified by an object which is contained in the component to which the view belongs, or it is an interface of a collection which contains such objects.
        """
        ...
    @abstractmethod
    def removeSelectionChangeListener(self, xListener: 'XSelectionChangeListener_58bf104d') -> None:
        """
        unregisters an event listener which was registered with XSelectionSupplier.addSelectionChangeListener().
        """
        ...
    @abstractmethod
    def select(self, xSelection: object) -> bool:
        """
        selects the object represented by xSelection if it is known and selectable in this object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XSelectionSupplier']

