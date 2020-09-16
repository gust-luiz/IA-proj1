from random import shuffle

import variables
from variables import (CODED_CITIES, DISTANCES, STABILITY_MAX, STABILITY_PERC,
                       avg_distance, distance_range)


def reached_stability(generation):
    if not avg_distance:
        return False

    c_diff = distance_range / avg_distance

    if c_diff >= (1 - STABILITY_PERC) and c_diff <= (1 + STABILITY_PERC):
        variables.stability_cnt += 1
    else:
        variables.stability_cnt = 0

    return variables.stability_cnt == STABILITY_MAX


def get_named_route(route):
    route += '9'

    return ' -> '.join([CODED_CITIES.get(city) for city in route])


def get_total_distance(route):
    distance = 0

    for ind, city in enumerate(route):
        distance += _get_distance(city + route[ind + 1 if ind + 1 < len(route) else 0])

    return distance


def rm_duplicates(route):
    unique = list(set(list(route)))
    rest = [num for num in map(str, range(len(CODED_CITIES))) if num not in unique]

    if not rest:
        return ''.join(route)

    shuffle(rest)

    for i, c in enumerate(route):
        route[i] = c if route.count(c) == 1 or (route.count(c) > 1 and not rest) else rest.pop()

    return ''.join(route)


def _get_distance(cities):
    return DISTANCES.get(cities) or DISTANCES.get(cities[::-1])
