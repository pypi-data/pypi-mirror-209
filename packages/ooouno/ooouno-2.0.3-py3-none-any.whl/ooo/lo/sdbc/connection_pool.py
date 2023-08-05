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
# Namespace: com.sun.star.sdbc
from .x_connection_pool import XConnectionPool as XConnectionPool_d3710ca6

class ConnectionPool(XConnectionPool_d3710ca6):
    """
    Service Class

    is the basic service for pooling SDBC connections.
    
    When the method com.sun.star.sdbc.XPooledConnection.getConnection() is called, the ConnectionPool will attempt to locate a suitable pooled connection or create a new connection from the DriverManager. When the connection will be released it will move to the pool of unused connections.

    See Also:
        `API ConnectionPool <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1ConnectionPool.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ConnectionPool'
    __ooo_type_name__: str = 'service'


__all__ = ['ConnectionPool']

