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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class DriverPropertyInfo(object):
    """
    Struct Class

    describes the driver properties for making a connection.
    
    The DriverPropertyInfo is of interest only to advanced programmers who need to interact with a driver to discover and supply properties for connections.

    See Also:
        `API DriverPropertyInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdbc_1_1DriverPropertyInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.DriverPropertyInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdbc.DriverPropertyInfo'
    """Literal Constant ``com.sun.star.sdbc.DriverPropertyInfo``"""

    def __init__(self, Choices: typing.Optional[typing.Tuple[str, ...]] = (), Name: typing.Optional[str] = '', Description: typing.Optional[str] = '', IsRequired: typing.Optional[bool] = False, Value: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Choices (typing.Tuple[str, ...], optional): Choices value.
            Name (str, optional): Name value.
            Description (str, optional): Description value.
            IsRequired (bool, optional): IsRequired value.
            Value (str, optional): Value value.
        """
        super().__init__()

        if isinstance(Choices, DriverPropertyInfo):
            oth: DriverPropertyInfo = Choices
            self.Choices = oth.Choices
            self.Name = oth.Name
            self.Description = oth.Description
            self.IsRequired = oth.IsRequired
            self.Value = oth.Value
            return

        kargs = {
            "Choices": Choices,
            "Name": Name,
            "Description": Description,
            "IsRequired": IsRequired,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._choices = kwargs["Choices"]
        self._name = kwargs["Name"]
        self._description = kwargs["Description"]
        self._is_required = kwargs["IsRequired"]
        self._value = kwargs["Value"]


    @property
    def Choices(self) -> typing.Tuple[str, ...]:
        """
        contains a sequence of possible values if the value for the field DriverPropertyInfo.value may be selected from a particular set of values; otherwise empty.
        """
        return self._choices

    @Choices.setter
    def Choices(self, value: typing.Tuple[str, ...]) -> None:
        self._choices = value

    @property
    def Name(self) -> str:
        """
        is the name of the property.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Description(self) -> str:
        """
        is a brief description of the property, which may be null.
        """
        return self._description

    @Description.setter
    def Description(self, value: str) -> None:
        self._description = value

    @property
    def IsRequired(self) -> bool:
        """
        is TRUE if a value must be supplied for this property during Driver.connect and FALSE otherwise.
        """
        return self._is_required

    @IsRequired.setter
    def IsRequired(self, value: bool) -> None:
        self._is_required = value

    @property
    def Value(self) -> str:
        """
        specifies the current value of the property, based on the driver-supplied default values.
        
        This field may be empty if no value is known.
        """
        return self._value

    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['DriverPropertyInfo']
