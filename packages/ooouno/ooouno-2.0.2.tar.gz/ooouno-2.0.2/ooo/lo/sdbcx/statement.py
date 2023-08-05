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
# Namespace: com.sun.star.sdbcx
from abc import abstractproperty
from ..sdbc.statement import Statement as Statement_8ed50a59

class Statement(Statement_8ed50a59):
    """
    Service Class

    extends the definition of the service com.sun.star.sdbc.Statement with a flag for the usage of bookmarks.

    See Also:
        `API Statement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Statement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Statement'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def UseBookmarks(self) -> bool:
        """
        returns TRUE if a result set should allow navigation with bookmarks or not.
        
        The default is FALSE.
        """
        ...


__all__ = ['Statement']

