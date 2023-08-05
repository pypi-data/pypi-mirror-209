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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 7.4
from .x_global_event_broadcaster import XGlobalEventBroadcaster as XGlobalEventBroadcaster_55351028


class theGlobalEventBroadcaster(XGlobalEventBroadcaster_55351028):
    """
    Singleton Class

    This singleton offers the document event functionality that can be found at any com.sun.star.document.OfficeDocument, but it does it for all existing documents.
    
    So it is a single place where a listener can be registered for all events in all documents.
    
    Prior to LibreOffice 4.3, this singleton was only available as a (single-instance) GlobalEventBroadcaster service.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API theGlobalEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1frame_1_1theGlobalEventBroadcaster.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.theGlobalEventBroadcaster'
    __ooo_type_name__: str = 'singleton'
    _instance = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


__all__ = ['theGlobalEventBroadcaster']

