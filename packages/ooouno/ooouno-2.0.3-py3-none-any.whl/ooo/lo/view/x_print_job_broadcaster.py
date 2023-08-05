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
    from .x_print_job_listener import XPrintJobListener as XPrintJobListener_efd10d89

class XPrintJobBroadcaster(XInterface_8f010a43):
    """
    allows for getting information about a print job.
    
    XPrintJobBroadcaster can be implemented by classes which implement XPrintable. It allows a XPrintJobListener to be registered, thus a client object will learn about the print progress.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XPrintJobBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XPrintJobBroadcaster.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.XPrintJobBroadcaster'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.view.XPrintJobBroadcaster'

    @abstractmethod
    def addPrintJobListener(self, xListener: 'XPrintJobListener_efd10d89') -> None:
        """
        adds an XPrintJobListener to be notified about print progress.
        """
        ...
    @abstractmethod
    def removePrintJobListener(self, xListener: 'XPrintJobListener_efd10d89') -> None:
        """
        removes an XPrintJobListener.
        """
        ...

__all__ = ['XPrintJobBroadcaster']

