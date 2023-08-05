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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35
    from ..io.x_stream import XStream as XStream_678908a4
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
    from ..util.date_time import DateTime as DateTime_84de09d3

class XSimpleFileAccess(XInterface_8f010a43):
    """
    This is the basic interface to read data from a stream.

    See Also:
        `API XSimpleFileAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XSimpleFileAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XSimpleFileAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XSimpleFileAccess'

    @abstractmethod
    def copy(self, SourceURL: str, DestURL: str) -> None:
        """
        Copies a file.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def createFolder(self, NewFolderURL: str) -> None:
        """
        Creates a new Folder.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def exists(self, FileURL: str) -> bool:
        """
        Checks if a file exists.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getContentType(self, FileURL: str) -> str:
        """
        Returns the content type of a file.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getDateTimeModified(self, FileURL: str) -> 'DateTime_84de09d3':
        """
        Returns the last modified date for the file.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getFolderContents(self, FolderURL: str, bIncludeFolders: bool) -> 'typing.Tuple[str, ...]':
        """
        Returns the contents of a folder.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getSize(self, FileURL: str) -> int:
        """
        Returns the size of a file.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def isFolder(self, FileURL: str) -> bool:
        """
        Checks if a URL represents a folder.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def isReadOnly(self, FileURL: str) -> bool:
        """
        Checks if a file is \"read only\".

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def kill(self, FileURL: str) -> None:
        """
        Removes a file.
        
        If the URL represents a folder, the folder will be removed, even if it's not empty.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def move(self, SourceURL: str, DestURL: str) -> None:
        """
        Moves a file.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def openFileRead(self, FileURL: str) -> 'XInputStream_98d40ab4':
        """
        Opens file to read.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def openFileReadWrite(self, FileURL: str) -> 'XStream_678908a4':
        """
        Opens file to read and write.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def openFileWrite(self, FileURL: str) -> 'XOutputStream_a4e00b35':
        """
        Opens file to write.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def setInteractionHandler(self, Handler: 'XInteractionHandler_bf80e51') -> None:
        """
        Sets an interaction handler to be used for further operations.
        
        A default interaction handler is available as service com.sun.star.task.InteractionHandler. The documentation of this service also contains further information about the interaction handler concept.
        """
        ...
    @abstractmethod
    def setReadOnly(self, FileURL: str, bReadOnly: bool) -> None:
        """
        Sets the \"read only\" of a file according to the boolean parameter, if the actual process has the right to do so.

        Raises:
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XSimpleFileAccess']

