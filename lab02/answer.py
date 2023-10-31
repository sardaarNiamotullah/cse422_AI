import random

numOfPlayers, target = map(int, input().split())
playersName = []
playersRun = []
for _ in range(numOfPlayers):
    name, runs = input().split()
    playersRun.append(int(runs))
    playersName.append(name)

def initialize_population(num_playersRun):
    population = []
    for _ in range(num_playersRun):
        chromosome = [random.randint(0, 1) for _ in range(num_playersRun)]
        population.append(chromosome)
    return population

def fitness(chromosome, playersRun, target):
    total_runs = sum([chromosome[i] * playersRun[i] for i in range(len(chromosome))])
    return abs(target - total_runs)

def crossover(parent1, parent2):
    split_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    return child1, child2

def mutate(chromosome, mutationRate):
    for i in range(len(chromosome)):
        if random.random() < mutationRate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def genetic_algorithm(playersRun, target, popSize, maxGen, mutationRate):
    num_playersRun = len(playersRun)
    population = initialize_population(num_playersRun)

    for generation in range(maxGen):
        population = sorted(population, key=lambda x: fitness(x, playersRun, target))
        best_chromosome = population[0]

        if fitness(best_chromosome, playersRun, target) == 0:
            return best_chromosome

        new_population = [best_chromosome]

        while len(new_population) < popSize:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutationRate)
            child2 = mutate(child2, mutationRate)
            new_population.extend([child1, child2])

        population = new_population

    return None

popSize = 100
maxGen = 1000
mutationRate = 0.01
result = genetic_algorithm(playersRun, target, popSize, maxGen, mutationRate)

if result is None:
    print(playersName)
    print("-1")
else:
    print(playersName)
    print("".join(map(str, result)))