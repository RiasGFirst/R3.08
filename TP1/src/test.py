from TP1.src.Point import Point


def test_distance_coor():
    assert Point(0, 0).distancePoint(Point(1, 0)) == 1


test_distance_coor()