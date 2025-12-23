import random
import string
import time
import os

# ==========================================
# GENE-WEAVER: CONFIGURATION (GOD SETTINGS)
# ==========================================
TARGET_DNA = "GENE-WEAVER: FINAL SUPREMACY"  # The Perfect Organism
POPULATION_SIZE = 200     # How many minions per generation
MUTATION_RATE = 0.01      # 1% chance of random mutation
ELITISM = True            # Keep the best organism alive forever?
# ==========================================

GENES = string.ascii_letters + string.punctuation + " "

def generate_random_dna(length):
    return ''.join(random.choice(GENES) for _ in range(length))

def calculate_fitness(dna):
    score = 0
    for i in range(len(TARGET_DNA)):
        if dna[i] == TARGET_DNA[i]:
            score += 1
    return score

def crossover(parent1, parent2):
    # Breeding: Take half from dad, half from mom
    midpoint = random.randint(0, len(TARGET_DNA) - 1)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child

def mutate(dna):
    # The "Cancer" factor: Random changes
    dna_list = list(dna)
    for i in range(len(dna_list)):
        if random.random() < MUTATION_RATE:
            dna_list[i] = random.choice(GENES)
    return ''.join(dna_list)

def run_engine():
    # Genesis: Create initial random chaos
    population = [generate_random_dna(len(TARGET_DNA)) for _ in range(POPULATION_SIZE)]
    generation = 1
    
    found = False
    
    while not found:
        # 1. Natural Selection (Sort by Fitness)
        population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)
        
        # 2. Visualization (The "God" View)
        best_specimen = population[0]
        max_score = calculate_fitness(best_specimen)
        
        os.system('clear') # Use 'cls' if on Windows, 'clear' for Termux
        print(f"GENE-WEAVER: EVOLUTION ENGINE // GEN {generation}")
        print("==================================================")
        print(f"TARGET: {TARGET_DNA}")
        print(f"BEST  : {best_specimen}")
        print(f"MATCH : {((max_score/len(TARGET_DNA))*100):.2f}%")
        print("==================================================")
        
        # Check if we achieved Supremacy
        if best_specimen == TARGET_DNA:
            print("\n[!] CONSTRUCT COMPLETED.")
            print("[!] SUPREMACY ACHIEVED.")
            break

        # 3. Breeding the Next Generation
        new_population = []
        
        # Elitism: Keep the king?
        if ELITISM:
            new_population.append(population[0])
            
        # Fill the rest
        while len(new_population) < POPULATION_SIZE:
            # Select top 50% to breed
            parent1 = random.choice(population[:int(POPULATION_SIZE/2)])
            parent2 = random.choice(population[:int(POPULATION_SIZE/2)])
            
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
            
        population = new_population
        generation += 1
        time.sleep(0.05) # Slow down to watch it happen

if __name__ == "__main__":
    run_engine()

