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
# Namespace: com.sun.star.sdbcx
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class Privilege(metaclass=UnoConstMeta, type_name="com.sun.star.sdbcx.Privilege", name_space="com.sun.star.sdbcx"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbcx.Privilege``"""
        pass

    class PrivilegeEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbcx.Privilege", name_space="com.sun.star.sdbcx"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbcx.Privilege`` as Enum values"""
        pass

else:
    from com.sun.star.sdbcx import Privilege as Privilege

    class PrivilegeEnum(IntFlag):
        """
        Enum of Const Class Privilege

        defines a list of flags (bitmaps) which determines the access rights of a user or a user group.
        
        This list may grow in the future.
        """
        SELECT = Privilege.SELECT
        """
        indicates that a user is allowed to read the data.
        """
        INSERT = Privilege.INSERT
        """
        indicates that a user is allowed to insert new data.
        """
        UPDATE = Privilege.UPDATE
        """
        indicates that a user is allowed to update data.
        """
        DELETE = Privilege.DELETE
        """
        indicates that a user is allowed to delete data.
        """
        READ = Privilege.READ
        """
        indicates that a user is allowed to read the structure of a definition object.
        """
        CREATE = Privilege.CREATE
        """
        indicates that a user is allowed to create a definition object.
        """
        ALTER = Privilege.ALTER
        """
        indicates that a user is allowed to alter an existing object.
        """
        REFERENCE = Privilege.REFERENCE
        """
        indicates that a user is allowed to set foreign keys for a table.
        """
        DROP = Privilege.DROP
        """
        indicates that a user is allowed to drop a definition object.
        """

__all__ = ['Privilege', 'PrivilegeEnum']
