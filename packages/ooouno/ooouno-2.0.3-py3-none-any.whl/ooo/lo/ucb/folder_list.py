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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .folder_list_command import FolderListCommand as FolderListCommand_e0140cf9
from .folder_list_entry import FolderListEntry as FolderListEntry_c6c30c4c


class FolderList(object):
    """
    Struct Class

    A list of folders.

    See Also:
        `API FolderList <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1FolderList.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.FolderList'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.FolderList'
    """Literal Constant ``com.sun.star.ucb.FolderList``"""

    def __init__(self, List: typing.Optional[typing.Tuple[FolderListEntry_c6c30c4c, ...]] = (), Command: typing.Optional[FolderListCommand_e0140cf9] = FolderListCommand_e0140cf9.GET) -> None:
        """
        Constructor

        Arguments:
            List (typing.Tuple[FolderListEntry, ...], optional): List value.
            Command (FolderListCommand, optional): Command value.
        """
        super().__init__()

        if isinstance(List, FolderList):
            oth: FolderList = List
            self.List = oth.List
            self.Command = oth.Command
            return

        kargs = {
            "List": List,
            "Command": Command,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._list = kwargs["List"]
        self._command = kwargs["Command"]


    @property
    def List(self) -> typing.Tuple[FolderListEntry_c6c30c4c, ...]:
        """
        The list of folders (only used in conjunction with FolderListCommand.SET).
        """
        return self._list

    @List.setter
    def List(self, value: typing.Tuple[FolderListEntry_c6c30c4c, ...]) -> None:
        self._list = value

    @property
    def Command(self) -> FolderListCommand_e0140cf9:
        """
        The command to process on this list of folders.
        """
        return self._command

    @Command.setter
    def Command(self, value: FolderListCommand_e0140cf9) -> None:
        self._command = value


__all__ = ['FolderList']
