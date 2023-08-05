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
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..frame.x_model import XModel as XModel_7a6e095c


class MailMergeEvent(EventObject_a3d70b03):
    """
    Struct Class

    represents a mail merge event.
    
    This type of event is being sent by the mail merge service right before the merging of the next document to be processed. This allows for example to modify the document specifically before it gets merged.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MailMergeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1MailMergeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.MailMergeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.text.MailMergeEvent'
    """Literal Constant ``com.sun.star.text.MailMergeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Model: typing.Optional[XModel_7a6e095c] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Model (XModel, optional): Model value.
        """

        if isinstance(Source, MailMergeEvent):
            oth: MailMergeEvent = Source
            self.Source = oth.Source
            self.Model = oth.Model
            return

        kargs = {
            "Source": Source,
            "Model": Model,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._model = kwargs["Model"]
        inst_keys = ('Model',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Model(self) -> XModel_7a6e095c:
        """
        The model of the document to be processed next.
        """
        return self._model

    @Model.setter
    def Model(self, value: XModel_7a6e095c) -> None:
        self._model = value


__all__ = ['MailMergeEvent']
