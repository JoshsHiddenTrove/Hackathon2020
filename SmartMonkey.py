import random

Genes = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Number of individuals in each generation 
Pop = 500
  
# Target string to be generated 
Goal = "plzzzzzz"

#crossover chance of genes
crossOver =.9

#how many generations between prints
NPrint=2 
    
class Individual(): 
    #Class representing individual in population 
    def __init__(self,chromo,nGen=1,cFactor=.5,mutationF = .10,userString = "HelloWorld",pop = 500): 
        self.chromosome = chromo  
        self.fitness = self.cal_fitness()
        self.fitness = self.cal_fitness()
        self.nPrint = nGen
        self.CrossoverFactor =cFactor
        self.mutationFactor=1-mutationF
        self.goalState=userString
        self.populationSize = pop

    
    def setMutationFactor(self,newM):
        self.mutationFactor= 1-newM
        
    def getMutationFactor(self):
        return self.mutationFactor

    def setPopSize(self,newPop):
        self.populationSize = newPop
    
    def getPopSize(self):
        return self.populationSize
    
    def getGoalState(self):
        return self.goalState
    
    def setGoalState(self,newGoal):
        self.goalState = newGoal
        
    def setNPrint(self,count):
        self.nPrint = count
        
    def getNprint(self):
        return self.nPrint

    @classmethod
    def mutated_genes(self): 
        #create random genes for mutation 
        return random.choice(Genes)  
  
    @classmethod
    def create_gnome(self): 
        #create chromosome or string of genes 
        gnome_len = len(Goal) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    def mate(self, par2): 
        #Perform mating and produce new offspring   
        # chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
  
            # random probability   
            prob = random.random() 
  
            # insert gene from parent 1  
            if prob < self.CrossoverFactor/2: 
                child_chromosome.append(gp1) 
  
            # insert gene from parent 2 
            elif prob < self.CrossoverFactor: 
                child_chromosome.append(gp2) 
  
            # otherwise insert random gene(mutate),  
            # for maintaining diversity 
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        # create new Individual(offspring) using  
        # generated chromosome for offspring 
        return Individual(child_chromosome) 
  
    def cal_fitness(self):  
        #Calculate fittness score, it is the number of 
        #characters in string which differ from target 
        #string. 
        fitness = 0
        for gs, gt in zip(self.chromosome, Goal): 
            if gs != gt: fitness+= 1
        return fitness 
  
# Driver code 
    def main(self):   
        #current generation 
        generation = 1

        found = False
        population = [] 

        # create initial population 
        for _ in range(self.populationSize): 
                    gnome = self.create_gnome() 
                    population.append(Individual(gnome)) 

        while not found: 
            if(generation == 25*NPrint):
                break
            # sort the population in increasing order of fitness score 
            population = sorted(population, key = lambda x:x.fitness) 

            # if the individual having lowest fitness score ie.  
            # 0 then we know that we have reached to the target 
            # and break the loop 
            if population[0].fitness <= 0: 
                found = True
                break

            # Otherwise generate new offsprings for new generation 
            new_generation = [] 

            # Perform Elitism, that mean 10% of fittest population 
            # goes to the next generation 
            s = int((10*self.populationSize)/100) 
            new_generation.extend(population[:s]) 

            # From 50% of fittest population, Individuals  
            # will mate to produce offspring 
            s = int((90*self.populationSize)/100) 
            for _ in range(s): 
                parent1 = random.choice(population[:50]) 
                parent2 = random.choice(population[:50]) 
                child = parent1.mate(parent2) 
                new_generation.append(child) 

            population = new_generation 
            if(generation % NPrint == 0):
                print("Generation:", generation,"Monkies so far ","".join(population[0].chromosome), "Fitness: ",population[0].fitness,"/",len(Goal))

            generation += 1


        print("Generation: {}\tString: {}\tFitness: {}".
            format(generation, 
            "".join(population[0].chromosome), 
            population[0].fitness)) 
  
if __name__ == '__main__': 
    Pop = input("how many monkies can you afford? (big = better)")
    Goal = input("what you wanna out of the monkeys fir (some txt)")
    crossover = input("How colaborative are the monkies?(0.01 to 0.99)")
    crossOver = 1-float(crossover)
    np = input("how often should you check up on the monkies?(some int)")
    NPrint=int(np)
    f=Individual("test")
    f.main() 



