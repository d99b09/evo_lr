import numpy as np
import random
from lr1 import Evo
from tqdm import tqdm

class Evo2:
    def __init__(self, length=1000, max_generation=500, num_of_offsprings=20):
        #super(Evo2, self).__init__(length)
        self.max_generation = max_generation
        self.num_of_offsprings = num_of_offsprings
        self.length = length
        self.fun1 = lambda x: (x[0] - 2)**2/2 + (x[1] + 1)**2/13 +3
        self.fun2 = lambda x: (x[0] + x[1] - 3)**2/36 + (-x[0] + x[1] +2)**2/8 - 17
        self.fun3 = lambda x: (3*x[0] - 2*x[1] - 1)**2/175 + (-x[0] + 2*x[1])**2/17 - 13
        self.fun_list = [self.fun1, self.fun2, self.fun3]
        self.x_max = 4
        self.x_min = -4

    def new_generation(self):
        return 4*np.random.uniform(-1, 1, (self.length, 2))

    def mutation(self, generation):
        return generation

    def crossingover(self, offsprings):
        alph = 0.1

        while len(offsprings) < self.max_generation:
            p1 = offsprings[np.random.randint(len(offsprings))]
            p2 = offsprings[np.random.randint(len(offsprings))]

            if p1 < p2:
                p = np.random.uniform(p1 - alph * (p2 - p1), p2 + alph * (p2 - p1))
            else:
                p = np.random.uniform(p2 - alph * (p1 - p2), p1 + alph * (p1 - p2))
                offsprings = np.vstack((offsprings, p))
        new_generation = offsprings
        return new_generation

    def crossingover2(self, offsprings):
        while len(offsprings) < self.max_generation:
            p1 = offsprings[np.random.randint(len(offsprings))]
            p2 = offsprings[np.random.randint(len(offsprings))]
            p = (p1 + p2)/2
            offsprings = np.vstack((offsprings, p))
        new_generation = offsprings
        return new_generation

    def next_generation(self, generation):
        #step 1
        offsprings_list = []
        for fun in self.fun_list:
            offspring = self.select(fun, generation)
            offsprings_list.append(offspring)
        #step 2
        offsprings = []
        offsprings = np.vstack((e for e in offsprings_list))


        #step 3
        generation = self.crossingover2(offsprings)

        #step 4

        return generation


    def select(self, fun, arr):
        ls = []
        for e in arr:
            ls += list(e)
        sortes_ls = sorted(ls, key=fun)[:self.num_of_offsprings]
        sorted_array = np.array(sortes_ls)
        sorted_array.reshape((-1,1))
        return np.reshape(sorted_array, (-1, 1))

    def evolution(self):
        generation = self.new_generation()
        #self.z(generation)
        for _ in range(self.max_generation):
            generation = self.next_generation(generation)

        return generation

    def z(self, generation):
        #x**2
        z1 = self.fun1(generation)
        z2 = self.fun2(generation)
        z3 = self.fun3(generation)
        z4 = z1 + z2 + z3

        return np.hstack((z1, z2, z3, z4))


class Evo_test:
    def __init__(self, length=1000, max_generation=500, num_of_offsprings=20):
        self.max_generation = max_generation
        self.num_of_offsprings = num_of_offsprings
        self.length = length
        self.fun1 = lambda x: x**2
        self.fun2 = lambda x: (x - 2)**2
        self.fun_list = [self.fun1, self.fun2]

    def new_generation(self):
        return 10*np.random.uniform(-1, 1, (self.length, 1))

    def mutation(self, generation):
        return generation

    def crossingover(self, offsprings):
        alph = 0.1

        while len(offsprings) < self.max_generation:
            p1 = offsprings[np.random.randint(len(offsprings))]
            p2 = offsprings[np.random.randint(len(offsprings))]

            if p1 < p2:
                p = np.random.uniform(p1 - alph * (p2 - p1), p2 + alph * (p2 - p1))
            else:
                p = np.random.uniform(p2 - alph * (p1 - p2), p1 + alph * (p1 - p2))
                offsprings = np.vstack((offsprings, p))
        new_generation = offsprings
        return new_generation

    def crossingover2(self, offsprings):
        while len(offsprings) < self.max_generation:
            p1 = offsprings[np.random.randint(len(offsprings))]
            p2 = offsprings[np.random.randint(len(offsprings))]
            p = (p1 + p2)/2
            offsprings = np.vstack((offsprings, p))
        new_generation = offsprings
        return new_generation

    def next_generation(self, generation):
        #step 1
        offsprings_list = []
        for fun in self.fun_list:
            offspring = self.select(fun, generation)
            offsprings_list.append(offspring)
        #step 2
        offsprings = []
        offsprings = np.vstack((e for e in offsprings_list))


        #step 3
        generation = self.crossingover2(offsprings)

        #step 4

        return generation


    def select(self, fun, arr):
        ls = []
        for e in arr:
            ls += list(e)
        sortes_ls = sorted(ls, key=fun)[:self.num_of_offsprings]
        sorted_array = np.array(sortes_ls)
        sorted_array.reshape((-1,1))
        return np.reshape(sorted_array, (-1, 1))

    def evolution(self):
        generation = self.new_generation()
        #self.z(generation)
        for _ in tqdm(range(self.max_generation)):
            generation = self.next_generation(generation)

        return generation

    def z(self, generation):
        #x**2
        z1 = self.fun1(generation)
        z2 = self.fun2(generation)
        z3 = z1 + z2

        return np.hstack((z1, z2, z3))



evo = Evo2(500, max_generation=1000)
print(evo.fun1([1, 2]))
# z = evo.z(final_gen)

print(final_gen)


