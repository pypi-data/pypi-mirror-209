########################################################################
# Copyright (C) 2016-2022 Mark J. Blair, NF6X
#
# This file is part of eetools.
#
#  eetools is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  eetools is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with eetools.  If not, see <http://www.gnu.org/licenses/>.
########################################################################

"""NF6X's misc. electrical engineering related tools."""

from .engformatter import EngFormatter
from .engformatter import eng
from .eseries import E3
from .eseries import E6
from .eseries import E12
from .eseries import E24
from .eseries import E48
from .eseries import E96
from .eseries import E192
from .eseries import match_ratio
from .fractional import frac
from .drilltables import drill
from .drilltables import drill_table
from .drilltables import fractional_drill_table
from .drilltables import number_drill_table
from .drilltables import letter_drill_table


__all__ = ['engformatter', 'eseries', 'fractional', 'drilltables']
__version__ = '0.3'
__copyright__ = 'Copyright (C) 2020 Mark J. Blair, released under GPLv3'
__pkg_url__ = 'https://gitlab.com/NF6X_Development/nf6x_eetools'
__dl_url__ = 'https://gitlab.com/NF6X_Development/nf6x_eetools'
__short_desc__ = __doc__
__long_desc__ = """NF6X's misc. electrical engineering related tools:

* eformat:       Extend string.format() with engineering number format.
* E3, E6, etc:   Find nearest IEC 60063:2015 standard component value.
* match_ratio(): Find nearby standard component values approximating a ratio.
* frac():        Convert number to fraction.
* drill():       Find nearest American twist drill size.
"""


eformat = EngFormatter().format
