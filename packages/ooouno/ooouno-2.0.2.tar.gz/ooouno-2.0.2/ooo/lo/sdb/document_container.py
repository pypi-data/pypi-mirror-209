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
# Namespace: com.sun.star.sdb
from ..container.x_hierarchical_name_container import XHierarchicalNameContainer as XHierarchicalNameContainer_d6621306
from ..frame.x_component_loader import XComponentLoader as XComponentLoader_eede0d75
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from .definition_container import DefinitionContainer as DefinitionContainer_fc1e0ded
from .definition_content import DefinitionContent as DefinitionContent_e0d20d25

class DocumentContainer(DefinitionContainer_fc1e0ded, DefinitionContent_e0d20d25, XHierarchicalNameContainer_d6621306, XComponentLoader_eede0d75, XMultiServiceFactory_191e0eb6):
    """
    Service Class

    describes a container which provides access to documents embedded into a database document, usually forms and reports.
    
    The com.sun.star.lang.XMultiServiceFactory.createInstanceWithArguments() should be used to create sub document container or form, or report objects.
    
    The embedded documents do not support any particular database related service, instead, they're usual com.sun.star.document.OfficeDocuments.The only thing worth mentioning here is that they support the com.sun.star.container.XChild interface, whose com.sun.star.container.XChild.getParent() method can be used to obtain the database document which the embedded document belongs to.

    See Also:
        `API DocumentContainer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DocumentContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DocumentContainer'
    __ooo_type_name__: str = 'service'


__all__ = ['DocumentContainer']

