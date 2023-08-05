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
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_status_indicator import XStatusIndicator as XStatusIndicator_e2d00d34

class XStatusIndicatorFactory(XInterface_8f010a43):
    """
    provides multiple, probably parallel running, status indicator objects
    
    A possible factory is the com.sun.star.frame.Frame service.

    See Also:
        `API XStatusIndicatorFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XStatusIndicatorFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XStatusIndicatorFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XStatusIndicatorFactory'

    @abstractmethod
    def createStatusIndicator(self) -> 'XStatusIndicator_e2d00d34':
        """
        create a new status indicator instance
        """
        ...

__all__ = ['XStatusIndicatorFactory']

