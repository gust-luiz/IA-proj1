from random import shuffle

from variables import POPULATION_SZ, distance_min
from utils import get_total_distance


def get_initial_generation():
    population = []

    for _ in range(POPULATION_SZ):
        another_cities = list(map(str, range(9)))
        shuffle(another_cities)
        population.append(''.join(['9', *another_cities]))

    return population


def get_next_generation(current, new):
    return current


def fitness(generation):
    calculed = list(map(_calc_fitness, generation))
    calculed.sort(key = lambda x: x[1])

    return [c[0] for c in calculed]


def crossover(generation):
    return []


def mutation(generation):
    return []


def _calc_fitness(route):
    return route, get_total_distance(route) / distance_min
