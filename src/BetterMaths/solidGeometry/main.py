import sympy

class Vector:
    def __init__(self, x, y, z, plane=None) -> None:
        self.x=x
        self.y=y
        self.z=z
        self.plane=plane
    

    def __repr__(self) -> str:
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}\nplane: {self.plane}"


    def collinear(self,u) -> "tuple[bool,object]":
        return collinear(self,u)
    

    def coplanar(self,u,v) -> bool:
        return coplanar(self,u,v)


class Plane:
    def __init__(self, i: Vector, j: Vector, k: Vector) -> None:
        if coplanar(i, j, k):
            raise ValueError("i, j and k are coplanar!")
        self.i=i
        self.j=j
        self.k=k
    
    def __repr__(self) -> str:
        i_coords=f"i: {self.i.x},{self.i.y},{self.i.z}"
        j_coords=f"j: {self.j.x},{self.j.y},{self.j.z}"
        k_coords=f"k: {self.k.x},{self.k.y},{self.k.z}"
        return f"{i_coords}\n{j_coords}\n{k_coords}"


def collinear(u: Vector, v: Vector) -> "tuple[bool,object]":
    try:
        k=v.x/u.x
        if k==(v.y/u.y)==(v.z/u.z):
            return (True, k)
        else:
            return (False, None)
    except:
        return (False,None)


def coplanar(u: Vector, v: Vector, w: Vector) -> bool:
    if collinear(u,v)[0] or collinear(u,w)[0] or collinear(v,w)[0]:
        return True
    if solveSystem2(f"{u.x}*a+{v.x}*b-{w.x}",f"{u.y}*a+{v.y}*b-{w.y}",f"{u.z}*a+{v.z}*b-{w.z}")!={}:
        return False
    return True


def inPlane(u: Vector, plane: Plane):
    i=plane.i
    j=plane.j
    k=plane.k
    solutions=solveSystem3(f"{i.x}*a+{j.x}*b+{k.x}*c-{u.x}",f"{i.y}*a+{j.y}*b+{k.y}*c-{u.y}",f"{i.z}*a+{j.z}*b+{k.z}*c-{u.z}")
    values=list(solutions.values())
    x=values[0]
    y=values[1]
    z=values[2]
    return Vector(x,y,z,plane)

def solveSystem2(eq1, eq2, eq3):
    a, b = sympy.symbols('a b')
    solutions = sympy.solve((eq1, eq2, eq3), (a, b))
    return solutions

def solveSystem3(eq1, eq2, eq3):
    a, b, c = sympy.symbols('a b c')
    solutions = sympy.solve((eq1, eq2, eq3), (a, b, c))
    return solutions


u=Vector(-1,0,3)
v=Vector(2,-1,1)
w=Vector(1,7,3)
print(coplanar(u,v,w))
plan=Plane(u,v,w)
s=Vector(-9,-4,0)
print(inPlane(s,plan))