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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from enum import Enum


class FormButtonType(Enum):
    """
    Enum Class


    See Also:
        `API FormButtonType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#abd774094fc2fbbdf91448f8a60c1798a>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.FormButtonType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.form.FormButtonType'

    PUSH = 'PUSH'
    """
    requires the button to act like a common push button, means no special action is triggered.
    """
    RESET = 'RESET'
    """
    When the button is clicked, it performs a reset on its containing form.
    """
    SUBMIT = 'SUBMIT'
    """
    When the button is clicked, it performs a submit on its containing form.
    """
    URL = 'URL'
    """
    When the button is clicked, a URL set for the button is opened.
    
    Specifies to use \"application/x-www-form-urlencoded\" as submit encoding.
    
    Usually used if the FormSubmitMethod attribute has the value POST.
    """

__all__ = ['FormButtonType']

