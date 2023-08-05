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
# Namespace: com.sun.star.configuration
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XTemplateContainer(XInterface_8f010a43):
    """
    is implemented by objects that contain instances of a named template to provide information about the template.
    
    An implementation will also implement com.sun.star.lang.XSingleServiceFactory, in which case that interface creates instances of the specified template.
    
    If multiple templates are supported, the supported factory interface may be com.sun.star.lang.XMultiServiceFactory, in which case the string returned from XTemplateContainer.getElementTemplateName() can be used as the service name argument.

    See Also:
        `API XTemplateContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1XTemplateContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.XTemplateContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.configuration.XTemplateContainer'

    @abstractmethod
    def getElementTemplateName(self) -> str:
        """
        retrieves the name of the template
        
        If instances of multiple templates are accepted by the container, this is the name of the basic or primary template.
        
        Instances of the template must be created using an appropriate factory.
        """
        ...

__all__ = ['XTemplateContainer']

