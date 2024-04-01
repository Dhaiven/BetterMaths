from BetterMaths.solidGeometry import *
from math import cos, acos, sin, asin

def coordinatesScalar(u: Vector, v: Vector) -> float:
    return u.x*v.x+u.y*v.y+u.z*v.z

def normScalar(u: Vector, v: Vector) -> float:
    return 0.5*(u.norm()**2+v.norm()**2)

def findAngle(u: Vector, v: Vector, type: int = 0) -> float:
    return acos(coordinatesScalar(u,v)/(u.norm()*v.norm()))

u=Vector(-2,-2,1)
v=Vector(3,0,-3)
print(coordinatesScalar(u,v))
print(findAngle(u,v,))