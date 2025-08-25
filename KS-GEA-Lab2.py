import random

weights = [2, 3, 4, 5]     
values = [3, 4, 5, 6]      
capacity = 5                 
num_items = len(weights)

POP_SIZE = 20
GENERATIONS = 10
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1

def fitness(individual):
    """Evaluate fitness of a solution"""
    total_weight = sum(w for w, g in zip(weights, individual) if g == 1)
    total_value = sum(v for v, g in zip(values, individual) if g == 1)
    if total_weight > capacity:
        return 0 
    return total_value

def create_individual():
    """Random binary sequence"""
    return [random.randint(0, 1) for _ in range(num_items)]

def selection(population, fitness_scores):
    """Tournament selection"""
    tournament_size = 3
    selected = random.sample(list(zip(population, fitness_scores)), tournament_size)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

def crossover(parent1, parent2):
    """One-point crossover"""
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, num_items - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1[:], parent2[:]

def mutate(individual):
    """Bit-flip mutation"""
    for i in range(num_items):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

def gene_expression_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]
    best_solution = None
    best_fitness = 0

    for gen in range(GENERATIONS):
        fitness_scores = [fitness(ind) for ind in population]

        for ind, fit in zip(population, fitness_scores):
            if fit > best_fitness:
                best_fitness = fit
                best_solution = ind

        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:POP_SIZE]

        print(f"Generation {gen+1}: Best Fitness = {best_fitness}")

    print("\nBest solution found:")
    print("Items selected:", best_solution)
    print("Maximum value:", best_fitness)

gene_expression_algorithm()
