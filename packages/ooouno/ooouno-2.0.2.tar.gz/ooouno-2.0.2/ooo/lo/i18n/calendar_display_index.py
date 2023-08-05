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
# Namespace: com.sun.star.i18n


class CalendarDisplayIndex(object):
    """
    Const Class

    Values to be passed to XCalendar.getDisplayName().
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API CalendarDisplayIndex <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1CalendarDisplayIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.CalendarDisplayIndex'
    __ooo_type_name__: str = 'const'

    AM_PM = 0
    """
    name of an AM/PM value
    """
    DAY = 1
    """
    name of a day of week
    """
    MONTH = 2
    """
    name of a month
    """
    YEAR = 3
    """
    name of a year (if used for a specific calendar)
    """
    ERA = 4
    """
    name of an era, like BC/AD
    """
    GENITIVE_MONTH = 5
    """
    name of a possessive genitive case month
    
    **since**
    
        LibreOffice 3.5
    """
    PARTITIVE_MONTH = 6
    """
    name of a partitive case month
    
    **since**
    
        LibreOffice 3.5
    """

__all__ = ['CalendarDisplayIndex']
