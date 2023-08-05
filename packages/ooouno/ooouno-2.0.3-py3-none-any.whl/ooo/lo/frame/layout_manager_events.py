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
# Namespace: com.sun.star.frame


class LayoutManagerEvents(object):
    """
    Const Class

    provides information about layout manager events
    
    Events are provided only for notification purposes only.
    
    **since**
    
        OOo 2.0

    See Also:
        `API LayoutManagerEvents <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1LayoutManagerEvents.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.LayoutManagerEvents'
    __ooo_type_name__: str = 'const'

    LOCK = 0
    """
    specifies that the layout manager processed a lock call, which prevents it from doing layouts.
    
    This event sends the current lock count as additional information.
    """
    UNLOCK = 1
    """
    specifies that the layout manager processed an unlock call, which admit layouts when the lock count is zero.
    
    This event sends the current lock count as additional information.
    """
    LAYOUT = 2
    """
    specifies that the layout manager refreshed the layout of the frame.
    
    This event sends no additional information.
    """
    VISIBLE = 3
    """
    specifies that the layout manager container frame window becomes visible.
    
    This event sends no additional information.
    """
    INVISIBLE = 4
    """
    specifies that the layout manager container frame window becomes invisible.
    
    This event sends no additional information.
    """
    MERGEDMENUBAR = 5
    """
    A merged menu bar has been set at the layout manager.
    
    This event sends no additional information.
    """
    UIELEMENT_VISIBLE = 6
    """
    specifies that a certain user interface element has been made visible
    
    This event sends the resource url of the newly visible user interface element.
    """
    UIELEMENT_INVISIBLE = 7
    """
    specifies that a certain user interface element has been made invisible
    
    This event sends the resource url of the invisible user interface element.
    """

__all__ = ['LayoutManagerEvents']
