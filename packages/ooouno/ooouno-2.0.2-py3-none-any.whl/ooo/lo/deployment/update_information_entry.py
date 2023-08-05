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
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..xml.dom.x_element import XElement as XElement_a33d0ae9


class UpdateInformationEntry(object):
    """
    Struct Class

    Objects of this type are used as elements of the enumeration returned by XUpdateInformationProvider.
    
    **since**
    
        OOo 2.3

    See Also:
        `API UpdateInformationEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1deployment_1_1UpdateInformationEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.UpdateInformationEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.deployment.UpdateInformationEntry'
    """Literal Constant ``com.sun.star.deployment.UpdateInformationEntry``"""

    def __init__(self, UpdateDocument: typing.Optional[XElement_a33d0ae9] = None, Description: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            UpdateDocument (XElement, optional): UpdateDocument value.
            Description (str, optional): Description value.
        """
        super().__init__()

        if isinstance(UpdateDocument, UpdateInformationEntry):
            oth: UpdateInformationEntry = UpdateDocument
            self.UpdateDocument = oth.UpdateDocument
            self.Description = oth.Description
            return

        kargs = {
            "UpdateDocument": UpdateDocument,
            "Description": Description,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._update_document = kwargs["UpdateDocument"]
        self._description = kwargs["Description"]


    @property
    def UpdateDocument(self) -> XElement_a33d0ae9:
        """
        the DOM representation of an update information entry
        """
        return self._update_document

    @UpdateDocument.setter
    def UpdateDocument(self, value: XElement_a33d0ae9) -> None:
        self._update_document = value

    @property
    def Description(self) -> str:
        """
        the (optional) description for an update information entry extracted from the update feed container
        """
        return self._description

    @Description.setter
    def Description(self, value: str) -> None:
        self._description = value


__all__ = ['UpdateInformationEntry']
