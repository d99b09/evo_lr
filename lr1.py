import math as m
from matplotlib import pyplot as plt
import numpy as np
import random as r



a = lambda x: m.sin(5*m.pi*(x**0.75-0.05))**6
a2 = np.vectorize(a)
b = np.arange(0, 1.01, 0.01)
plt.plot(b, a2(b))
# plt.show()


class Evo:
    def __init__(self, length, sigma=0.1, max_generations=100, num_of_offsprings=5):
        self.length = length
        self.sigma = sigma
        self.genes = self.get_random_genes(self.length)
        self.score_arr = None
        self.max_generations = max_generations
        self.num_of_offsprings = num_of_offsprings
        self.current_fun = lambda x: m.sin(5 * m.pi * (x ** 0.75 - 0.05))**6

    # def current_fun(self, x):
    #     return m.sin(5 * m.pi * (x ** 0.75 - 0.05))

    def get_random_genes(self, length, max_generation=500):
        return np.random.rand(length)

    def score(self, generation):
        for i, e in enumerate(generation):
            generation[i][1] = self.current_fun(e[0])
        for i in range(len(generation)):
            nearby_list = []
            for j in range(len(generation)):
                if (generation[j][0] > (generation[i][0] - self.sigma)) and (generation[j][0] < (generation[i][0] +
                                                                                                 self.sigma)):
                    nearby_list.append(generation[j][0])
            curr_fun = np.vectorize(self.current_fun)
            max_nearby = max(curr_fun(nearby_list))
            generation[i][3] = max_nearby
            if max_nearby == generation[i][1]:
                generation[i][2] = 1
            else:
                generation[i][2] = self.dist(generation[i][0], max_nearby)
        for i, e in enumerate(generation):
            generation[i][4] = e[1] - e[2]
        generation = generation[generation[:, 4].argsort()]
        return generation


    def select(self, generation):

        generation = generation[-self.num_of_offsprings:]

        return generation

    def dist(self, x, y):
        x = self.current_fun(x)
        #y = self.current_fun(y)
        #print(x, y)
        return (x**2 + y**2)**(1/2)

    def reproduction(self, offsprings):
        gen1 = []
        gen2 = []
        for _ in range(int((self.length - self.num_of_offsprings)/2)):
            gen1.append([np.random.uniform(0, 1), 0, 0, 0, 0])
        for _ in range(int((self.length - self.num_of_offsprings)/2)):
            gen2.append([self.mutation(offsprings),
                         0, 0, 0, 0])
        gen1 = np.array(gen1)
        gen2 = np.array(gen2)
        return np.vstack((offsprings, gen1, gen2))

    def mutation(self, offsprings):
        a = -1
        while (a < 0) or (a > 1):
            sample = offsprings[np.random.randint(self.num_of_offsprings)][0]
            a = sample + np.random.uniform(-0.1, 0.1)
        return a

    def next_generation(self, generation):
        generation_and_score = self.score(generation)
        offsprings = self.select(generation_and_score)
        generation = self.reproduction(offsprings)
          #generation = generation[generation[:, 0].argsort()]
        #offspring = generation
        return generation


    def evolution(self):
        generation_pre = self.get_random_genes(self.length)
        generation = []
        for i in generation_pre:
            generation.append([i, 0, 0, 0, 0])
        generation = np.array(generation)
        generation_index = 1
        for _ in range(self.max_generations):
            generation = self.next_generation(generation)
        return self.score(generation)



if __name__ == '__main__':
    evo = Evo(45, max_generations=20,
              num_of_offsprings=10)
    generation = evo.evolution()
    gen_list1 = []
    gen_list2 = []

    for i in range(len(generation)):
        #@if generation[i][2] == 1:
        gen_list1.append(generation[i][0])
        gen_list2.append(generation[i][1])

    plt.plot(gen_list1, gen_list2, '+')
    #plt.show()

    result1 = []
    result2 = []
    for gen in generation:
        if gen[2] == 1:
            result1.append(gen[0])
            result2.append(gen[1])
    plt.plot(result1, result2, 'o')
    plt.show()
    print(result1)
    print(result2)



    print(1)

