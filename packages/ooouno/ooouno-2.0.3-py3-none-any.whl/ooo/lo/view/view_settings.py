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
# Namespace: com.sun.star.view
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class ViewSettings(XPropertySet_bc180bfa):
    """
    Service Class

    provides access to the settings of the controller of an office document.

    See Also:
        `API ViewSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1view_1_1ViewSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.ViewSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ShowHoriRuler(self) -> bool:
        """
        If this property is TRUE, the horizontal ruler is displayed.
        """
        ...

    @abstractproperty
    def ShowHoriScrollBar(self) -> bool:
        """
        If this property is TRUE, the horizontal scroll bar is displayed.
        """
        ...

    @abstractproperty
    def ShowVertRuler(self) -> bool:
        """
        If this property is TRUE, the vertical ruler is displayed.
        """
        ...

    @abstractproperty
    def ShowVertScrollBar(self) -> bool:
        """
        If this property is TRUE, the vertical scroll bar is displayed.
        """
        ...

    @abstractproperty
    def ZoomValue(self) -> int:
        """
        specifies the zoom-value in percent.
        """
        ...


__all__ = ['ViewSettings']

