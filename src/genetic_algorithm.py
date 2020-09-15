from random import choice, randint, random, sample, shuffle

from utils import get_total_distance
from variables import (CHILDREN_PER_COUPLE_RANGE, CODED_CITIES, CROSSOVER_PBTY,
                       MUTATION_PBTY, POPULATION_SZ, distance_min)


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


'''def selection(generation):
    n_selected = round(CROSSOVER_PBTY * len(generation)) # number of individuals to create couples
    if n_selected % 2 != 0: # check if number is even
        n_selected += 1

    return generation[0:n_selected]'''

def crossover(generation):
    new_individuals = []
    # half_gen_sz = len(generation) / 2
    options = [
        _crossover_order1,
        # _crossover_2_point
    ]

    for ind in range(0, len(generation), 2):
    # for ind in range(0, half_gen_sz):
        if random() >= CROSSOVER_PBTY:
            continue

        new_individuals.extend(choice(options)(generation[ind], generation[ind + 1]))
        # new_individuals.extend(choice(options)(generation[ind], generation[half_gen_sz + ind]))

    return new_individuals


def mutation(generation):
    individuals_mutated = []
    generation_mutated = generation.copy()

    for id, individual in enumerate(generation_mutated):
        if random() <= MUTATION_PBTY:
            gene_a_idx, gene_b_idx = (int(n) for n in sample(range(1, 10), 2))
            old_gene = individual[gene_a_idx]
            new_gene = individual[gene_b_idx]

            individual_list = list(individual)
            individual_list[gene_a_idx], individual_list[gene_b_idx] = new_gene, old_gene

            individuals_mutated.append(''.join(individual_list))

            generation_mutated[id] = ''.join(individual_list)

    return individuals_mutated, generation_mutated


def _crossover_2_point(parent_a, parent_b):
    new_individuals = []
    son_a = list(parent_a)
    son_b = list(parent_b)

    points = sorted(sample(range(1, 9), 2))

    idx_changes = []
    for i in range(points[0]+1, points[-1]+1):
        # Verify if the number inside the crossover range already exists in the range outside the crossover
        # range in the other parent
        if ((parent_a[0:points[0]+1].find(parent_b[i]) == -1) and
                (parent_a[points[-1]+1:].find(parent_b[i]) == -1) and
                (parent_b[0:points[0]+1].find(parent_a[i]) == -1) and
                (parent_b[points[-1]+1:].find(parent_a[i]) == -1)):
            son_a[i], son_b[i] = parent_b[i], parent_a[i]
            idx_changes.append(i)

    # Checking if the changes don't create repetition. Otherwise, undo the change.
    for i in idx_changes:
        if son_a.count(son_a[i]) > 1:
            son_a[i], son_b[i] = parent_a[i], parent_b[i]

    # Add to son list if it is different from parents
    if (son_a != list(parent_a)) and (son_b != list(parent_b)):
        # print("TROCOU!!")
        new_individuals.append(''.join(son_a))
        new_individuals.append(''.join(son_b))

    return new_individuals


def _crossover_order1(parent_a, parent_b):
    cities_cnt = len(CODED_CITIES)
    new_individuals = []

    for _ in range(randint(*CHILDREN_PER_COUPLE_RANGE)):
        inds = sample(range(1, cities_cnt), 2)
        inds.sort()

        fixed = list(map(int, choice([parent_a, parent_b])[inds[0]: inds[1] + 1]))
        rest = [num for num in range(cities_cnt) if num not in fixed and num != 9]
        shuffle(rest)
        new = [fixed.pop() if ind >= inds[0] and ind <= inds[1] else rest.pop() for ind in range(1, cities_cnt)]
        new_individuals.append(''.join(['9', *list(map(str, new))]))

    return new_individuals


def _calc_fitness(route):
    return route, get_total_distance(route) / distance_min
