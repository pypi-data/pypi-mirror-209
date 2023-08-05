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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from ..lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory_27210f0d

class FileSystemStorageFactory(XSingleServiceFactory_27210f0d):
    """
    Service Class

    The FileSystemStorageFactory is a service that allows to create a FileSystemStorage based on URL.
    
    The URL must point to a folder.
    
    In case com.sun.star.lang.XSingleServiceFactory.createInstance() call is used the result storage will be open in read-write mode based on an arbitrary file system folder.
    
    In case com.sun.star.lang.XSingleServiceFactory.createInstanceWithArguments() call is used a sequence of the following parameters can be used:
    
    The parameters are optional, that means that sequence can be empty or contain only first parameter, or first and second one. In case no parameters are provided the call works the same way as com.sun.star.lang.XSingleServiceFactory.createInstance(). In case only first parameter is provided, the storage is opened in readonly mode.
    
    The opened storages can support read access in addition to specified one.

    See Also:
        `API FileSystemStorageFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1FileSystemStorageFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.FileSystemStorageFactory'
    __ooo_type_name__: str = 'service'


__all__ = ['FileSystemStorageFactory']

