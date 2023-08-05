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
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .note_print_mode import NotePrintMode as NotePrintMode_bdae0bf5

class PrintSettings(ABC):
    """
    Service Class

    These properties describe the printing of the content of a text document.

    See Also:
        `API PrintSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1PrintSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.PrintSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def PrintAnnotationMode(self) -> 'NotePrintMode_bdae0bf5':
        """
        determines how notes are printed.
        """
        ...

    @abstractproperty
    def PrintBlackFonts(self) -> bool:
        """
        determines if characters are always printed in black.
        """
        ...

    @abstractproperty
    def PrintControls(self) -> bool:
        """
        determines if control shapes are printed.
        """
        ...

    @abstractproperty
    def PrintDrawings(self) -> bool:
        """
        determines if shapes are printed.
        """
        ...

    @abstractproperty
    def PrintEmptyPages(self) -> bool:
        """
        determines if automatically inserted empty pages are printed.
        """
        ...

    @abstractproperty
    def PrintFaxName(self) -> str:
        """
        contains the name of the fax.
        """
        ...

    @abstractproperty
    def PrintGraphics(self) -> bool:
        """
        determines if graphic objects are printed
        """
        ...

    @abstractproperty
    def PrintLeftPages(self) -> bool:
        """
        determines if left pages are printed.
        """
        ...

    @abstractproperty
    def PrintPageBackground(self) -> bool:
        """
        determines if the background color / background graphic of pages is printed.
        """
        ...

    @abstractproperty
    def PrintPaperFromSetup(self) -> bool:
        """
        specifies if the printer paper tray selection of the system printer is used.
        
        If com.sun.star.view.PrintSettings.PaperFromSetup is FALSE, then the paper tray selection of the page styles is used.
        """
        ...

    @abstractproperty
    def PrintProspect(self) -> bool:
        """
        determines if prospect printing is used.
        """
        ...

    @abstractproperty
    def PrintReversed(self) -> bool:
        """
        determines if the pages are printed in the reverse order, starting with the last page.
        """
        ...

    @abstractproperty
    def PrintRightPages(self) -> bool:
        """
        determines if right pages are printed.
        """
        ...

    @abstractproperty
    def PrintTables(self) -> bool:
        """
        determines if text tables are printed.
        """
        ...


__all__ = ['PrintSettings']

