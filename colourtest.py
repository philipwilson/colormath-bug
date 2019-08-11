#!/usr/bin/env python3

from colormath.color_objects import LabColor, XYZColor, sRGBColor, CMYKColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000, delta_e_cie1994, delta_e_cie1976


print("this test uses the colormath python library to construct a CMYKColor object, convert it to L*a*b, use the L*a*b* values to construct a new LabColor object, then convert it to CMYKColor and dump the results.  We should wind up where we started, but we don't.")


c = CMYKColor(0.75, 0.0, 0.75, 0.2)
print(repr(c))
l = convert_color(c, LabColor)
print(repr(l))
constructor = repr(l)
new_l = eval(constructor)
print(repr(new_l))
new_c = convert_color(new_l, CMYKColor)
print(repr(new_c))
