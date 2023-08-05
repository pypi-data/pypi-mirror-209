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
# Namespace: com.sun.star.animations


class EventTrigger(object):
    """
    Const Class


    See Also:
        `API EventTrigger <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1EventTrigger.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.EventTrigger'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    Nothing triggers this event.
    """
    ON_BEGIN = 1
    ON_END = 2
    BEGIN_EVENT = 3
    """
    This event is raised when the element local timeline begins to play.
    
    It will be raised each time the element begins the active duration (i.e. when it restarts, but not when it repeats).
    """
    END_EVENT = 4
    """
    This event is raised at the active end of the element.
    
    Note that this event is not raised at the simple end of each repeat.
    """
    ON_CLICK = 5
    ON_DBL_CLICK = 6
    ON_MOUSE_ENTER = 7
    ON_MOUSE_LEAVE = 8
    ON_NEXT = 9
    """
    This event is raised when the user wants the presentation to go one step forward.
    """
    ON_PREV = 10
    """
    This event is raised when the user wants the presentation to go one step backward.
    """
    ON_STOP_AUDIO = 11
    REPEAT = 12
    """
    This event is raised when the element local timeline repeats.
    
    It will be raised each time the element repeats, after the first iteration.
    """

__all__ = ['EventTrigger']
