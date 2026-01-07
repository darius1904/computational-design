import Rhino.Geometry as rg
import math

# INPUTS
num_curves = 24         # number of curves in the ribbon
points_per_curve = 52   # points along each curve
curve_length = 25       # height of the ribbon
twist_factor = 2        # how much the ribbon twists
amplitude = 3           # sine wave amplitude
lines = []
curves = []

# creatw twisted curves
for i in range(num_curves):
    curve_pts = []
    for j in range(points_per_curve):
        t = j / float(points_per_curve - 1)  # normalized [0,1]
        x = i * 3  # spacing between curves
        y = math.sin(t * math.pi * twist_factor + i) * amplitude
        z = t * curve_length
        curve_pts.append(rg.Point3d(x, y, z))
    #create a polyline curve through the points
    crv = rg.Curve.CreateInterpolatedCurve(curve_pts,3)
    curves.append(crv)
    
    #connect consecutive points with lines for a mesh-like effect
    for k in range(len(curve_pts) - 1):
        lines.append(rg.Line(curve_pts[k], curve_pts[k+1]))
    #the NURBS can be seen when zooming in!!!

# OUTPUT
a = curves  # the twisting ribbon curves
b = lines   # optional connecting lines






print("test")
