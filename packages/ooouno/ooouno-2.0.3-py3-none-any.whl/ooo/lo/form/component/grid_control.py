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
# Namespace: com.sun.star.form.component
import typing
from abc import abstractproperty
from ..form_components import FormComponents as FormComponents_c8e60c76
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_grid_column_factory import XGridColumnFactory as XGridColumnFactory_fbb70de0
from ..x_reset import XReset as XReset_71670917
from ...view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15
if typing.TYPE_CHECKING:
    from ...awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ...util.color import Color as Color_68e908c5

class GridControl(FormComponents_c8e60c76, FormControlModel_e2990d22, XGridColumnFactory_fbb70de0, XReset_71670917, XSelectionSupplier_fed20e15):
    """
    Service Class

    specifies a model for a control which can display form data in a table-like way.
    
    In opposite to other form controls, grid controls do not only display the single current value of a column they are bound to. Moreover, they do display not only the current row of the form, but all rows (at least potentially, limited by the control size, of course).
    
    The table rows in a grid control correspond to the rows in the DataForm the control belongs to, and the columns correspond to single columns of the form's row set.
    
    Columns of a grid control are modeled by own objects, too. They are very similar to usual com.sun.star.form.DataAwareControlModels modeling other \"single-value\" controls, but they are not described as own services. Instead, they need to be created using the com.sun.star.form.XGridColumnFactory interface.
    
    **since**
    
        OOo 2.0

    See Also:
        `API GridControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1GridControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.GridControl'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Border(self) -> int:
        """
        returns the border style of the control.
        """
        ...

    @abstractproperty
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @abstractproperty
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        contains the font attributes of the text in the control.
        """
        ...

    @abstractproperty
    def RowHeight(self) -> int:
        """
        specifies the height of a row of the grid.
        
        If the value is set to NULL, the height is determined automatically according to the current font used.
        """
        ...

    @abstractproperty
    def Tabstop(self) -> bool:
        """
        determines whether the control can be reached by the tabulator key.
        """
        ...

    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...


__all__ = ['GridControl']

