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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.TransferCommandOperation import COPY as TRANSFER_COMMAND_OPERATION_COPY
    from com.sun.star.ucb.TransferCommandOperation import LINK as TRANSFER_COMMAND_OPERATION_LINK
    from com.sun.star.ucb.TransferCommandOperation import MOVE as TRANSFER_COMMAND_OPERATION_MOVE

    class TransferCommandOperation(uno.Enum):
        """
        Enum Class


        See Also:
            `API TransferCommandOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#ab7b6f3480b7c1c53e953d42a066614b4>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.TransferCommandOperation', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.TransferCommandOperation'
        __ooo_type_name__: str = 'enum'

        COPY = cast("TransferCommandOperation", TRANSFER_COMMAND_OPERATION_COPY)
        """
        Copy the source to the target folder.
        
        WebDAV methods as defined in HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)
        """
        LINK = cast("TransferCommandOperation", TRANSFER_COMMAND_OPERATION_LINK)
        """
        Create a link in the target folder.
        
        The link's target is the source object.
        """
        MOVE = cast("TransferCommandOperation", TRANSFER_COMMAND_OPERATION_MOVE)
        """
        Move the source to the target folder.
        
        WebDAV methods as defined in HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class TransferCommandOperation(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.TransferCommandOperation", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.TransferCommandOperation`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['TransferCommandOperation']
