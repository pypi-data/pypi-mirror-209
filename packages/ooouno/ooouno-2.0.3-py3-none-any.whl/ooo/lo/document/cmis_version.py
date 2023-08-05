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
# Namespace: com.sun.star.document
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class CmisVersion(object):
    """
    Struct Class

    specifies a CMIS document version.

    See Also:
        `API CmisVersion <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1CmisVersion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.CmisVersion'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.CmisVersion'
    """Literal Constant ``com.sun.star.document.CmisVersion``"""

    def __init__(self, Id: typing.Optional[str] = '', TimeStamp: typing.Optional[object] = UNO_NONE, Author: typing.Optional[str] = '', Comment: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Id (str, optional): Id value.
            TimeStamp (object, optional): TimeStamp value.
            Author (str, optional): Author value.
            Comment (str, optional): Comment value.
        """
        super().__init__()

        if isinstance(Id, CmisVersion):
            oth: CmisVersion = Id
            self.Id = oth.Id
            self.TimeStamp = oth.TimeStamp
            self.Author = oth.Author
            self.Comment = oth.Comment
            return

        kargs = {
            "Id": Id,
            "TimeStamp": TimeStamp,
            "Author": Author,
            "Comment": Comment,
        }
        if kargs["TimeStamp"] is UNO_NONE:
            kargs["TimeStamp"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._id = kwargs["Id"]
        self._time_stamp = kwargs["TimeStamp"]
        self._author = kwargs["Author"]
        self._comment = kwargs["Comment"]


    @property
    def Id(self) -> str:
        """
        unique ID of the Cmis version
        """
        return self._id

    @Id.setter
    def Id(self, value: str) -> None:
        self._id = value

    @property
    def TimeStamp(self) -> object:
        """
        specifies the time when the revision was created.
        """
        return self._time_stamp

    @TimeStamp.setter
    def TimeStamp(self, value: object) -> None:
        self._time_stamp = value

    @property
    def Author(self) -> str:
        """
        contains the author that created the version.
        """
        return self._author

    @Author.setter
    def Author(self, value: str) -> None:
        self._author = value

    @property
    def Comment(self) -> str:
        """
        contains the comment the author has left.
        """
        return self._comment

    @Comment.setter
    def Comment(self, value: str) -> None:
        self._comment = value


__all__ = ['CmisVersion']
