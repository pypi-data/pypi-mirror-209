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
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod, abstractproperty
from ...lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ...awt.x_window import XWindow as XWindow_713b0924

class XWizardPage(XComponent_98dc0ab5):
    """
    is a single page of a Wizard
    
    **since**
    
        OOo 3.3

    See Also:
        `API XWizardPage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XWizardPage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XWizardPage'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XWizardPage'

    @abstractmethod
    def activatePage(self) -> None:
        """
        called when the page is activated
        """
        ...
    @abstractmethod
    def canAdvance(self) -> bool:
        """
        determines whether it is allowed to travel to a later page in the wizard
        
        You should base this decision on the state of the page only, not on a global state of the wizard. Usually, you return FALSE here if and only if not all necessary input on the page has been provided by the user, or the provided input is not valid.
        
        If checked for validity is expensive, or if you prefer giving your user more detailed feedback on validity than a disabled Next button in the wizard, then move your checks to the commitPage() method.
        """
        ...
    @abstractmethod
    def commitPage(self, Reason: int) -> bool:
        """
        is called when the page is about to be left
        
        An implementation can veto the leave by returning FALSE here. Usually, the decision about this depends on the current state of the page.
        """
        ...
    @abstractproperty
    def PageId(self) -> int:
        """
        denotes the ID of the page.
        
        Within a wizard, no two pages are allowed to have the same ID.
        """
        ...

    @abstractproperty
    def Window(self) -> 'XWindow_713b0924':
        """
        provides read-only access to the window of the page
        """
        ...


__all__ = ['XWizardPage']

