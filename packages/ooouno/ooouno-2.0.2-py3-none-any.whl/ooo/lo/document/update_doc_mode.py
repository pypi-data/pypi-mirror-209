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
# Namespace: com.sun.star.document


class UpdateDocMode(object):
    """
    Const Class

    Specify the way a document can be updated.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API UpdateDocMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1document_1_1UpdateDocMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.UpdateDocMode'
    __ooo_type_name__: str = 'const'

    NO_UPDATE = 0
    """
    Do not update document.
    """
    QUIET_UPDATE = 1
    """
    Update document if it does not require a dialog.
    
    Otherwise do not update. For example a link to a database can require a dialog to get password for an update.
    """
    ACCORDING_TO_CONFIG = 2
    """
    Produce update according to configuration settings.
    
    If there are no settings use dialog.
    """
    FULL_UPDATE = 3
    """
    Update document even if it does require a dialog.
    """

__all__ = ['UpdateDocMode']
