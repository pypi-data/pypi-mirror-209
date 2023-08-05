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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from ..ucb.x_content import XContent as XContent_79db0975

class DocumentSaveRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    an error specifying the lack of a document name
    
    Usually thrown if someone tries to save a document which hasn't a name yet.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DocumentSaveRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdb_1_1DocumentSaveRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DocumentSaveRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdb.DocumentSaveRequest'
    __pyunostruct__: str = 'com.sun.star.sdb.DocumentSaveRequest'

    typeName: str = 'com.sun.star.sdb.DocumentSaveRequest'
    """Literal Constant ``com.sun.star.sdb.DocumentSaveRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Content: typing.Optional[XContent_79db0975] = None, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Content (XContent, optional): Content value.
            Name (str, optional): Name value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Content": Content,
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._content = kwargs["Content"]
        self._name = kwargs["Name"]
        inst_keys = ('Content', 'Name')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Content(self) -> XContent_79db0975:
        """
        specifies the content where the document should save inside.
        
        Somebody handling the request could, e.g., use the content as root content to display the hierarchy of the sub contents.
        """
        return self._content
    
    @Content.setter
    def Content(self, value: XContent_79db0975) -> None:
        self._content = value

    @property
    def Name(self) -> str:
        """
        The default name of the document, may be empty.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['DocumentSaveRequest']

