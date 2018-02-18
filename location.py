from geopy.geocoders import ArcGIS


def get_loc(loc):
    """
    (str) -> tuple(float, float)
    Function gets place and returns its coordinates

    param loc: string that is place where the film was filmed
    return: tuple of two floats that are longitude and latitude

    >>> get_loc("North Hollywood, Los Angeles, California, USA")
    (34.17, -118.379)
    >>> get_loc("Jo's Cafe, San Marcos, Texas, USA")
    (29.886, -97.928)
    """
    # print(loc)
    if loc:
        location = ArcGIS(timeout=10)
        place = location.geocode(loc)
        return round(place.latitude, 3), round(place.longitude, 3)


if "__main__" == __name__:
    import doctest

    doctest.testmod()
