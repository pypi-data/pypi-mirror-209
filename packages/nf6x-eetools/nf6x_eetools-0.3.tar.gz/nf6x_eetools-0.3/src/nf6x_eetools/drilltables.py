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

"""Twist drill size tables"""

fractional_drill_table = {
    "1/64in":  1/64,
    "1/32in":  1/32,
    "3/64in":  3/64,
    "1/16in":  1/16,
    "5/64in":  5/64,
    "3/32in":  3/32,
    "7/64in":  7/64,
    "1/8in":   1/8,
    "9/64in":  9/64,
    "5/32in":  5/32,
    "11/64in": 11/64,
    "3/16in":  3/16,
    "13/64in": 13/64,
    "7/32in":  7/32,
    "15/64in": 15/64,
    "1/4in":   1/4,
    "17/64in": 17/64,
    "9/32in":  9/32,
    "19/64in": 19/64,
    "5/16in":  5/16,
    "21/64in": 21/64,
    "11/32in": 11/32,
    "23/64in": 23/64,
    "3/8in":   3/8,
    "25/64in": 25/64,
    "13/32in": 13/32,
    "27/64in": 27/64,
    "7/16in":  7/16,
    "29/64in": 29/64,
    "15/32in": 15/32,
    "31/64in": 31/64,
    "1/2in":   1/2,
    "33/64in": 33/64,
    "17/32in": 17/32,
    "35/64in": 35/64,
    "9/16in":  9/16,
    "37/64in": 37/64,
    "19/32in": 19/32,
    "39/64in": 39/64,
    "5/8in":   5/8,
    "41/64in": 41/64,
    "21/32in": 21/32,
    "43/64in": 43/64,
    "11/16in": 11/16,
    "45/64in": 45/64,
    "23/32in": 23/32,
    "47/64in": 47/64,
    "3/4in":   3/4,
    "49/64in": 49/64,
    "25/32in": 25/32,
    "51/64in": 51/64,
    "13/16in": 13/16,
    "53/64in": 53/64,
    "27/32in": 27/32,
    "55/64in": 55/64,
    "7/8in":   7/8,
    "57/64in": 57/64,
    "29/32in": 29/32,
    "59/64in": 59/64,
    "15/16in": 15/16,
    "61/64in": 61/64,
    "31/32in": 31/32,
    "63/64in": 63/64,
    "1in":     1.0
}

number_drill_table = {
    'no104': 0.0031,
    'no103': 0.0035,
    'no102': 0.0039,
    'no101': 0.0043,
    'no100': 0.0047,
    'no99':  0.0051,
    'no98':  0.0055,
    'no97':  0.0059,
    'no96':  0.0063,
    'no95':  0.0067,
    'no94':  0.0071,
    'no93':  0.0075,
    'no92':  0.0079,
    'no91':  0.0083,
    'no90':  0.0087,
    'no89':  0.0091,
    'no88':  0.0095,
    'no87':  0.010,
    'no86':  0.0105,
    'no85':  0.011,
    'no84':  0.0115,
    'no83':  0.012,
    'no82':  0.0125,
    'no81':  0.013,
    'no80':  0.0135,
    'no79':  0.0145,
    'no78':  0.016,
    'no77':  0.018,
    'no76':  0.020,
    'no75':  0.021,
    'no74':  0.0225,
    'no73':  0.024,
    'no72':  0.025,
    'no71':  0.026,
    'no70':  0.028,
    'no69':  0.0292,
    'no68':  0.031,
    'no67':  0.032,
    'no66':  0.033,
    'no65':  0.035,
    'no64':  0.036,
    'no63':  0.037,
    'no62':  0.038,
    'no61':  0.039,
    'no60':  0.040,
    'no59':  0.041,
    'no58':  0.042,
    'no57':  0.043,
    'no56':  0.0465,
    'no55':  0.052,
    'no54':  0.055,
    'no53':  0.0595,
    'no52':  0.0635,
    'no51':  0.067,
    'no50':  0.070,
    'no49':  0.073,
    'no48':  0.076,
    'no47':  0.0785,
    'no46':  0.081,
    'no45':  0.082,
    'no44':  0.086,
    'no43':  0.089,
    'no42':  0.0935,
    'no41':  0.096,
    'no40':  0.098,
    'no39':  0.0995,
    'no38':  0.1015,
    'no37':  0.104,
    'no36':  0.1065,
    'no35':  0.110,
    'no34':  0.111,
    'no33':  0.113,
    'no32':  0.116,
    'no31':  0.120,
    'no30':  0.1285,
    'no29':  0.136,
    'no28':  0.1405,
    'no27':  0.144,
    'no26':  0.147,
    'no25':  0.1495,
    'no24':  0.152,
    'no23':  0.154,
    'no22':  0.157,
    'no21':  0.159,
    'no20':  0.161,
    'no19':  0.166,
    'no18':  0.1695,
    'no17':  0.173,
    'no16':  0.177,
    'no15':  0.180,
    'no14':  0.182,
    'no13':  0.185,
    'no12':  0.189,
    'no11':  0.191,
    'no10':  0.1935,
    'no9':   0.196,
    'no8':   0.199,
    'no7':   0.201,
    'no6':   0.204,
    'no5':   0.2055,
    'no4':   0.209,
    'no3':   0.213,
    'no2':   0.221,
    'no1':   0.228
}

letter_drill_table = {
    'A':   0.234,
    'B':   0.238,
    'C':   0.242,
    'D':   0.246,
    'E':   0.250,
    'F':   0.257,
    'G':   0.261,
    'H':   0.266,
    'I':   0.272,
    'J':   0.277,
    'K':   0.281,
    'L':   0.290,
    'M':   0.295,
    'N':   0.302,
    'O':   0.316,
    'P':   0.323,
    'Q':   0.332,
    'R':   0.339,
    'S':   0.348,
    'T':   0.358,
    'U':   0.368,
    'V':   0.377,
    'W':   0.386,
    'X':   0.397,
    'Y':   0.404,
    'Z':   0.413
}

drill_table = {
    **fractional_drill_table,
    **number_drill_table,
    **letter_drill_table
}


def drill(diameter, margin=0, showdiam=True, table=drill_table):
    """Return string representing nearest American drill size

    For a given diameter, return a string representing the nearest
    American twist drill size. Arguments:

    diameter
    margin    If 0, return nearest size;
              if > 0, return equal or larger size;
              if < 0, return equal or smaller size
    showdiam  If True, include actual diameter in returned string
    table     Drill table to use [drill_table]"""

    if margin > 0:
        s = min({k: table[k] for k in table if table[k] >= diameter},
                key=lambda d: table[d]-diameter)
    elif margin < 0:
        s = min({k: table[k] for k in table if table[k] <= diameter},
                key=lambda d: diameter-table[d])
    else:
        s = min(table, key=lambda d: abs(table[d]-diameter))

    if showdiam:
        s = s + f" ({table[s]:g} in)"

    return s
