import numpy as np

from lr1 import Evo

class Evo2:
    def __init__(self, length):
        #super(Evo2, self).__init__(length)
        self.length = length
        self.fun1 = lambda x1, x2: (x1 - 2)**2/2 + (x2 + 1)**2/13 +3
        self.fun2 = lambda x1, x2: (x1 + x2 - 3)**2/36 + (-x1 + x2 +2)**2/8 - 17
        self.fun3 = lambda x1, x2: (3*x1 - 2*x2 - 1)**2/175 + (-x1 + 2*x2)**2/17 - 13

        self.x_max = 4
        self.x_min = -4

    def new_generation(self):
        return 4*np.random.rand(self.length, 2)


class Evo_test:
    def __init__(self, length, max_generation=500, num_of_offsprings=32):
        self.max_generation = max_generation
        self.num_of_offsprings = num_of_offsprings
        self.length = length
        self.fun1 = lambda x: x**2
        self.fun2 = lambda x: (x - 2)**2
        self.fun_list = [self.fun1, self.fun2]

    def next_generation(self, generation):
        #step 1
        offsprings_list = []
        for fun in self.fun_list:
            offspring = self.select(fun, generation)
            offsprings_list.append(offspring)

        offsprings = []
        for offspring in offsprings_list:
            offsprings += offspring



        return generation

    def select(self, fun, ls):
        return sorted(ls, key=fun)[:self.num_of_offsprings]

    def evolution(self):
        generation = None
        for _ in len(self.max_generation):
            generation = self.next_generation(generation)


evo = Evo2(100)
a = evo.new_generation()
b = None
for i in a:
    b[i] = [evo.fun1(i[0], i[1]), evo.fun2(i[0], i[1]), evo.fun3(i[0], i[1])]
print(11121)


