from shapely import Polygon, Point


def is_in_polygon(poly, point):
    polygon = Polygon(poly)
    return polygon.contains(Point(point)) or polygon.intersects(Point(point))
