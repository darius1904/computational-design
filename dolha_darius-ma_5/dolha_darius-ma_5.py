import Rhino.Geometry as rg
import math


#Task1


import Rhino.Geometry as rg

def curve_to_lines(iCurve, n):
    """
    Convert a curve into N straight line segments.
    Returns a list of rg.Line objects.
    """
    if iCurve is None or n < 2:
        return []

    iCurve.Domain = rg.Interval(0.0, 1.0)

    t0=iCurve.Domain.T0
    t1=iCurve.Domain.T1

    pts = []
    lines = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * (i / float(n))
        pts.append(iCurve.PointAt(t)). #PointAt(t) evaluates the curve at parameter t, returning a Point3d object
    
    # Build lines
    for i in range(n):
        lines.append(rg.Line(pts[i], pts[i+1])). #Line(start, end) creates a straight line segment between two points.
    
    return lines


a=curve_to_lines(iCurve,iN)







#Task3



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
