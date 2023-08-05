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
# Namespace: com.sun.star.sheet
from abc import abstractproperty
from .x_formula_parser import XFormulaParser as XFormulaParser_d54d0cbc

class XFilterFormulaParser(XFormulaParser_d54d0cbc):
    """
    Extends the interface XFormulaParser by an attribute that specifies the namespace URL of the supported formula language.

    See Also:
        `API XFilterFormulaParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XFilterFormulaParser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XFilterFormulaParser'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XFilterFormulaParser'

    @abstractproperty
    def SupportedNamespace(self) -> str:
        """
        Specifies the namespace URL of the formula language supported by this implementation.
        """
        ...


__all__ = ['XFilterFormulaParser']

