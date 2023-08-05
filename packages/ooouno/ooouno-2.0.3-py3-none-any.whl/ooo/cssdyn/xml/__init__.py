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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.xml.attribute import Attribute as Attribute
with suppress(ImportError):
    from ...dyn.xml.attribute_container import AttributeContainer as AttributeContainer
with suppress(ImportError):
    from ...dyn.xml.attribute_data import AttributeData as AttributeData
with suppress(ImportError):
    from ...dyn.xml.export_filter import ExportFilter as ExportFilter
with suppress(ImportError):
    from ...dyn.xml.fast_attribute import FastAttribute as FastAttribute
with suppress(ImportError):
    from ...dyn.xml.import_filter import ImportFilter as ImportFilter
with suppress(ImportError):
    from ...dyn.xml.namespace_container import NamespaceContainer as NamespaceContainer
with suppress(ImportError):
    from ...dyn.xml.para_user_defined_attributes_supplier import ParaUserDefinedAttributesSupplier as ParaUserDefinedAttributesSupplier
with suppress(ImportError):
    from ...dyn.xml.text_user_defined_attributes_supplier import TextUserDefinedAttributesSupplier as TextUserDefinedAttributesSupplier
with suppress(ImportError):
    from ...dyn.xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier
with suppress(ImportError):
    from ...dyn.xml.x_export_filter import XExportFilter as XExportFilter
with suppress(ImportError):
    from ...dyn.xml.x_import_filter import XImportFilter as XImportFilter
with suppress(ImportError):
    from ...dyn.xml.x_import_filter2 import XImportFilter2 as XImportFilter2
with suppress(ImportError):
    from ...dyn.xml.xml_export_filter import XMLExportFilter as XMLExportFilter
with suppress(ImportError):
    from ...dyn.xml.xml_import_filter import XMLImportFilter as XMLImportFilter
