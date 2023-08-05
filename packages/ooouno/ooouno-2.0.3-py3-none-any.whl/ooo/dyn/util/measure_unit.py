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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class MeasureUnit(metaclass=UnoConstMeta, type_name="com.sun.star.util.MeasureUnit", name_space="com.sun.star.util"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.util.MeasureUnit``"""
        pass

    class MeasureUnitEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.util.MeasureUnit", name_space="com.sun.star.util"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.util.MeasureUnit`` as Enum values"""
        pass

else:
    from com.sun.star.util import MeasureUnit as MeasureUnit

    class MeasureUnitEnum(IntEnum):
        """
        Enum of Const Class MeasureUnit

        These constants are used to specify a measure.
        
        A component using these constants may not support all units.
        """
        MM_100TH = MeasureUnit.MM_100TH
        """
        all measures for this component are in 100th millimeter
        """
        MM_10TH = MeasureUnit.MM_10TH
        """
        all measures for this component are in 10th millimeter
        """
        MM = MeasureUnit.MM
        """
        all measures for this component are in millimeter
        """
        CM = MeasureUnit.CM
        """
        all measures for this component are in centimeters
        """
        INCH_1000TH = MeasureUnit.INCH_1000TH
        """
        all measures for this component are in 1000th inch
        """
        INCH_100TH = MeasureUnit.INCH_100TH
        """
        all measures for this component are in 100th inch
        """
        INCH_10TH = MeasureUnit.INCH_10TH
        """
        all measures for this component are in 10th inch
        """
        INCH = MeasureUnit.INCH
        """
        all measures for this component are in inch
        """
        POINT = MeasureUnit.POINT
        """
        all measures for this component are in points
        """
        TWIP = MeasureUnit.TWIP
        """
        all measures for this component are in twips
        """
        M = MeasureUnit.M
        """
        all measures for this component are in meters
        """
        KM = MeasureUnit.KM
        """
        all measures for this component are in kilometers
        """
        PICA = MeasureUnit.PICA
        """
        all measures for this component are in pica
        """
        FOOT = MeasureUnit.FOOT
        """
        all measures for this component are in foot
        """
        MILE = MeasureUnit.MILE
        """
        all measures for this component are in miles
        """
        PERCENT = MeasureUnit.PERCENT
        """
        all measures for this component are in percentage
        """
        PIXEL = MeasureUnit.PIXEL
        """
        all measures for this component are in pixel
        """
        APPFONT = MeasureUnit.APPFONT
        """
        all measures for this component are in APPFONT
        """
        SYSFONT = MeasureUnit.SYSFONT
        """
        all measures for this component are in SYSFONT
        """

__all__ = ['MeasureUnit', 'MeasureUnitEnum']
