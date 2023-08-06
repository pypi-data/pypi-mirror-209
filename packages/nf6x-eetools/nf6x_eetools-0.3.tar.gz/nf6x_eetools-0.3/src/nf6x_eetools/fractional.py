# coding: UTF-8
########################################################################
# Copyright (C) 2022 Mark J. Blair, NF6X
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

"""Utilities for fractional dimensions"""

from math import floor, ceil
from fractions import Fraction


def frac(value, denominator=64, rounding=0, correction=True):
    """Find nearest fractional dimension to provided value.

    Returns a string representation of a fractional dimension
    approximating the provided value.

    Arguments:

      value        Numeric value to be approximated
      denominator  Fractional denominator prior to reduction [64]
      rounding     Round normally if 0; round up if positive;
                   round down if negative [0]
      correction   Include correction for original value [True]"""

    # Compute numerator with desired rounding
    if rounding > 0:
        numerator = ceil(value*denominator)
    elif rounding < 0:
        numerator = floor(value*denominator)
    else:
        numerator = round(value*denominator)

    # Convert to Fraction object to reduce the fraction,
    # and find reduced whole, numerator, and denominator parts
    f = Fraction(numerator, denominator)
    rw = int(f.numerator / f.denominator)
    rn = f.numerator % f.denominator
    rd = f.denominator

    # Create string representation
    if rw != 0:
        s = f"{rw}+{rn}/{rd}"
    else:
        s = f"{rn}/{rd}"

    # Append error if requested
    if correction:
        c = value - (rw + rn/rd)
        s = s + f" {c:+g}"

    return s
