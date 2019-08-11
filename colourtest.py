#!/usr/bin/env python3

from colormath.color_objects import LabColor, XYZColor, sRGBColor, CMYKColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000, delta_e_cie1994, delta_e_cie1976

greeting = """
This test uses the colormath python library to:
1. Construct a CMYKColor object, 
2. Convert it to LabColor with convert_color
3. Use the L*a*b* values from the resulting LabColor object to construct a new LabColor object
4. Convert it to CMYKColor and dump the results.  

We should wind up where we started, modulo floating-point minutiae, but we don't.
"""
print(greeting)


c = CMYKColor(0.75, 0.0, 0.75, 0.2)
print(repr(c))
l = convert_color(c, LabColor)
print(repr(l))
constructor = repr(l)
new_l = eval(constructor)
print(repr(new_l))
new_c = convert_color(new_l, CMYKColor)
print(repr(new_c))
