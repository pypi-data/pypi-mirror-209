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
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_window import XWindow as XWindow_713b0924

class XContainerWindowEventHandler(XInterface_8f010a43):
    """
    Handles events fired by windows represented by a com.sun.star.awt.XWindow interface.

    See Also:
        `API XContainerWindowEventHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XContainerWindowEventHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XContainerWindowEventHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XContainerWindowEventHandler'

    @abstractmethod
    def callHandlerMethod(self, xWindow: 'XWindow_713b0924', EventObject: object, MethodName: str) -> bool:
        """
        Handles an event generated by a window.
        
        The implementation must be aware that the EventObject argument contains types which it is not prepared to handle. Similarly this applies for the MethodName argument. In this case the method should simply return false.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def getSupportedMethodNames(self) -> 'typing.Tuple[str, ...]':
        """
        returns a sequence of supported method names
        """
        ...

__all__ = ['XContainerWindowEventHandler']

