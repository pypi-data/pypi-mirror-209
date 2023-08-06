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

"""IEC 60063:2015 standard component values."""

import decimal
from .engformatter import EngFormatter
from bisect import bisect_left


def find_nearest(series, value):
    """Find item in series nearest to value; return index.

    series must be a sorted iterable. If two items are equally close,
    return the smaller of the two."""

    i = bisect_left(series, value)
    if i == 0:
        return i
    elif i == len(series):
        return i-1
    else:
        a = series[i-1]
        b = series[i]
        if value-a <= b-value:
            return i-1
        else:
            return i


class Eseries():
    """Find nearest IEC 60063:2015 standard component value.

    https://en.wikipedia.org/wiki/E_series_of_preferred_numbers

    This class is immutable. Except where stated otherwise, returned
    numeric values are decimal.Decimal() instances."""

    # Default to [1,2,5] series. Override this in inherited classes
    # for standard IEC 60063:2015 series E3...E192.
    # This must be a sorted iterable with values bounded by [1..10).
    # All entries should be decimal.Decimal() instances.
    _series = (
        decimal.Decimal('1'),
        decimal.Decimal('2'),
        decimal.Decimal('5')
    )

    # Digits of precision appropriate for this series. Override this
    # in inherited classes.
    _precision = 1

    # Tolerance appropriate for this series. Override this in inherited
    # classes.
    _tolerance = decimal.Decimal('0.5')

    def __init__(self, value=0):
        """Initialize the class from a numeric value to be approximated.

        value must be >= 0, and may be any type supported by the
        decimal.Decimal() initializer. If value is derived from Eseries,
        then re-approximate its original initilization value."""

        if issubclass(value.__class__, Eseries):
            self._orig = value.orig()
        else:
            self._orig = value
        self._exact = decimal.Decimal(self._orig)

        if self._exact < 0:
            raise ValueError('ERROR: value must be nonnegative.')

        exponent = self._exact.logb()
        coefficient = self._exact.scaleb(-1*exponent)

        self._index = find_nearest(self._series, coefficient)
        self._approx = self._series[self._index].scaleb(exponent)

    def __float__(self):
        """Return E series approximation as a float value."""
        return float(self._approx)

    def __str__(self):
        """Return E series approximation as a string.

        Returns a string formatted with EngFormatter.format(),
        having an SI unit prefix and an appropriate number of digits
        of precision for this series."""

        fmt = '{:' + str(self._precision) + 'i}'
        eng = EngFormatter()
        return eng.format(fmt, self._approx)

    def __repr__(self):
        """Return string representation of object."""
        return '<{:s}({:s})={:s}>'.format(self.__class__.__name__,
                                          repr(self._orig),
                                          str(self))

    def orig(self):
        """Return original value used to initialize this class.

        Returned value is same type that was passed to initializer."""

        return self._orig

    def exact(self):
        """Return the exact value used to initialize this class.

        Returned value is a decimal.Decimal() object."""

        return self._exact

    def approx(self):
        """Return the E series approximation for the initializer value."""

        return self._approx

    def next(self):
        """Return the next greater value in this series."""

        exponent = self._approx.logb()
        if self._index == (len(self._series) - 1):
            newidx = 0
            exponent = exponent + 1
        else:
            newidx = self._index + 1
        return self.__class__(self._series[newidx].scaleb(exponent))

    def prev(self):
        """Return the previous smaller value in this series."""

        exponent = self._approx.logb()
        if self._index == 0:
            newidx = len(self._series) - 1
            exponent = exponent - 1
        else:
            newidx = self._index - 1
        return self.__class__(self._series[newidx].scaleb(exponent))

    def error(self):
        """Return error as ratio (approx()-exact())/exact()."""

        return (self._approx - self._exact)/self._exact

    def tolerance(self):
        """Return component tolerance appropriate for this series.

        For example, the E96 series is typically used for +/-1% component
        tolerances, so E96.tolerance() would return 0.01."""

        return self._tolerance

    def precision(self):
        """Return number of digits of precision appropriate for this series.

        Return value is an int."""

        return self._precision

    def series(self):
        """Return the list of decade coefficients for this series."""

        return self._series

    def index(self):
        """Return the index in the decade coefficient list for this value."""

        return self._index


class E3(Eseries):
    """IEC 60063:2015 standard ±40% tolerance component values."""
    _tolerance = decimal.Decimal('0.4')
    _precision = 2
    _series = (
        decimal.Decimal('1.0'),
        decimal.Decimal('2.2'),
        decimal.Decimal('4.7')
    )


class E6(Eseries):
    """IEC 60063:2015 standard ±20% tolerance component values."""
    _tolerance = decimal.Decimal('0.2')
    _precision = 2
    _series = (
        decimal.Decimal('1.0'),
        decimal.Decimal('1.5'),
        decimal.Decimal('2.2'),
        decimal.Decimal('3.3'),
        decimal.Decimal('4.7'),
        decimal.Decimal('6.8')
    )


class E12(Eseries):
    """IEC 60063:2015 standard ±10% tolerance component values."""
    _tolerance = decimal.Decimal('0.1')
    _precision = 2
    _series = (
        decimal.Decimal('1.0'),
        decimal.Decimal('1.2'),
        decimal.Decimal('1.5'),
        decimal.Decimal('1.8'),
        decimal.Decimal('2.2'),
        decimal.Decimal('2.7'),
        decimal.Decimal('3.3'),
        decimal.Decimal('3.9'),
        decimal.Decimal('4.7'),
        decimal.Decimal('5.6'),
        decimal.Decimal('6.8'),
        decimal.Decimal('8.2')
    )


class E24(Eseries):
    """IEC 60063:2015 standard ±5% tolerance component values."""
    _tolerance = decimal.Decimal('0.05')
    _precision = 2
    _series = (
        decimal.Decimal('1.0'),
        decimal.Decimal('1.1'),
        decimal.Decimal('1.2'),
        decimal.Decimal('1.3'),
        decimal.Decimal('1.5'),
        decimal.Decimal('1.6'),
        decimal.Decimal('1.8'),
        decimal.Decimal('2.0'),
        decimal.Decimal('2.2'),
        decimal.Decimal('2.4'),
        decimal.Decimal('2.7'),
        decimal.Decimal('3.0'),
        decimal.Decimal('3.3'),
        decimal.Decimal('3.6'),
        decimal.Decimal('3.9'),
        decimal.Decimal('4.3'),
        decimal.Decimal('4.7'),
        decimal.Decimal('5.1'),
        decimal.Decimal('5.6'),
        decimal.Decimal('6.2'),
        decimal.Decimal('6.8'),
        decimal.Decimal('7.5'),
        decimal.Decimal('8.2'),
        decimal.Decimal('9.1')
    )


class E48(Eseries):
    """IEC 60063:2015 standard ±2% tolerance component values."""
    _tolerance = decimal.Decimal('0.02')
    _precision = 3
    _series = (
        decimal.Decimal('1.00'),
        decimal.Decimal('1.05'),
        decimal.Decimal('1.10'),
        decimal.Decimal('1.15'),
        decimal.Decimal('1.21'),
        decimal.Decimal('1.27'),
        decimal.Decimal('1.33'),
        decimal.Decimal('1.40'),
        decimal.Decimal('1.47'),
        decimal.Decimal('1.54'),
        decimal.Decimal('1.62'),
        decimal.Decimal('1.69'),
        decimal.Decimal('1.78'),
        decimal.Decimal('1.87'),
        decimal.Decimal('1.96'),
        decimal.Decimal('2.05'),
        decimal.Decimal('2.15'),
        decimal.Decimal('2.26'),
        decimal.Decimal('2.37'),
        decimal.Decimal('2.49'),
        decimal.Decimal('2.61'),
        decimal.Decimal('2.74'),
        decimal.Decimal('2.87'),
        decimal.Decimal('3.01'),
        decimal.Decimal('3.16'),
        decimal.Decimal('3.32'),
        decimal.Decimal('3.48'),
        decimal.Decimal('3.65'),
        decimal.Decimal('3.83'),
        decimal.Decimal('4.02'),
        decimal.Decimal('4.22'),
        decimal.Decimal('4.42'),
        decimal.Decimal('4.64'),
        decimal.Decimal('4.87'),
        decimal.Decimal('5.11'),
        decimal.Decimal('5.36'),
        decimal.Decimal('5.62'),
        decimal.Decimal('5.90'),
        decimal.Decimal('6.19'),
        decimal.Decimal('6.49'),
        decimal.Decimal('6.81'),
        decimal.Decimal('7.15'),
        decimal.Decimal('7.50'),
        decimal.Decimal('7.87'),
        decimal.Decimal('8.25'),
        decimal.Decimal('8.66'),
        decimal.Decimal('9.09'),
        decimal.Decimal('9.53')
    )


class E96(Eseries):
    """IEC 60063:2015 standard ±1% tolerance component values."""
    _tolerance = decimal.Decimal('0.01')
    _precision = 3
    _series = (
        decimal.Decimal('1.00'),
        decimal.Decimal('1.02'),
        decimal.Decimal('1.05'),
        decimal.Decimal('1.07'),
        decimal.Decimal('1.10'),
        decimal.Decimal('1.13'),
        decimal.Decimal('1.15'),
        decimal.Decimal('1.18'),
        decimal.Decimal('1.21'),
        decimal.Decimal('1.24'),
        decimal.Decimal('1.27'),
        decimal.Decimal('1.30'),
        decimal.Decimal('1.33'),
        decimal.Decimal('1.37'),
        decimal.Decimal('1.40'),
        decimal.Decimal('1.43'),
        decimal.Decimal('1.47'),
        decimal.Decimal('1.50'),
        decimal.Decimal('1.54'),
        decimal.Decimal('1.58'),
        decimal.Decimal('1.62'),
        decimal.Decimal('1.65'),
        decimal.Decimal('1.69'),
        decimal.Decimal('1.74'),
        decimal.Decimal('1.78'),
        decimal.Decimal('1.82'),
        decimal.Decimal('1.87'),
        decimal.Decimal('1.91'),
        decimal.Decimal('1.96'),
        decimal.Decimal('2.00'),
        decimal.Decimal('2.05'),
        decimal.Decimal('2.10'),
        decimal.Decimal('2.15'),
        decimal.Decimal('2.21'),
        decimal.Decimal('2.26'),
        decimal.Decimal('2.32'),
        decimal.Decimal('2.37'),
        decimal.Decimal('2.43'),
        decimal.Decimal('2.49'),
        decimal.Decimal('2.55'),
        decimal.Decimal('2.61'),
        decimal.Decimal('2.67'),
        decimal.Decimal('2.74'),
        decimal.Decimal('2.80'),
        decimal.Decimal('2.87'),
        decimal.Decimal('2.94'),
        decimal.Decimal('3.01'),
        decimal.Decimal('3.09'),
        decimal.Decimal('3.16'),
        decimal.Decimal('3.24'),
        decimal.Decimal('3.32'),
        decimal.Decimal('3.40'),
        decimal.Decimal('3.48'),
        decimal.Decimal('3.57'),
        decimal.Decimal('3.65'),
        decimal.Decimal('3.74'),
        decimal.Decimal('3.83'),
        decimal.Decimal('3.92'),
        decimal.Decimal('4.02'),
        decimal.Decimal('4.12'),
        decimal.Decimal('4.22'),
        decimal.Decimal('4.32'),
        decimal.Decimal('4.42'),
        decimal.Decimal('4.53'),
        decimal.Decimal('4.64'),
        decimal.Decimal('4.75'),
        decimal.Decimal('4.87'),
        decimal.Decimal('4.99'),
        decimal.Decimal('5.11'),
        decimal.Decimal('5.23'),
        decimal.Decimal('5.36'),
        decimal.Decimal('5.49'),
        decimal.Decimal('5.62'),
        decimal.Decimal('5.76'),
        decimal.Decimal('5.90'),
        decimal.Decimal('6.04'),
        decimal.Decimal('6.19'),
        decimal.Decimal('6.34'),
        decimal.Decimal('6.49'),
        decimal.Decimal('6.65'),
        decimal.Decimal('6.81'),
        decimal.Decimal('6.98'),
        decimal.Decimal('7.15'),
        decimal.Decimal('7.32'),
        decimal.Decimal('7.50'),
        decimal.Decimal('7.68'),
        decimal.Decimal('7.87'),
        decimal.Decimal('8.06'),
        decimal.Decimal('8.25'),
        decimal.Decimal('8.45'),
        decimal.Decimal('8.66'),
        decimal.Decimal('8.87'),
        decimal.Decimal('9.09'),
        decimal.Decimal('9.31'),
        decimal.Decimal('9.53'),
        decimal.Decimal('9.76')
    )


class E192(Eseries):
    """IEC 60063:2015 standard ±0.5% tolerance component values."""
    _tolerance = decimal.Decimal('0.005')
    _precision = 3
    _series = (
        decimal.Decimal('1.00'),
        decimal.Decimal('1.01'),
        decimal.Decimal('1.02'),
        decimal.Decimal('1.04'),
        decimal.Decimal('1.05'),
        decimal.Decimal('1.06'),
        decimal.Decimal('1.07'),
        decimal.Decimal('1.09'),
        decimal.Decimal('1.10'),
        decimal.Decimal('1.11'),
        decimal.Decimal('1.13'),
        decimal.Decimal('1.14'),
        decimal.Decimal('1.15'),
        decimal.Decimal('1.17'),
        decimal.Decimal('1.18'),
        decimal.Decimal('1.20'),
        decimal.Decimal('1.21'),
        decimal.Decimal('1.23'),
        decimal.Decimal('1.24'),
        decimal.Decimal('1.26'),
        decimal.Decimal('1.27'),
        decimal.Decimal('1.29'),
        decimal.Decimal('1.30'),
        decimal.Decimal('1.32'),
        decimal.Decimal('1.33'),
        decimal.Decimal('1.35'),
        decimal.Decimal('1.37'),
        decimal.Decimal('1.38'),
        decimal.Decimal('1.40'),
        decimal.Decimal('1.42'),
        decimal.Decimal('1.43'),
        decimal.Decimal('1.45'),
        decimal.Decimal('1.47'),
        decimal.Decimal('1.49'),
        decimal.Decimal('1.50'),
        decimal.Decimal('1.52'),
        decimal.Decimal('1.54'),
        decimal.Decimal('1.56'),
        decimal.Decimal('1.58'),
        decimal.Decimal('1.60'),
        decimal.Decimal('1.62'),
        decimal.Decimal('1.64'),
        decimal.Decimal('1.65'),
        decimal.Decimal('1.67'),
        decimal.Decimal('1.69'),
        decimal.Decimal('1.72'),
        decimal.Decimal('1.74'),
        decimal.Decimal('1.76'),
        decimal.Decimal('1.78'),
        decimal.Decimal('1.80'),
        decimal.Decimal('1.82'),
        decimal.Decimal('1.84'),
        decimal.Decimal('1.87'),
        decimal.Decimal('1.89'),
        decimal.Decimal('1.91'),
        decimal.Decimal('1.93'),
        decimal.Decimal('1.96'),
        decimal.Decimal('1.98'),
        decimal.Decimal('2.00'),
        decimal.Decimal('2.03'),
        decimal.Decimal('2.05'),
        decimal.Decimal('2.08'),
        decimal.Decimal('2.10'),
        decimal.Decimal('2.13'),
        decimal.Decimal('2.15'),
        decimal.Decimal('2.18'),
        decimal.Decimal('2.21'),
        decimal.Decimal('2.23'),
        decimal.Decimal('2.26'),
        decimal.Decimal('2.29'),
        decimal.Decimal('2.32'),
        decimal.Decimal('2.34'),
        decimal.Decimal('2.37'),
        decimal.Decimal('2.40'),
        decimal.Decimal('2.43'),
        decimal.Decimal('2.46'),
        decimal.Decimal('2.49'),
        decimal.Decimal('2.52'),
        decimal.Decimal('2.55'),
        decimal.Decimal('2.58'),
        decimal.Decimal('2.61'),
        decimal.Decimal('2.64'),
        decimal.Decimal('2.67'),
        decimal.Decimal('2.71'),
        decimal.Decimal('2.74'),
        decimal.Decimal('2.77'),
        decimal.Decimal('2.80'),
        decimal.Decimal('2.84'),
        decimal.Decimal('2.87'),
        decimal.Decimal('2.91'),
        decimal.Decimal('2.94'),
        decimal.Decimal('2.98'),
        decimal.Decimal('3.01'),
        decimal.Decimal('3.05'),
        decimal.Decimal('3.09'),
        decimal.Decimal('3.12'),
        decimal.Decimal('3.16'),
        decimal.Decimal('3.20'),
        decimal.Decimal('3.24'),
        decimal.Decimal('3.28'),
        decimal.Decimal('3.32'),
        decimal.Decimal('3.36'),
        decimal.Decimal('3.40'),
        decimal.Decimal('3.44'),
        decimal.Decimal('3.48'),
        decimal.Decimal('3.52'),
        decimal.Decimal('3.57'),
        decimal.Decimal('3.61'),
        decimal.Decimal('3.65'),
        decimal.Decimal('3.70'),
        decimal.Decimal('3.74'),
        decimal.Decimal('3.79'),
        decimal.Decimal('3.83'),
        decimal.Decimal('3.88'),
        decimal.Decimal('3.92'),
        decimal.Decimal('3.97'),
        decimal.Decimal('4.02'),
        decimal.Decimal('4.07'),
        decimal.Decimal('4.12'),
        decimal.Decimal('4.17'),
        decimal.Decimal('4.22'),
        decimal.Decimal('4.27'),
        decimal.Decimal('4.32'),
        decimal.Decimal('4.37'),
        decimal.Decimal('4.42'),
        decimal.Decimal('4.48'),
        decimal.Decimal('4.53'),
        decimal.Decimal('4.59'),
        decimal.Decimal('4.64'),
        decimal.Decimal('4.70'),
        decimal.Decimal('4.75'),
        decimal.Decimal('4.81'),
        decimal.Decimal('4.87'),
        decimal.Decimal('4.93'),
        decimal.Decimal('4.99'),
        decimal.Decimal('5.05'),
        decimal.Decimal('5.11'),
        decimal.Decimal('5.17'),
        decimal.Decimal('5.23'),
        decimal.Decimal('5.30'),
        decimal.Decimal('5.36'),
        decimal.Decimal('5.42'),
        decimal.Decimal('5.49'),
        decimal.Decimal('5.56'),
        decimal.Decimal('5.62'),
        decimal.Decimal('5.69'),
        decimal.Decimal('5.76'),
        decimal.Decimal('5.83'),
        decimal.Decimal('5.90'),
        decimal.Decimal('5.97'),
        decimal.Decimal('6.04'),
        decimal.Decimal('6.12'),
        decimal.Decimal('6.19'),
        decimal.Decimal('6.26'),
        decimal.Decimal('6.34'),
        decimal.Decimal('6.42'),
        decimal.Decimal('6.49'),
        decimal.Decimal('6.57'),
        decimal.Decimal('6.65'),
        decimal.Decimal('6.73'),
        decimal.Decimal('6.81'),
        decimal.Decimal('6.90'),
        decimal.Decimal('6.98'),
        decimal.Decimal('7.06'),
        decimal.Decimal('7.15'),
        decimal.Decimal('7.23'),
        decimal.Decimal('7.32'),
        decimal.Decimal('7.41'),
        decimal.Decimal('7.50'),
        decimal.Decimal('7.59'),
        decimal.Decimal('7.68'),
        decimal.Decimal('7.77'),
        decimal.Decimal('7.87'),
        decimal.Decimal('7.96'),
        decimal.Decimal('8.06'),
        decimal.Decimal('8.16'),
        decimal.Decimal('8.25'),
        decimal.Decimal('8.35'),
        decimal.Decimal('8.45'),
        decimal.Decimal('8.56'),
        decimal.Decimal('8.66'),
        decimal.Decimal('8.76'),
        decimal.Decimal('8.87'),
        decimal.Decimal('8.98'),
        decimal.Decimal('9.09'),
        decimal.Decimal('9.20'),
        decimal.Decimal('9.31'),
        decimal.Decimal('9.42'),
        decimal.Decimal('9.53'),
        decimal.Decimal('9.65'),
        decimal.Decimal('9.76'),
        decimal.Decimal('9.88')
    )


def match_ratio(v1, v2, maxsteps=1):
    """Find pair of standard component values approximating a ratio.

    Given two values v1 and v2, find two nearby standard values which
    most closely match the ratio of their exact values. If passed values
    are derived from Eseries, then chosen value will be in the same
    series, within +/- maxsteps of the nearest standard value. If either
    passed value is not derived from Eseries, then E96 values will be
    used.

    maxsteps must be an integer >= 1.

    Returns tuple of (w1, w2, error) where w1 and w2 are the new
    approximate values, and error is defined as:

                    (w1.approx() / w2.approx())
    error = 1.0  -  ---------------------------
                     (v1.exact() / v2.exact())
    """

    if issubclass(v1.__class__, Eseries):
        av1 = v1
    else:
        av1 = E96(v1)

    if issubclass(v2.__class__, Eseries):
        av2 = v2
    else:
        av2 = E96(v2)

    if (not isinstance(maxsteps, int)) or (maxsteps < 1):
        raise ValueError('maxsteps must be an integer >= 1')

    # The target ratio we want to approximate
    target = av1.exact() / av2.exact()

    # Create lists of component value candidates
    L1 = [None]*((2*maxsteps) + 1)
    L1[maxsteps] = av1
    L2 = [None]*((2*maxsteps) + 1)
    L2[maxsteps] = av2
    for n in range(maxsteps-1, -1, -1):
        L1[n] = L1[n+1].prev()
        L2[n] = L2[n+1].prev()
    for n in range(maxsteps+1, (2*maxsteps)+1):
        L1[n] = L1[n-1].next()
        L2[n] = L2[n-1].next()

    # Evaluate each pair of component value candidates, and pick
    # the pair with minimum error. Give preference to the initial
    # approximations.
    w1 = av1
    w2 = av2
    minerr = decimal.Decimal(1.0) - ((av1.approx()/av2.approx())/target)
    for c1 in L1:
        for c2 in L2:
            err = decimal.Decimal(1.0) - ((c1.approx()/c2.approx())/target)
            if abs(err) < abs(minerr):
                w1 = c1
                w2 = c2
                minerr = err

    # Return results
    return (w1, w2, minerr)
