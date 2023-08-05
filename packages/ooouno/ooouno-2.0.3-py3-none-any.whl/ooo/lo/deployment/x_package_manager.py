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
# Namespace: com.sun.star.deployment
import typing
from abc import abstractmethod
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from .x_package import XPackage as XPackage_cb1f0c4d
    from .x_package_type_info import XPackageTypeInfo as XPackageTypeInfo_3bc70f7b
    from ..task.x_abort_channel import XAbortChannel as XAbortChannel_baca0bc4
    from ..ucb.x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee

class XPackageManager(XComponent_98dc0ab5, XModifyBroadcaster_fd990df0):
    """
    The XPackageManager interface is used to add or remove packages to a specific repository.
    
    This interface represents a particular repository. Packages are deployable files, e.g. scripts or UNO components.
    
    Adding a UNO package means that a copy of the package is stored in the repository.
    
    Removing a UNO package means that the previously added package is removed from the repository.
    
    All interface methods do neither register nor revoke an extension. This happens exclusively by XExtensionManager.
    
    Objects of this interface are created using the XPackageManagerFactory service resp. the singleton  /singletons/com.sun.star.deployment.thePackageManagerFactory .
    
    **since**
    
        OOo 2.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XPackageManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XPackageManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.XPackageManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.deployment.XPackageManager'

    @abstractmethod
    def addPackage(self, url: str, properties: 'typing.Tuple[NamedValue_a37a0af3, ...]', mediaType: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        adds a UNO package.
        
        The properties argument is currently only used to suppress the license information for shared extensions.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def checkPrerequisites(self, extension: 'XPackage_cb1f0c4d', xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> int:
        """
        checks if the extension can be used.
        
        The extension must be managed by this package manager, that is, it must be recorded in its database. The package manager calls XPackage.checkPrerequisites and updates its data base with the result. The result, which is from Prerequisites will be returned.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createAbortChannel(self) -> 'XAbortChannel_baca0bc4':
        """
        creates a command channel to be used to asynchronously abort a command.
        """
        ...
    @abstractmethod
    def getContext(self) -> str:
        """
        returns the underlying deployment context, that is, the name of the repository.
        """
        ...
    @abstractmethod
    def getDeployedPackage(self, identifier: str, fileName: str, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        gets a deployed package.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getDeployedPackages(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage_cb1f0c4d, ...]':
        """
        gets all currently deployed packages.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getExtensionsWithUnacceptedLicenses(self, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage_cb1f0c4d, ...]':
        """
        returns all extensions which are currently not in use because the user did not accept the license.
        
        The function will not return any object for the user repository, because a user extension will not be kept in the user repository if its license is declined. Only extensions which are registered at start-up of OOo, that is, shared and bundled extensions, can be returned.
        
        Extensions which allow the license to be suppressed, that is, it does not need to be displayed, and which are installed with the corresponding option, are also not returned.

        Raises:
            DeploymentException: ``DeploymentException``
        """
        ...
    @abstractmethod
    def getSupportedPackageTypes(self) -> 'typing.Tuple[XPackageTypeInfo_3bc70f7b, ...]':
        """
        gets the supported XPackageTypeInfos.
        """
        ...
    @abstractmethod
    def importExtension(self, extension: 'XPackage_cb1f0c4d', xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        adds an extension.
        
        This copies the extension. If it was from the same repository, which is represented by this XPackageManager interface, then nothing happens.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def isReadOnly(self) -> bool:
        """
        indicates that this implementation cannot be used for tasks which require write access to the location where the extensions are installed.
        
        Normally one would call a method and handle the exception if writing failed. However, a GUI interface may need to know beforehand if writing is allowed. For example, the Extension Manager dialog needs to enable / disable the Add button depending if the user has write permission. Only the XPackageManager implementation knows the location of the installed extensions. Therefore it is not possible to check \"externally\" for write permission.
        """
        ...
    @abstractmethod
    def reinstallDeployedPackages(self, force: bool, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        Expert feature: erases the underlying registry cache and reinstalls all previously added packages.
        
        Please keep in mind that all registration status get lost.
        
        Please use this in case of suspected cache inconsistencies only.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def removePackage(self, identifier: str, fileName: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        removes a UNO package.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def synchronize(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> bool:
        """
        synchronizes the extension database with the contents of the extensions folder.
        
        Added extensions will be added to the database and removed extensions will be removed from the database.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.ContentCreationException: ``ContentCreationException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
        """
        ...

__all__ = ['XPackageManager']

