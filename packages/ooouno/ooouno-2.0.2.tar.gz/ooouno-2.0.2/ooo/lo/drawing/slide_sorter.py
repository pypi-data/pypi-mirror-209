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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing
import typing
from abc import abstractmethod
from .x_slide_sorter_base import XSlideSorterBase as XSlideSorterBase_c400e37
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..frame.x_controller import XController as XController_b00e0b8f

class SlideSorter(XSlideSorterBase_c400e37):
    """
    Service Class

    A slide sorter shows previews for a set of slides, typically all slides in a document, and allows the selection, reordering, creation, and deletion of slides.
    
    In the drawing framework a slide sorter is regarded as a view.

    See Also:
        `API SlideSorter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1SlideSorter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.SlideSorter'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, xViewId: object, xController: 'XController_b00e0b8f', xParentWindow: 'XWindow_713b0924') -> None:
        """
        Create a new slide sorter object.
        """
        ...

__all__ = ['SlideSorter']

