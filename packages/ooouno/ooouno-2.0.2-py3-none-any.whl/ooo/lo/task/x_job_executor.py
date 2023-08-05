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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XJobExecutor(XInterface_8f010a43):
    """
    starts action for any triggered event from outside
    
    If somewhere from outside trigger an event on this interface it will be used to find any registered service inside configuration of this executor. If somewhere could be found it will be started and controlled by this instance. After it finish his work it's possible to deactivate further startups or let him run again if a new event will be detected later.

    See Also:
        `API XJobExecutor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XJobExecutor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XJobExecutor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XJobExecutor'

    @abstractmethod
    def trigger(self, Event: str) -> None:
        """
        trigger event to start registered jobs
        
        Jobs are registered in configuration and will be started by executor automatically, if they are registered for triggered event. The meaning of given string Event mustn't be known. Because for the executor it's enough to use it for searching a registered job inside his own configuration. So no special events will be defined here.
        """
        ...

__all__ = ['XJobExecutor']

