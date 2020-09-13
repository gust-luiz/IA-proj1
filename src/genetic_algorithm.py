from random import shuffle

from variables import POPULATION_SZ


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
    return generation


def crossover(generation):
    return []


def mutation(generation):
    return []
