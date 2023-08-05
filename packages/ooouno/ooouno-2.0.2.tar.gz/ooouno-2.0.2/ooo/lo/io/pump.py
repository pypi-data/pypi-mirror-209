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
# Namespace: com.sun.star.io
from .x_active_data_control import XActiveDataControl as XActiveDataControl_de310cef
from .x_active_data_sink import XActiveDataSink as XActiveDataSink_b8d00ba3
from .x_active_data_source import XActiveDataSource as XActiveDataSource_d1900c7f

class Pump(XActiveDataControl_de310cef, XActiveDataSink_b8d00ba3, XActiveDataSource_d1900c7f):
    """
    Service Class

    the implementation of a data source and a data sink.
    
    A thread will be created that reads from the input stream and writes the data to the connected output stream. Data will not be buffered by this service.

    See Also:
        `API Pump <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1io_1_1Pump.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.Pump'
    __ooo_type_name__: str = 'service'


__all__ = ['Pump']

