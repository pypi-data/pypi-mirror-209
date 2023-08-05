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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from .x_accessible_component import XAccessibleComponent as XAccessibleComponent_b2f21269
if typing.TYPE_CHECKING:
    from ..awt.x_font import XFont as XFont_5f480843

class XAccessibleExtendedComponent(XAccessibleComponent_b2f21269):
    """
    The XAccessibleExtendedComponent interface contains additional methods to those of the XAccessibleComponent interface.
    
    These methods provide information that is used not as often. The division into two interfaces allows classes to support the more frequently used methods of the XAccessibleComponent interface and only support the XAccessibleExtendedComponent interface if that makes sense for the class.
    
    This interface provides extended access to retrieve information concerning the graphical representation of an object. This interface combines methods from the Java interfaces javax.accessibility.AccessibleComponent and javax.accessibility.AccessibleExtendedComponent.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleExtendedComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleExtendedComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleExtendedComponent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleExtendedComponent'

    @abstractmethod
    def getFont(self) -> 'XFont_5f480843':
        """
        Returns the font of this object.
        """
        ...
    @abstractmethod
    def getTitledBorderText(self) -> str:
        """
        Returns the titled border text.
        
        This method stems from the Java interface AccessibleExtendedComponent.
        """
        ...
    @abstractmethod
    def getToolTipText(self) -> str:
        """
        Returns the tool tip text of this object.
        
        This method stems from the Java interface AccessibleExtendedComponent.
        """
        ...

__all__ = ['XAccessibleExtendedComponent']

