import numpy as np;

class GeneticAlgorithmStrangeBankProblem:
    start_population_size = 10;
    mutation_threshold    = 0.1;
    

def fitness(population, n):
    
  '''calculates the fitness score of each
     of the individuals in the population
     
     returns a 1D numpy array: index referring to 
     ith individual in population, and value referring 
     to the fitness score.'''


  return 

def select(population, fit):
      ''' take input:  population and fit
      fit contains fitness values of each of the individuals 
      in the population  
      
      return:  one individual randomly giving
      more weight to ones which have high fitness score'''
    a = [0,1,2,3,4]
    size = 1
    p = [.31, .29, 0.26, 0.14]
    return 

def crossover(x, y):
      '''take input: 2 parents - x, y. 
     Generate a random crossover point. 
     Append first half of x with second 
     half of y to create the child
     
     returns: a child chromosome'''

  return 

def mutate(child):
      '''take input: a child
     mutates a random 
     gene into another random gene
     
     returns: mutated child'''
  

  return 

def GA(population, n, mutation_threshold = 0.3):
      '''implement the pseudocode here by
     calling the necessary functions- Fitness, 
     Selection, Crossover and Mutation
     
     print: the max fitness value and the 
     chromosome that generated it which is ultimately 
     the solution board'''




  return

'''for 8 queen problem, n = 8'''
n = 8

'''start_population denotes how many individuals/chromosomes are there
  in the initial population n = 8'''
start_population = 10 

'''if you want you can set mutation_threshold to a higher value,
   to increase the chances of mutation'''
mutation_threshold = 0.3

'''creating the population with random integers between 0 to 7 inclusive
   for n = 8 queen problem'''
population = np.random.randint(0, n, (start_population, n))

'''calling the GA function'''
GA(population, n, mutation_threshold)


    