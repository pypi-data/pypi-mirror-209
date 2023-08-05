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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc


class ColumnSearch(object):
    """
    Const Class

    indicates in which way a column can be used in the WHERE search.

    See Also:
        `API ColumnSearch <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1ColumnSearch.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ColumnSearch'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    A possible value for column SEARCHABLE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getTypeInfo().
    
    Indicates that WHERE search clauses are not supported for this type.
    """
    CHAR = 1
    """
    A possible value for column SEARCHABLE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getTypeInfo().
    
    Indicates that the only WHERE search clause that can be based on this type is WHERE...LIKE.
    """
    BASIC = 2
    """
    A possible value for column SEARCHABLE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc\">XDatabaseMetaData.getTypeInfo().
    
    Indicates that one can base all WHERE search clauses except WHERE...LIKE on this data type.
    """
    FULL = 3
    """
    A possible value for column SEARCHABLE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc\">XDatabaseMetaData.getTypeInfo().
    
    Indicates that all WHERE search clauses can be based on this type.
    """

__all__ = ['ColumnSearch']
