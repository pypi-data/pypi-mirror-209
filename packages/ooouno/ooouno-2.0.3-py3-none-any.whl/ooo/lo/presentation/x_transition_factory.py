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
# Namespace: com.sun.star.presentation
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_slide_show_view import XSlideShowView as XSlideShowView_3eb40fa9
    from .x_transition import XTransition as XTransition_123a0ea7
    from ..rendering.x_bitmap import XBitmap as XBitmap_b1b70b7b

class XTransitionFactory(XInterface_8f010a43):
    """
    TransitionFactory interface to request optional custom Transition instances for slide show transitions.
    
    This interface provides the necessary methods to query and create optional transition effects for a SlideShow
    
    **since**
    
        OOo 2.4

    See Also:
        `API XTransitionFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XTransitionFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.XTransitionFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.presentation.XTransitionFactory'

    @abstractmethod
    def createTransition(self, transitionType: int, transitionSubType: int, transitionFadeColor: int, view: 'XSlideShowView_3eb40fa9', leavingBitmap: 'XBitmap_b1b70b7b', enteringBitmap: 'XBitmap_b1b70b7b') -> 'XTransition_123a0ea7':
        """
        Actually create a transition for the given transition id.
        """
        ...
    @abstractmethod
    def hasTransition(self, transitionType: int, transitionSubType: int) -> bool:
        """
        Checks whether this instance provides an implementation for given transition id.
        """
        ...

__all__ = ['XTransitionFactory']

