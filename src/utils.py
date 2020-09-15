import variables
from variables import CODED_CITIES, DISTANCES, STABILITY_MAX, STABILITY_PERC


def reached_stability(generation):
    c_min_dist = get_total_distance(generation[0])
    c_diff = c_min_dist / (variables.stability_base_pnt or variables.distance_min)

    if c_min_dist < variables.distance_min:
        variables.distance_min = c_min_dist

    if c_diff >= (1 - STABILITY_PERC) and c_diff <= (1 + STABILITY_PERC):
        variables.stability_cnt += 1

        if variables.stability_cnt == 1:
            variables.stability_base_pnt = c_min_dist
    else:
        variables.stability_cnt = 0
        variables.stability_base_pnt = None

    return variables.stability_cnt == STABILITY_MAX


def get_named_route(route):
    route += '9'

    return ' -> '.join([CODED_CITIES.get(city) for city in route])


def get_total_distance(route):
    distance = 0

    for ind, city in enumerate(route):
        distance += _get_distance(city + route[ind + 1 if ind + 1 < len(route) else 0])

    return distance


def _get_distance(cities):
    return DISTANCES.get(cities) or DISTANCES.get(cities[::-1])
