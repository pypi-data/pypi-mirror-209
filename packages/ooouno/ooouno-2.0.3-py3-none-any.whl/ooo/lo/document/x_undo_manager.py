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
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod
from ..container.x_child import XChild as XChild_a6390b07
from ..util.x_lockable import XLockable as XLockable_8f330a3b
if typing.TYPE_CHECKING:
    from .x_undo_action import XUndoAction as XUndoAction_d6580cb3
    from .x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener_5a3b1056

class XUndoManager(XChild_a6390b07, XLockable_8f330a3b):
    """
    provides access to the undo/redo stacks of a document
    
    Changes to a document usually result in recording of information how to undo those changes, if desired. A so-called undo action records the information how to undo a single change. Undo actions are maintained in a stack, so that the changes they represent can be undo in the reverse order they have originally been applied.
    
    Additionally, the Undo manager manages a Redo stack: Actions which are undone are moved from the Undo to the Redo stack, so it is possible to re-apply the changes to the document.
    
    For collecting multiple changes in a single undo action, so-called Undo contexts are provided. When an Undo context is entered, all subsequently added Undo actions are not pushed onto the undo stack directly, but considered a sub action of the Undo context. Once the Undo context is left, a single undo action is pushed onto the undo stack, which comprises all those single Undo actions.Undo contexts can be arbitrarily nested.
    
    Hidden Undo actions are those which in no observable way contribute to the undo stack. That is, any method retrieving information about the stack will behave as if the undo action does not exist. Nonetheless, calling undo() respectively redo() will include those actions.Hidden Undo actions can be created by calling enterHiddenUndoContext(), following by leaveUndoContext().
    
    An Undo manager can be locked and unlocked, using the XLockable.lock() and XLockable.unlock() methods. When it is locked, then every attempt to add an undo action, or to enter or leave an Undo context, will be silently ignored.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XUndoManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XUndoManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XUndoManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XUndoManager'

    @abstractmethod
    def addUndoAction(self, iAction: 'XUndoAction_d6580cb3') -> None:
        """
        adds the given undo action to the undo stack.
        
        The redo stack is cleared when a new action is pushed onto the undo stack.
        
        The Undo manager takes ownership of any actions pushed onto the undo stack. This means that if the action is finally removed from the Undo manager's control (e.g. by calling clear() resp. clearRedo()), it will be disposed, as long as it supports the com.sun.star.lang.XComponent interface.
        
        If the Undo manager is locked at the moment the method is called, the call will be ignored, and the undo action will immediately be disposed, if applicable.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def addUndoManagerListener(self, iListener: 'XUndoManagerListener_5a3b1056') -> None:
        """
        adds a listener to be notified of changes in the Undo/Redo stacks.
        """
        ...
    @abstractmethod
    def clear(self) -> None:
        """
        clears the undo and the redo stack.
        
        All actions will be removed from both the Undo and the Redo stack. Actions which implement the com.sun.star.lang.XComponent interface will be disposed.

        Raises:
            com.sun.star.document.UndoContextNotClosedException: ``UndoContextNotClosedException``
        """
        ...
    @abstractmethod
    def clearRedo(self) -> None:
        """
        clears the redo stack.
        
        All actions will be removed from the Redo stack. Actions which implement the com.sun.star.lang.XComponent interface will be disposed.

        Raises:
            com.sun.star.document.UndoContextNotClosedException: ``UndoContextNotClosedException``
        """
        ...
    @abstractmethod
    def enterHiddenUndoContext(self) -> None:
        """
        enters a new undo context, creating a hidden undo action.
        
        A hidden undo action does not, in any visible way, contribute to the undo stack. This means that
        
        A new undo action will be added to the undo stack. As long as the context is not left, every undo action added to the stack will be treated as sub action. This means it will not be directly accessible at the undo manager, not appear in any user interface, and cannot be separately undone or re-done.
        
        Each call to enterHiddenUndoContext must be paired by a call to leaveUndoContext(), otherwise, the document's undo stack is left in an inconsistent state.
        
        Undo contexts can be nested, i.e. it is legitimate to call enterUndoContext() and enterHiddenUndoContext multiple times without calling leaveUndoContext() inbetween.

        Raises:
            EmptyUndoStackException: ``EmptyUndoStackException``
        """
        ...
    @abstractmethod
    def enterUndoContext(self, iTitle: str) -> None:
        """
        enters a new undo context.
        
        A new undo action will be added to the undo stack, with the title given as iTitle. As long as the context is not left, every undo action added to the stack will be treated as sub action. This means it will not be directly accessible at the Undo manager, not appear in any user interface, and cannot be separately undone or re-done.
        
        Each call to enterUndoContext must be paired by a call to leaveUndoContext(), otherwise, the document's undo stack is left in an inconsistent state.
        
        Undo contexts can be nested, i.e. it is legitimate to call enterUndoContext and enterHiddenUndoContext() multiple times without calling leaveUndoContext() inbetween.
        """
        ...
    @abstractmethod
    def getAllRedoActionTitles(self) -> 'typing.Tuple[str, ...]':
        """
        returns the titles of all actions currently on the Redo stack, from top to bottom
        """
        ...
    @abstractmethod
    def getAllUndoActionTitles(self) -> 'typing.Tuple[str, ...]':
        """
        returns the titles of all actions currently on the undo stack, from top to bottom
        """
        ...
    @abstractmethod
    def getCurrentRedoActionTitle(self) -> str:
        """
        returns the title of the top-most action on the Redo stack

        Raises:
            com.sun.star.document.EmptyUndoStackException: ``EmptyUndoStackException``
        """
        ...
    @abstractmethod
    def getCurrentUndoActionTitle(self) -> str:
        """
        returns the title of the top-most action on the undo stack

        Raises:
            com.sun.star.document.EmptyUndoStackException: ``EmptyUndoStackException``
        """
        ...
    @abstractmethod
    def isRedoPossible(self) -> bool:
        """
        determines whether redo() can reasonably be expected to succeed.
        """
        ...
    @abstractmethod
    def isUndoPossible(self) -> bool:
        """
        determines whether undo() can reasonably be expected to succeed.
        """
        ...
    @abstractmethod
    def leaveUndoContext(self) -> None:
        """
        leaves the undo context previously opened via enterUndoContext() respectively enterHiddenUndoContext().
        
        If no undo action has been added since the context has been opened, the context is not only left, but silently removed, and does not contribute to the undo stack at all. In this case, possible listeners will be notified via XUndoManagerListener.cancelledContext().
        
        Otherwise, the undo context will be closed, and added to the Undo stack; the redo stack will be cleared, and listeners will be notified via XUndoManagerListener.leftContext() resp. XUndoManagerListener.leftHiddenContext()

        Raises:
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def redo(self) -> None:
        """
        replays the action on the document which has most recently been undone
        
        Effectively, invoking this method will

        Raises:
            com.sun.star.document.EmptyUndoStackException: ``EmptyUndoStackException``
            com.sun.star.document.UndoContextNotClosedException: ``UndoContextNotClosedException``
            com.sun.star.document.UndoFailedException: ``UndoFailedException``
        """
        ...
    @abstractmethod
    def removeUndoManagerListener(self, iListener: 'XUndoManagerListener_5a3b1056') -> None:
        """
        removes a previously added listener
        """
        ...
    @abstractmethod
    def reset(self) -> None:
        """
        resets the Undo manager
        
        In particular, this method will
        
        Note that possible listeners will not get notifications for the single parts of the reset, i.e. there will be no single XUndoManagerListener.allActionsCleared(), XUndoManagerListener.leftContext(), etc., notifications. Instead, listeners will be notified of the reset by calling their XUndoManagerListener.resetAll() method.
        """
        ...
    @abstractmethod
    def undo(self) -> None:
        """
        reverts the most recent action on the document.
        
        Effectively, invoking this method will

        Raises:
            com.sun.star.document.EmptyUndoStackException: ``EmptyUndoStackException``
            com.sun.star.document.UndoContextNotClosedException: ``UndoContextNotClosedException``
            com.sun.star.document.UndoFailedException: ``UndoFailedException``
        """
        ...

__all__ = ['XUndoManager']

