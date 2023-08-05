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
# Namespace: com.sun.star.animations
from abc import abstractproperty
from .x_animation_node import XAnimationNode as XAnimationNode_1cf10eb9

class XAudio(XAnimationNode_1cf10eb9):
    """
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API XAudio <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAudio.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.XAudio'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.animations.XAudio'

    @abstractproperty
    def HideDuringShow(self) -> bool:
        """
        Specifies if the source shape should be hidden during slideshow (defaults to false).
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @abstractproperty
    def Narration(self) -> bool:
        """
        Specifies if the source shape is a narration for the slide (defaults to false).
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @abstractproperty
    def Source(self) -> object:
        """
        This attribute specifies the source element that contains the audio.
        """
        ...

    @abstractproperty
    def Volume(self) -> float:
        """
        """
        ...


__all__ = ['XAudio']

