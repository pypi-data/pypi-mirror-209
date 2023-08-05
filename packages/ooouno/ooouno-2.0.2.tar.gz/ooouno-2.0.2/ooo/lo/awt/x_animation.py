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
# Namespace: com.sun.star.awt
from abc import abstractmethod, ABC

class XAnimation(ABC):
    """
    allows controlling an animation.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XAnimation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XAnimation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XAnimation'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XAnimation'

    @abstractmethod
    def isAnimationRunning(self) -> bool:
        """
        determines whether the animation is currently running
        """
        ...
    @abstractmethod
    def startAnimation(self) -> None:
        """
        starts the animation
        """
        ...
    @abstractmethod
    def stopAnimation(self) -> None:
        """
        stops the animation
        """
        ...

__all__ = ['XAnimation']

