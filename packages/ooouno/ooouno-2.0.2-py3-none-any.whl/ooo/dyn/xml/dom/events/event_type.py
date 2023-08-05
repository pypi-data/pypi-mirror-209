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
# Namespace: com.sun.star.xml.dom.events
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.xml.dom.events.EventType import DOMActivate as EVENT_TYPE_DOMActivate
    from com.sun.star.xml.dom.events.EventType import DOMAttrModified as EVENT_TYPE_DOMAttrModified
    from com.sun.star.xml.dom.events.EventType import DOMCharacterDataModified as EVENT_TYPE_DOMCharacterDataModified
    from com.sun.star.xml.dom.events.EventType import DOMFocusIn as EVENT_TYPE_DOMFocusIn
    from com.sun.star.xml.dom.events.EventType import DOMFocusOut as EVENT_TYPE_DOMFocusOut
    from com.sun.star.xml.dom.events.EventType import DOMNodeInserted as EVENT_TYPE_DOMNodeInserted
    from com.sun.star.xml.dom.events.EventType import DOMNodeInsertedIntoDocument as EVENT_TYPE_DOMNodeInsertedIntoDocument
    from com.sun.star.xml.dom.events.EventType import DOMNodeRemoved as EVENT_TYPE_DOMNodeRemoved
    from com.sun.star.xml.dom.events.EventType import DOMNodeRemovedFromDocument as EVENT_TYPE_DOMNodeRemovedFromDocument
    from com.sun.star.xml.dom.events.EventType import DOMSubtreeModified as EVENT_TYPE_DOMSubtreeModified
    from com.sun.star.xml.dom.events.EventType import click as EVENT_TYPE_click
    from com.sun.star.xml.dom.events.EventType import mousedown as EVENT_TYPE_mousedown
    from com.sun.star.xml.dom.events.EventType import mousemove as EVENT_TYPE_mousemove
    from com.sun.star.xml.dom.events.EventType import mouseout as EVENT_TYPE_mouseout
    from com.sun.star.xml.dom.events.EventType import mouseover as EVENT_TYPE_mouseover
    from com.sun.star.xml.dom.events.EventType import mouseup as EVENT_TYPE_mouseup

    class EventType(uno.Enum):
        """
        Enum Class

        ENUM EventType

        See Also:
            `API EventType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1events.html#a2628ea8d12e8b2563c32f05dc7fff6fa>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.xml.dom.events.EventType', value)

        __ooo_ns__: str = 'com.sun.star.xml.dom.events'
        __ooo_full_ns__: str = 'com.sun.star.xml.dom.events.EventType'
        __ooo_type_name__: str = 'enum'

        DOMActivate: EventType = EVENT_TYPE_DOMActivate
        """
        """
        DOMAttrModified: EventType = EVENT_TYPE_DOMAttrModified
        """
        """
        DOMCharacterDataModified: EventType = EVENT_TYPE_DOMCharacterDataModified
        """
        """
        DOMFocusIn: EventType = EVENT_TYPE_DOMFocusIn
        """
        """
        DOMFocusOut: EventType = EVENT_TYPE_DOMFocusOut
        """
        """
        DOMNodeInserted: EventType = EVENT_TYPE_DOMNodeInserted
        """
        """
        DOMNodeInsertedIntoDocument: EventType = EVENT_TYPE_DOMNodeInsertedIntoDocument
        """
        """
        DOMNodeRemoved: EventType = EVENT_TYPE_DOMNodeRemoved
        """
        """
        DOMNodeRemovedFromDocument: EventType = EVENT_TYPE_DOMNodeRemovedFromDocument
        """
        """
        DOMSubtreeModified: EventType = EVENT_TYPE_DOMSubtreeModified
        """
        """
        click: EventType = EVENT_TYPE_click
        """
        """
        mousedown: EventType = EVENT_TYPE_mousedown
        """
        """
        mousemove: EventType = EVENT_TYPE_mousemove
        """
        """
        mouseout: EventType = EVENT_TYPE_mouseout
        """
        """
        mouseover: EventType = EVENT_TYPE_mouseover
        """
        """
        mouseup: EventType = EVENT_TYPE_mouseup
        """
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class EventType(metaclass=UnoEnumMeta, type_name="com.sun.star.xml.dom.events.EventType", name_space="com.sun.star.xml.dom.events"):
        """Dynamically created class that represents ``com.sun.star.xml.dom.events.EventType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['EventType']
