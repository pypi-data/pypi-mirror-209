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
from ..sdbc.result_set import ResultSet as ResultSet_8ecf0a4f
from .x_delete_rows import XDeleteRows as XDeleteRows_af5c0b72
from .x_row_locate import XRowLocate as XRowLocate_a4730b04
from ..util.x_cancellable import XCancellable as XCancellable_afc30b64

class ResultSet(ResultSet_8ecf0a4f, XDeleteRows_af5c0b72, XRowLocate_a4730b04, XCancellable_afc30b64):
    """
    Service Class

    extends the SDBC ResultSet by the possibility of bookmark positioning, canceling the positioning, and updating of rows.

    See Also:
        `API ResultSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1ResultSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.ResultSet'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CanUpdateInsertedRows(self) -> bool:
        """
        returns whether the result set supports updating of newly inserted rows.
        
        This may not work, as the result set may contain automatic generated data which is used as key information.
        """
        ...

    @abstractproperty
    def IsBookmarkable(self) -> bool:
        """
        returns if the result set supports bookmark navigation.
        """
        ...


__all__ = ['ResultSet']

