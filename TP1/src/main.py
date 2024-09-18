from Rectangle import Rectangle
from Triangle import Triangle
from Cercle import Cercle
from Point import Point

def principal():
    """
    This is a test function for the classes
    :return:
    """
    # Point
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(5, 6)
    print(p1)
    print(p2)
    print(p1.distancePoint(point=p2))
    print(p2.distanceCoordonnees(4, 6))

    # Cercle
    c1 = Cercle(5, p2)
    c2 = Cercle(2)

    print(c1)
    print(f"Le cercle c1 contient le point p1: {c1.dansCercle(p1)}")
    print(f"Le cercle c1 contient le point p2: {c1.dansCercle(p2)}")

    print(c2)
    print(f"Le cercle c2 contient le point p1: {c2.dansCercle(p1)}")
    print(f"Le cercle c2 contient le point p2: {c2.dansCercle(p2)}")

    # Rectangle
    r1 = Rectangle(point_bg=p1, point_hd=p2)
    r2 = Rectangle(point_bg=p2, longueur_x=5, longueur_y=7)

    print(r1)
    print(f"Le rectangle r1 contient le point p3: {r1.pointDansRectangle(p3)}")

    print(r2)
    print(f"Le rectangle r2 contient le point p3: {r2.pointDansRectangle(p3)}")

    # Triangle
    tp1 = Point(1, 1)
    t1 = Triangle(5, 4, tp1)

    print(t1)
    print(f"La surface du triangle t1 est: {t1.surface()}")
    print(f"le perimetre du triangle t1 est: {t1.perimetre()}")
    print(f"L'hypotenuse du triangle t1 est: {t1.hypothenuse()}")
    print(f"Le rectangle est isocèle: {t1.isisocele()}")



if __name__ == "__main__":
    principal()