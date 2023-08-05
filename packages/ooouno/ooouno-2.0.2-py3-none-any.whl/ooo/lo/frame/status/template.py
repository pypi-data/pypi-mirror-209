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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Template(object):
    """
    Struct Class

    contains an association between a style name and a value.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Template <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1Template.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.Template'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.Template'
    """Literal Constant ``com.sun.star.frame.status.Template``"""

    def __init__(self, StyleName: typing.Optional[str] = '', Value: typing.Optional[int] = 0, StyleNameIdentifier: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            StyleName (str, optional): StyleName value.
            Value (int, optional): Value value.
            StyleNameIdentifier (str, optional): StyleNameIdentifier value.
        """
        super().__init__()

        if isinstance(StyleName, Template):
            oth: Template = StyleName
            self.StyleName = oth.StyleName
            self.Value = oth.Value
            self.StyleNameIdentifier = oth.StyleNameIdentifier
            return

        kargs = {
            "StyleName": StyleName,
            "Value": Value,
            "StyleNameIdentifier": StyleNameIdentifier,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._style_name = kwargs["StyleName"]
        self._value = kwargs["Value"]
        self._style_name_identifier = kwargs["StyleNameIdentifier"]


    @property
    def StyleName(self) -> str:
        """
        specifies a style name.
        """
        return self._style_name

    @StyleName.setter
    def StyleName(self, value: str) -> None:
        self._style_name = value

    @property
    def Value(self) -> int:
        """
        specifies a value that is bound to the style name.
        """
        return self._value

    @Value.setter
    def Value(self, value: int) -> None:
        self._value = value

    @property
    def StyleNameIdentifier(self) -> str:
        """
        specifies an identifier name in English (only for standard style).
        
        **since**
        
            LO 7.2
        """
        return self._style_name_identifier

    @StyleNameIdentifier.setter
    def StyleNameIdentifier(self, value: str) -> None:
        self._style_name_identifier = value


__all__ = ['Template']
