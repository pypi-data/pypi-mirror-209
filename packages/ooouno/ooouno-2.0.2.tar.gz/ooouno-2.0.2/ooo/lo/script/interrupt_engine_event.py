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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .interrupt_reason import InterruptReason as InterruptReason_f3d00dd2


class InterruptEngineEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes an interrupt which occurs in the scripting engine.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API InterruptEngineEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1InterruptEngineEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.InterruptEngineEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.InterruptEngineEvent'
    """Literal Constant ``com.sun.star.script.InterruptEngineEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Name: typing.Optional[str] = '', SourceCode: typing.Optional[str] = '', StartLine: typing.Optional[int] = 0, StartColumn: typing.Optional[int] = 0, EndLine: typing.Optional[int] = 0, EndColumn: typing.Optional[int] = 0, ErrorMessage: typing.Optional[str] = '', Reason: typing.Optional[InterruptReason_f3d00dd2] = InterruptReason_f3d00dd2.Cancel) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Name (str, optional): Name value.
            SourceCode (str, optional): SourceCode value.
            StartLine (int, optional): StartLine value.
            StartColumn (int, optional): StartColumn value.
            EndLine (int, optional): EndLine value.
            EndColumn (int, optional): EndColumn value.
            ErrorMessage (str, optional): ErrorMessage value.
            Reason (InterruptReason, optional): Reason value.
        """

        if isinstance(Source, InterruptEngineEvent):
            oth: InterruptEngineEvent = Source
            self.Source = oth.Source
            self.Name = oth.Name
            self.SourceCode = oth.SourceCode
            self.StartLine = oth.StartLine
            self.StartColumn = oth.StartColumn
            self.EndLine = oth.EndLine
            self.EndColumn = oth.EndColumn
            self.ErrorMessage = oth.ErrorMessage
            self.Reason = oth.Reason
            return

        kargs = {
            "Source": Source,
            "Name": Name,
            "SourceCode": SourceCode,
            "StartLine": StartLine,
            "StartColumn": StartColumn,
            "EndLine": EndLine,
            "EndColumn": EndColumn,
            "ErrorMessage": ErrorMessage,
            "Reason": Reason,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._source_code = kwargs["SourceCode"]
        self._start_line = kwargs["StartLine"]
        self._start_column = kwargs["StartColumn"]
        self._end_line = kwargs["EndLine"]
        self._end_column = kwargs["EndColumn"]
        self._error_message = kwargs["ErrorMessage"]
        self._reason = kwargs["Reason"]
        inst_keys = ('Name', 'SourceCode', 'StartLine', 'StartColumn', 'EndLine', 'EndColumn', 'ErrorMessage', 'Reason')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Name(self) -> str:
        """
        fully qualified name to address the module or function affected by the event that took place.
        
        If the module or function can't be addressed by name (for example, in case that a runtime-generated eval-module is executed), this string is empty.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def SourceCode(self) -> str:
        """
        source code of the Module affected by the event that took place.
        
        If the source can be accessed using the ModuleName, or if the source is unknown (executing compiled code), this string can be empty.
        """
        return self._source_code

    @SourceCode.setter
    def SourceCode(self, value: str) -> None:
        self._source_code = value

    @property
    def StartLine(self) -> int:
        """
        contains the first line in the module's source code that is affected by the event that took place.
        
        If \"name\" addresses a function, all line and column values are nevertheless given relative to the module's source. If source code is not available, this value addresses a binary position in the compiled code.
        """
        return self._start_line

    @StartLine.setter
    def StartLine(self, value: int) -> None:
        self._start_line = value

    @property
    def StartColumn(self) -> int:
        """
        contains the first column in the \"StartLine\" that is affected by the event that took place.
        """
        return self._start_column

    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def EndLine(self) -> int:
        """
        contains the last line in the module's source code that is affected by the event that took place.
        """
        return self._end_line

    @EndLine.setter
    def EndLine(self, value: int) -> None:
        self._end_line = value

    @property
    def EndColumn(self) -> int:
        """
        contains the first column in the \"EndLine\" which is NOT affected by the event that took place.
        """
        return self._end_column

    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value

    @property
    def ErrorMessage(self) -> str:
        """
        error message.
        
        Only valid if Reason is RuntimeError or CompileError.
        """
        return self._error_message

    @ErrorMessage.setter
    def ErrorMessage(self, value: str) -> None:
        self._error_message = value

    @property
    def Reason(self) -> InterruptReason_f3d00dd2:
        """
        contains the interrupt reason.
        """
        return self._reason

    @Reason.setter
    def Reason(self, value: InterruptReason_f3d00dd2) -> None:
        self._reason = value


__all__ = ['InterruptEngineEvent']
