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
# Namespace: com.sun.star.task
from .x_master_password_handling2 import XMasterPasswordHandling2 as XMasterPasswordHandling2_59b91029
from .x_password_container import XPasswordContainer as XPasswordContainer_fe9d0e09
from .x_url_container import XUrlContainer as XUrlContainer_bbe40be9

class XPasswordContainer2(XMasterPasswordHandling2_59b91029, XPasswordContainer_fe9d0e09, XUrlContainer_bbe40be9):
    """
    Provides a unified interface for the PasswordContainer service to implement.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XPasswordContainer2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XPasswordContainer2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XPasswordContainer2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XPasswordContainer2'


__all__ = ['XPasswordContainer2']

