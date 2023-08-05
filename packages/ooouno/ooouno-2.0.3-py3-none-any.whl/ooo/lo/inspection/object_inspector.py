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
# Namespace: com.sun.star.inspection
import typing
from abc import abstractmethod
from .x_object_inspector import XObjectInspector as XObjectInspector_3c860faa
if typing.TYPE_CHECKING:
    from .x_object_inspector_model import XObjectInspectorModel as XObjectInspectorModel_9077119b

class ObjectInspector(XObjectInspector_3c860faa):
    """
    Service Class

    describes a com.sun.star.frame.Controller which can be used to browse and modify properties of components.
    
    The controller can be plugged into a com.sun.star.frame.XFrame, and will provide a visual component for inspecting and modifying component properties.Note that \"property\" here is a generic term - any aspect of a component can be considered a property, as long as some property handler is able to describe this aspect in a property-like way.
    
    The basic idea is that one facet of the inspected component is represented by a single line of controls: A label, an input control, and optionally one or two buttons which, when pressed, trigger additional user interaction (e.g. a more sophisticated dialog to enter a property value).
    
    Additionally, property lines can be grouped into different categories. A usual implementation of such categories would be tab pages, but other implementations are possible, too.
    
    Even more, the inspector can optionally display a help section at the bottom of its window, which can display arbitrary (context-sensitive) help texts.
    
    An ObjectInspector needs one or more property handlers which describe the facets of an inspected component - without such handlers, the inspector window will simply stay empty.
    
    The property handlers, as well as more information about the layout of the inspector, are provided by an inspector model, which has to be implemented by the user of the inspector.
    
    Since property handlers might have the need to raise UI, they will be created with a context value named \"DialogParentWindow\", which contains an XWindow which should be used as parent of any windows to raise.If the com.sun.star.uno.XComponentContext in which the ObjectInspector was created already contains such a value, it is not overwritten. Only if it doesn't, the inspector will add an own value - which contains the inspector's main window - to the context when creating handlers.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API ObjectInspector <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1inspection_1_1ObjectInspector.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.ObjectInspector'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createDefault(self) -> None:
        """
        creates a default instance of the ObjectInspector
        
        **since**
        
            OOo 2.2
        """
        ...
    @abstractmethod
    def createWithModel(self, Model: 'XObjectInspectorModel_9077119b') -> None:
        """
        creates an instance of the ObjectInspector, using a given ObjectInspectorModel
        
        **since**
        
            OOo 2.2

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['ObjectInspector']

