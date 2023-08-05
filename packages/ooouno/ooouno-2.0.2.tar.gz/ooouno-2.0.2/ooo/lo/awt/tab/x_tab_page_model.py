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
# Namespace: com.sun.star.awt.tab
from abc import abstractproperty, ABC

class XTabPageModel(ABC):
    """
    specifies an XTabPageModel interface.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XTabPageModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tab_1_1XTabPageModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tab'
    __ooo_full_ns__: str = 'com.sun.star.awt.tab.XTabPageModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tab.XTabPageModel'

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether a tab page is enabled or disabled.
        """
        ...

    @abstractproperty
    def ImageURL(self) -> str:
        """
        specifies a URL that references a graphic that should be displayed in the tab bar.
        """
        ...

    @abstractproperty
    def TabPageID(self) -> int:
        """
        ID for tab page.
        """
        ...

    @abstractproperty
    def Title(self) -> str:
        """
        specifies the text that is displayed in the tab bar of the tab page.
        """
        ...

    @abstractproperty
    def ToolTip(self) -> str:
        """
        specifies a tooltip text that should be displayed in the tab bar.
        """
        ...


__all__ = ['XTabPageModel']

