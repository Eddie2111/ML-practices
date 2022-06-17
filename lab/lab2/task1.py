import numpy as np;

class GeneticAlgorithm:
    start_population_size   = 10;
    mutation_threshold      = 0.3
    
    def __init__(self,path):
        self.limit, self.n                = 100, -1;
        self.storedData, self.population  = [], [];
        self.report                       = [];
        givenInput                        = open(path,'r');
        record                            = givenInput.readlines();
        
        for x,y in enumerate(record):
            cache_from_source = y[:-1].split();
            if x == 0:
                self.n = int(cache_from_source[0]);
            elif cache_from_source[0] == 'd':
                self.storedData.append( int(cache_from_source[1]) );
            elif cache_from_source[0] == 'l':
                self.storedData.append( int(cache_from_source[1]) * -1 );
                
        self.report.append(self.n);
        self.report.append(self.storedData);
        self.selected_fit = self.target();
        givenInput.close();
        
    def fitness(self):
        n    = [];
        for people in self.population:
            total = 0;
            for i in range(len(people)):
                if people[i] == 1:
                    total += self.storedData[i];
            n.append(total);
        n = np.absolute(np.array(n));
        
        self.report.append(("Population: ", self.population));
        self.report.append(("fitness: ", n));
        
        return n;
    def selection(self,score):
        summation            = np.sum(score);
        probability_limit    = summation - score;
        probability_limit    = probability_limit / np.sum(probability_limit);
        indices     = [];
        
        for i in range(len(self.population)):
            indices.append(i);
        choice = np.random.choice(indices,2,True,probability_limit);

        self.report.append(("total: ", summation));
        self.report.append((choice));
        
        return self.population[choice[0]], self.population[choice[1]];
    
    def crossovers(self,x,y):
        crossovers_rate = np.random.randint(0,self.n);
        child           = np.append(x[:crossovers_rate],y[crossovers_rate:]);
        
        self.report.append(("X: ", x , "\n Y: ", y, "\n Child: ", child));
        self.report.append(("Rate of crossing over: ", crossovers_rate));
        self.report.append(("Current child: ", child));
        
        return child;
    
    def mutation(self,child):
        probability = GeneticAlgorithm.mutation_threshold;
        if np.random.random(1)[0]> probability:
            mutation_rate = np.random.randint(0,self.n);
            mutation_value = np.random.randint(0,2);
            child[mutation_rate] = mutation_value;
            self.report.append(("[Before] Mutation: ", child,mutation_rate,mutation_value));
            self.report.append(("[After] Mutation: ", child));
        return child;

    def target(self):
        self.population = np.random.randint(0,2,(GeneticAlgorithm.start_population_size,self.n));
        for i in range(self.limit):
            reporti = ("GENERATION: ", i);
            self.report.append(reporti);
            new_population = [];
            fitness_scores = self.fitness();
            max_index =np.where (fitness_scores==max(fitness_scores))[0];
            if 0 in fitness_scores:
                index = np.where (fitness_scores==0)[0][0];
                self.report.append(index); 
                self.report.append(self.population[index]);
                if np.all(self.population[index]== 0 ):
                    self.population[index] = self.population[max_index];
                    # At this case generated result is unacceptable, cannot add to report neither use it #
                else:
                    return self.population[index];
            for j in range(GeneticAlgorithm.start_population_size):
                x,y = self.selection(fitness_scores);
                child = self.crossovers(x,y);
                child = self.mutation(child);
                if np.all(child==0):
                    continue;
                new_population.append(child);
            self.population = new_population;
        return np.array([-1]);
    
    def fittest(self):
        if np.any(self.selected_fit == -1):
            return -1;
        main = np.array2string(self.selected_fit, separator='');
        return main[1:-1];
    
    def reports(self):
        for i in self.report:
            print(i);
        return '';
    
def main():
    bankData = GeneticAlgorithm("data1.txt");
    print("Answer: ", bankData.fittest() );
    
main();

        