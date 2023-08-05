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
# Namespace: com.sun.star.awt
import typing
from abc import abstractproperty
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5
    from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class UnoControlFormattedFieldModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlFormattedField .
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlFormattedFieldModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlFormattedFieldModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlFormattedFieldModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """
        ...

    @abstractproperty
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """
        ...

    @abstractproperty
    def Border(self) -> int:
        """
        specifies the border style of the control.
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
    def EffectiveDefault(self) -> object:
        """
        specifies the default value of the formatted field.
        
        This may be a numeric value (double) or a string, depending on the formatting of the field.
        """
        ...

    @abstractproperty
    def EffectiveMax(self) -> float:
        """
        specifies the maximum value that can be entered.
        
        This property is ignored if the format of the field is no numeric format.
        """
        ...

    @abstractproperty
    def EffectiveMin(self) -> float:
        """
        specifies the minimum value that can be entered.
        
        This property is ignored if the format of the field is no numeric format.
        """
        ...

    @abstractproperty
    def EffectiveValue(self) -> float:
        """
        specifies the current value of the formatted field.
        
        This may be a numeric value (double) or a string, depending on the formatting of the field.
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
        specifies the font attributes of the text in the control.
        """
        ...

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...

    @abstractproperty
    def FormatKey(self) -> int:
        """
        specifies the format to be used when formatting the field input and output.
        
        This value is meaningful relative to the FormatsSupplier property only.
        """
        ...

    @abstractproperty
    def FormatsSupplier(self) -> 'XNumberFormatsSupplier_3afb0fb7':
        """
        supplies the formats the field should work with.
        """
        ...

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...

    @abstractproperty
    def HideInactiveSelection(self) -> bool:
        """
        specifies whether the selection in the control should be hidden when the control is not active (focused).
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def MaxTextLen(self) -> int:
        """
        specifies the maximum character count.
        
        There's no limitation, if set to 0.
        """
        ...

    @abstractproperty
    def MouseWheelBehavior(self) -> int:
        """
        defines how the mouse wheel can be used to scroll through the control's content.
        
        Usually, the mouse wheel spins the numeric value displayed in the control. Using this property, and one of the MouseWheelBehavior constants, you can control under which circumstances this is possible.
        """
        ...

    @abstractproperty
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...

    @abstractproperty
    def ReadOnly(self) -> bool:
        """
        specifies that the content of the control cannot be modified by the user.
        """
        ...

    @abstractproperty
    def Repeat(self) -> bool:
        """
        specifies whether the mouse should show repeating behavior, i.e.
        
        repeatedly trigger an action when keeping pressed.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def RepeatDelay(self) -> int:
        """
        specifies the mouse repeat delay, in milliseconds.
        
        When the user presses a mouse in a control area where this triggers an action (such as spinning the value), then usual control implementations allow to repeatedly trigger this action, without the need to release the mouse button and to press it again. The delay between two such triggers is specified with this property.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def Spin(self) -> bool:
        """
        specifies that the control has a spin button.
        """
        ...

    @abstractproperty
    def StrictFormat(self) -> bool:
        """
        specifies that the text is checked during the user input.
        
        This property is optional - not every component implementing this service is required to provide it, as real-time input checking on a formatted field may be pretty expensive.
        """
        ...

    @abstractproperty
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...

    @abstractproperty
    def Text(self) -> str:
        """
        specifies the text displayed in the control.
        """
        ...

    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @abstractproperty
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @abstractproperty
    def TreatAsNumber(self) -> bool:
        """
        specifies that the text is treated as a number.
        """
        ...

    @abstractproperty
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 3.3
        """
        ...

    @abstractproperty
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...


__all__ = ['UnoControlFormattedFieldModel']

