from functools import reduce

def get_genotype_outcomes(genotype_a, geotypeB):
    if len(genotype_a) < 2 or len(genotype_b) < 2:
        return []

    return [
        ''.join(sorted([genotype_a[0], genotype_b[0]])),
        ''.join(sorted([genotype_a[0], genotype_b[1]])),
        ''.join(sorted([genotype_a[1], genotype_b[0]])),
        ''.join(sorted([genotype_a[1], genotype_b[1]])),
    ]

def get_outcome_count_with_dominant_allele(outcomes):
    return len(list(filter(lambda x: x.find('A') > -1, outcomes)))

def get_probabilty_of_genetic_expression(genotypes, genotype_a, genotype_b, total_population_count):
    _genotypes = dict(genotypes)
    
    outcomes = get_genotype_outcomes(genotype_a, genotype_b)
    
    probability_of_expression_a = _genotypes[genotype_a] / total_population_count
    _genotypes[genotype_a] -= 1
    total_population_count -= 1

    probability_of_expression_b = _genotypes[genotype_b] / total_population_count
    _genotypes[genotype_b] -= 1
    total_population_count -= 1
    
    expression_ratio = get_outcome_count_with_dominant_allele(outcomes) / len(outcomes)

    return probability_of_expression_a * probability_of_expression_b * expression_ratio

population = [int(item) for item in input().split()]

total_population_count = reduce(lambda x, y: x + y, population)

if len(population) < 3:
    raise Exception('Error: Three numbers denoting each possible genotype are expected. Exiting...')

genotypes = { 'AA': population[0], 'Aa':population[1], 'aa':population[2] }
overall_probability = 0

for genotype_a in genotypes:
    for genotype_b in genotypes:
        overall_probability += get_probabilty_of_genetic_expression(genotypes, genotype_a, genotype_b, total_population_count)
        
print(overall_probability)

        