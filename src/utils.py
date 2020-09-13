from variables import CODED_CITIES, DISTANCES


def reached_stability(generation):
    return False


def get_named_route(route):
    return ' -> '.join([CODED_CITIES.get(city) for city in route])


def get_total_distance(route):
    distance = 0

    for ind, city in enumerate(route):
        distance += _get_distance(city + route[ind + 1 if ind + 1 < len(route) else 0])

    return distance


def _get_distance(cities):
    return DISTANCES.get(cities) or DISTANCES.get(cities[::-1])
