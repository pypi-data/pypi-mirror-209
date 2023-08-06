# coding: UTF-8
########################################################################
# Copyright (C) 2016-2019 Mark J. Blair, NF6X
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

"""Overload string.Formatter to include engineering numeric format."""

import decimal
import string


def normalize(value, precision=0):
    """Normalize a numeric value to an integer power of 1000.

    Returns (coefficient, exponent) tuple, where exponent is a multiple
    of 3. Coefficient is a decimal.Decimal instance. If precision>0,
    then round to specified total number of significant digits.

    value is immediately cast to a decimal.Decimal instance before
    further processing, so it can be any valid initializer supported
    by decimal.Decimal()."""

    # Convert to coefficient and exponent
    coefficient = decimal.Decimal(value)
    if coefficient.is_zero():
        exponent = 0
    else:
        exponent = int(coefficient.logb())
        coefficient = coefficient.scaleb(-exponent)

    # Round to specified precision
    if precision == 1:
        coefficient = coefficient.quantize(decimal.Decimal('1'),
                                           rounding=decimal.ROUND_HALF_UP)
    elif precision > 1:
        q = str().join(['1.', '0'*(precision-1)])
        coefficient = coefficient.quantize(decimal.Decimal(q),
                                           rounding=decimal.ROUND_HALF_UP)

    # Adjust so exponent is a multiple of 3 and coefficient >= 1,
    # without increasing apparent precision.
    adjustment = exponent % 3
    if adjustment < 0:
        adjustment = adjustment + 3

    if adjustment > 0:
        (s, d, e) = coefficient.as_tuple()
        e = int(e + adjustment)
        if precision == adjustment:
            # Will need to insert one zero left of decimal point
            d = d + (0,)
            e = e - 1
        elif (precision == 1) and (adjustment == 2):
            # Will need to insert two zeros left of decimal point
            d = d + (0, 0)
            e = e - 2
        coefficient = decimal.Decimal((s, d, e))
        exponent = exponent - adjustment

    return (coefficient, exponent)


si_unit_prefix = {
    -24: ('y',  'yocto'),
    -21: ('z',  'zepto'),
    -18: ('a',  'atto'),
    -15: ('f',  'femto'),
    -12: ('p',  'pico'),
    -9:  ('n',  'nano'),
    -6:  ('µ',  'micro'),
    -3:  ('m',  'milli'),
    -2:  ('c',  'centi'),
    -1:  ('d',  'deci'),
    0:   ('',   ''),
    1:   ('da', 'deca'),
    2:   ('h',  'hecto'),
    3:   ('k',  'kilo'),
    6:   ('M',  'mega'),
    9:   ('G',  'giga'),
    12:  ('T',  'tera'),
    15:  ('P'   'peta'),
    18:  ('E',  'exa'),
    21:  ('Z',  'zetta'),
    24:  ('Y',  'yotta')
}


class EngFormatter(string.Formatter):
    """Add engineering numeric format to standard string formatter.

    New 'i' and 'I' format specifiers format numeric value with
    optionally specified relative precision (defaults to 3 digits),
    optional preceding '+' sign for positive values, and SI unit
    prefix. Value is normalized to a power of 1000 with a coefficient
    in the range (1 <= coefficient < 1000).

    'i' provies a symbolic prefix.
    'I' provides a word prefix.

    Format specifier examples:

    '{:i}'
        Default precision of 3 digits. Include sign only for
        negative values. Prefix is symbolic, e.g. 'k'.

    '{:4i}'
        Precision of 4 digits. Include sign only for
        negative values. Prefix is symbolic, e.g. 'k'.

    '{:+i}'
        Default precision of 3 digits. Include sign only for
        both positive and negative values. Prefix is symbolic,
        e.g. 'k'.

    '{:+2I}'
        Precision of 2 digits. Include sign only for
        both positive and negative values. Prefix is a word prefix,
        e.g. 'kilo'

    Usage example:
        import nf6x_eetools as ee
        print(ee.EngFormatter().format('R{:d}: {:2i}Ω', 123, 4700))
    """

    _def_precision = 3

    def format_field(self, value, format_spec):

        if format_spec.endswith('i'):
            # Use symbolic unit prefix
            idx = 0
        elif format_spec.endswith('I'):
            # Use word unit prefix
            idx = 1
        else:
            # Use default string formatter
            return super().format_field(value, format_spec)

        # Parse format specifier, looking for optional
        # + prefix and optional precision value.
        if format_spec.startswith('+'):
            plus_sign = True
            p = format_spec[1:-1]
        else:
            plus_sign = False
            p = format_spec[:-1]
        if p != '':
            try:
                precision = int(p)
            except ValueError:
                raise ValueError('invalid precision specifier: '
                                 + repr(p)
                                 + ' is not an integer value')
            if precision < 1:
                raise ValueError('invalid precision specifier: '
                                 + repr(p)
                                 + ' is not a positive integer value')
        else:
            precision = self._def_precision

        # Normalize the value
        (coefficient, exponent) = normalize(value, precision)

        # Do we have a prefix for this exponent?
        if exponent not in si_unit_prefix:
            raise ValueError('unknown unit prefix for exponent '
                             + str(exponent)
                             + 'in '
                             + repr(value))

        # Assemble formatted string and return it
        if plus_sign and coefficient > 0:
            sign = '+'
        else:
            sign = ''
        return sign + str(coefficient) + ' ' + si_unit_prefix[exponent][idx]


def eng(value, precision=3, unit=''):
    """Shortcut to express a single value in engineering format.

    Handy for use in interactive sessions.

    Usage examples:
        import nf6x_eetools as ee
        ee.eng(12345)
        ee.eng(0.54321, 4, 'V')"""

    fmt = '{:' + str(int(precision)) + 'i}{:s}'
    return EngFormatter().format(fmt, value, unit)
