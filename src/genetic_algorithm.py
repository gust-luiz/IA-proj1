from random import shuffle, sample, randint

from variables import POPULATION_SZ, CROSSOVER_PBTY, MUTATION_PBTY, distance_min
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
    generation_mutated = generation.copy()
    qtd = round(MUTATION_PBTY * len(generation))
    individuals_index = sample(range(len(generation)), qtd)
    print(individuals_index)

    for i in individuals_index:        
        old_gene_index = randint(1, 9) #first and last gene not included
        old_gene = generation_mutated[old_gene_index]
        new_gene = str(randint(0,8))
        while new_gene == old_gene: # get guarantee that new_gene is different from old_gene
            new_gene = str(randint(0,8))
        new_gene_index = generation_mutated[i].find(new_gene)
        individual = list(generation_mutated[i])
        individual[old_gene_index], individual[new_gene_index] = individual[new_gene_index], individual[old_gene_index]
        generation_mutated[i] = ''.join(individual)

    return generation, generation_mutated


def _calc_fitness(route):
    return route, get_total_distance(route) / distance_min
