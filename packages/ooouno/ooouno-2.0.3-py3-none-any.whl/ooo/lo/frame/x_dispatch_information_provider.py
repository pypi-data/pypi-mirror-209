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
# Namespace: com.sun.star.frame
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .dispatch_information import DispatchInformation as DispatchInformation_1a290ec9

class XDispatchInformationProvider(XInterface_8f010a43):
    """
    provides information about supported commands
    
    This interface can be used to retrieve additional information about supported commands. This interface is normally used by configuration implementations to retrieve all supported commands. A dispatch information provider is normally supported by a Frame service.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XDispatchInformationProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatchInformationProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDispatchInformationProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDispatchInformationProvider'

    @abstractmethod
    def getConfigurableDispatchInformation(self, CommandGroup: int) -> 'typing.Tuple[DispatchInformation_1a290ec9, ...]':
        """
        returns additional information about supported commands of a given command group.
        """
        ...
    @abstractmethod
    def getSupportedCommandGroups(self) -> uno.ByteSequence:
        """
        returns all supported command groups.
        """
        ...

__all__ = ['XDispatchInformationProvider']

