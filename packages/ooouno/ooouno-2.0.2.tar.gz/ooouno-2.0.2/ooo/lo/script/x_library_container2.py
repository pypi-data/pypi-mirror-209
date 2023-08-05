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
# Namespace: com.sun.star.script
from abc import abstractmethod
from .x_library_container import XLibraryContainer as XLibraryContainer_daa0e6d

class XLibraryContainer2(XLibraryContainer_daa0e6d):
    """
    Extension of XLibraryContainer to provide additional information about the libraries contained in a library container.

    See Also:
        `API XLibraryContainer2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XLibraryContainer2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XLibraryContainer2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XLibraryContainer2'

    @abstractmethod
    def getLibraryLinkURL(self, Name: str) -> str:
        """
        returns the location of the library link target.
        
        Should return the same URL that was passed to createLibraryLink in the StorageURL parameter.
        
        If the accessed library item exists but isn't a link, an IllegalArgumentException is thrown

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def isLibraryLink(self, Name: str) -> bool:
        """
        returns true if the accessed library item is a link, e.g., created by createLibraryLink, otherwise false.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def isLibraryReadOnly(self, Name: str) -> bool:
        """
        returns true if the accessed library item (library or library link) is read only.
        
        A library can be read only because it was set to read only using the methods provided by this interface or because of other reasons depending on the implementation (e.g., file system write protection)

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def renameLibrary(self, Name: str, NewName: str) -> None:
        """
        renames the library item with the specified name.
        
        If the accessed library item is a link only the link is renamed, not the target library. If a library with the new name exists already a com.sun.star.container.ElementExistException is thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    @abstractmethod
    def setLibraryReadOnly(self, Name: str, bReadOnly: bool) -> None:
        """
        Sets the accessed library item (library or library link) to read only according to the flag bReadOnly (true means read only)

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XLibraryContainer2']

