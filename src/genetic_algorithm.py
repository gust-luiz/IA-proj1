from random import choice, randint, random, sample, shuffle

import variables
from utils import get_total_distance, rm_duplicates
from variables import (CHILDREN_PER_COUPLE_RANGE, CODED_CITIES, CROSSOVER_PBTY,
                       CURRENT_INDV_PERC, MUTATION_PBTY, NEW_INDV_PERC,
                       POPULATION_SZ, distance_min)


def get_initial_generation():
    population = []

    for _ in range(POPULATION_SZ):
        another_cities = list(map(str, range(9)))
        shuffle(another_cities)
        population.append(''.join(['9', *another_cities]))

    return population


def get_next_generation(current, new):
    new_sz = round(POPULATION_SZ * NEW_INDV_PERC)
    current_sz = round(POPULATION_SZ * CURRENT_INDV_PERC)

    next_generation, rest = current[: current_sz], current[current_sz + 1 :]

    if len(new) >= new_sz:
        next_generation.extend(sample(new, k=new_sz))

        return next_generation

    next_generation.extend(new)

    while len(next_generation) < POPULATION_SZ:
        next_generation.append(rest.pop())

    print('next_gen', len(next_generation), next_generation)

    return next_generation


def fitness(generation):
    calculed = []
    average = 0
    min_dist, max_dist = float('inf'), float('-inf')

    for individual in generation:
        total, fitness_value = _calc_fitness(individual)

        average += total
        min_dist = min([min_dist, total])
        max_dist = max([max_dist, total])

        calculed.append([individual, fitness_value])

    variables.current_dist_range = max_dist - min_dist
    variables.avg_distance = average / len(generation)
    variables.distance_min = min([min_dist, variables.distance_min])

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
        _ordered_crossover,
        _uniform_crossover,
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

    for id, individual in enumerate(generation):
        if random() <= MUTATION_PBTY:
            gene_a_idx, gene_b_idx = (int(n) for n in sample(range(1, 10), 2))
            old_gene = individual[gene_a_idx]
            new_gene = individual[gene_b_idx]

            individual_list = list(individual)
            individual_list[gene_a_idx], individual_list[gene_b_idx] = new_gene, old_gene

            individuals_mutated.append(''.join(individual_list))

    return individuals_mutated


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

        new = [fixed.pop(0) if ind >= inds[0] and ind <= inds[1] else rest.pop() for ind in range(1, cities_cnt)]
        new = ''.join(['9', *list(map(str, new))])

        if new not in [parent_a, parent_b]:
            new_individuals.append(new)

    return new_individuals


def _ordered_crossover(parent_a, parent_b):
    cities_cnt = len(CODED_CITIES)
    asc_or_desc = choice([0, -1])
    new_individuals = []

    for _ in range(randint(*CHILDREN_PER_COUPLE_RANGE)):
        inds = sample(range(1, cities_cnt), 2)
        inds.sort()

        fixed = list(map(int, choice([parent_a, parent_b])[inds[0]: inds[1] + 1]))
        rest = [num for num in range(cities_cnt) if num not in fixed and num != 9]
        new = [fixed.pop(0) if ind >= inds[0] and ind <= inds[1] else rest.pop(asc_or_desc) for ind in range(1, cities_cnt)]
        new = ''.join(['9', *list(map(str, new))])

        if new not in [parent_a, parent_b]:
            new_individuals.append(new)

    return new_individuals


def _uniform_crossover(parent_a, parent_b):
    cities_cnt = len(CODED_CITIES)
    new_individuals = []

    for _ in range(randint(*CHILDREN_PER_COUPLE_RANGE)):
        new = []

        for ind in range(cities_cnt):
            new.append(choice([parent_a[ind], parent_b[ind]]))

        new_individuals.append(rm_duplicates(new))

    return new_individuals


def _calc_fitness(route):
    return get_total_distance(route), get_total_distance(route) / distance_min
