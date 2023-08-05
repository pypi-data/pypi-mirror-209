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
# Namespace: com.sun.star.form
from abc import abstractmethod
from .x_update_broadcaster import XUpdateBroadcaster as XUpdateBroadcaster_fc910de1

class XBoundComponent(XUpdateBroadcaster_fc910de1):
    """
    specifies a (form) component which is bound to a data source.
    
    The interface provides the possibility of committing its respective data to a data source it is bound to. A commit() will be performed by the environment (usually, a FormController).For example, suppose you have a data-bound control that is connected to a database field. Each time the control loses its focus, the model (component) of the control is triggered by the environment to store its value in the database field.
    
    A commit may fail if an XUpdateListener vetoes the it.

    See Also:
        `API XBoundComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XBoundComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XBoundComponent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XBoundComponent'

    @abstractmethod
    def commit(self) -> bool:
        """
        commits the content of the component into the data source it is bound to.
        """
        ...

__all__ = ['XBoundComponent']

