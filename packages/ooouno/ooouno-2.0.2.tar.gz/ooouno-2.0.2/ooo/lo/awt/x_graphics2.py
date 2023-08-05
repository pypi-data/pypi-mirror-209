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
import typing
from abc import abstractmethod
from .x_graphics import XGraphics as XGraphics_842309dd
if typing.TYPE_CHECKING:
    from .rectangle import Rectangle as Rectangle_84b109e9
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc

class XGraphics2(XGraphics_842309dd):
    """
    provides the basic output operation of a device.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XGraphics2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XGraphics2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XGraphics2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XGraphics2'

    @abstractmethod
    def clear(self, aRect: 'Rectangle_84b109e9') -> None:
        """
        clears the given rectangle on the device
        
        **since**
        
            LibreOffice 4.1
        """
        ...
    @abstractmethod
    def drawImage(self, nX: int, nY: int, nWidth: int, nHeight: int, nStyle: int, aGraphic: 'XGraphic_a4da0afc') -> None:
        """
        draws a com.sun.star.graphic.XGraphic in the output device.
        
        Note that some devices may not support this operation.
        
        **since**
        
            LibreOffice 4.1
        """
        ...

__all__ = ['XGraphics2']

