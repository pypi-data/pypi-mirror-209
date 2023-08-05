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
# Namespace: com.sun.star.sheet.opencl
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class OpenCLDevice(object):
    """
    Struct Class


    See Also:
        `API OpenCLDevice <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1opencl_1_1OpenCLDevice.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet.opencl'
    __ooo_full_ns__: str = 'com.sun.star.sheet.opencl.OpenCLDevice'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.opencl.OpenCLDevice'
    """Literal Constant ``com.sun.star.sheet.opencl.OpenCLDevice``"""

    def __init__(self, Name: typing.Optional[str] = '', Vendor: typing.Optional[str] = '', Driver: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Vendor (str, optional): Vendor value.
            Driver (str, optional): Driver value.
        """
        super().__init__()

        if isinstance(Name, OpenCLDevice):
            oth: OpenCLDevice = Name
            self.Name = oth.Name
            self.Vendor = oth.Vendor
            self.Driver = oth.Driver
            return

        kargs = {
            "Name": Name,
            "Vendor": Vendor,
            "Driver": Driver,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._vendor = kwargs["Vendor"]
        self._driver = kwargs["Driver"]


    @property
    def Name(self) -> str:
        """
        The name of the device as returned by OpenCL.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Vendor(self) -> str:
        """
        The vendor of the device as returned by OpenCL.
        """
        return self._vendor

    @Vendor.setter
    def Vendor(self, value: str) -> None:
        self._vendor = value

    @property
    def Driver(self) -> str:
        """
        The driver version as returned by OpenCL.
        """
        return self._driver

    @Driver.setter
    def Driver(self, value: str) -> None:
        self._driver = value


__all__ = ['OpenCLDevice']
