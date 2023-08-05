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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class SubIncrement(object):
    """
    Struct Class


    See Also:
        `API SubIncrement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1SubIncrement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.SubIncrement'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.SubIncrement'
    """Literal Constant ``com.sun.star.chart2.SubIncrement``"""

    def __init__(self, IntervalCount: typing.Optional[object] = None, PostEquidistant: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            IntervalCount (object, optional): IntervalCount value.
            PostEquidistant (object, optional): PostEquidistant value.
        """
        super().__init__()

        if isinstance(IntervalCount, SubIncrement):
            oth: SubIncrement = IntervalCount
            self.IntervalCount = oth.IntervalCount
            self.PostEquidistant = oth.PostEquidistant
            return

        kargs = {
            "IntervalCount": IntervalCount,
            "PostEquidistant": PostEquidistant,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._interval_count = kwargs["IntervalCount"]
        self._post_equidistant = kwargs["PostEquidistant"]


    @property
    def IntervalCount(self) -> object:
        """
        should contain nothing for auto, or an integer value for an explicit interval count.
        """
        return self._interval_count

    @IntervalCount.setter
    def IntervalCount(self, value: object) -> None:
        self._interval_count = value

    @property
    def PostEquidistant(self) -> object:
        """
        should contain nothing for auto, or a boolean value for an explicit setting.
        """
        return self._post_equidistant

    @PostEquidistant.setter
    def PostEquidistant(self, value: object) -> None:
        self._post_equidistant = value


__all__ = ['SubIncrement']
