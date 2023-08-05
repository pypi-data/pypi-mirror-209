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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.4
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:

    def _get_class():
        orig_init = None
        ordered_keys = ('FeatureURL', 'FrameName', 'SearchFlags')
        def init(self, *args, **kwargs):
            if len(kwargs) == 0 and len(args) == 1 and getattr(args[0], "__class__", None) == self.__class__:
                orig_init(self, args[0])
                return
            kargs = kwargs.copy()
            for i, arg in enumerate(args):
                kargs[ordered_keys[i]] = arg
            orig_init(self, **kargs)

        type_name = 'com.sun.star.frame.DispatchDescriptor'
        struct = uno.getClass(type_name)
        struct.__ooo_ns__ = 'com.sun.star.frame'
        struct.__ooo_full_ns__= type_name
        struct.__ooo_type_name__ = 'struct'
        orig_init = struct.__init__
        struct.__init__ = init
        return struct

    DispatchDescriptor = _get_class()

else:
    from com.sun.star.frame import DispatchDescriptor as DispatchDescriptor

__all__ = ['DispatchDescriptor']

