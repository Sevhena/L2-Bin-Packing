from .. import Solution, WeightSet
from ..model import Multiway
from .offline import NextFit as NFD, FirstFitDecreasing as FFD,\
        BestFitDecreasing as BFD, WorstFitDecreasing as WFD

itr = 10


class MultiNextFit(Multiway):

    def __init__(self):
        self.count = itr

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)
        upper_bound = max(2*sum_values/numbins, max_values)

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = NFD()
            self.count += algo.counting_compares()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = NFD()
        solution = algo((upper_bound, weights))
        self.count += algo.counting_compares()
        return solution


class MultiFirstFit(Multiway):

    def __init__(self):
        self.count = itr

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)
        upper_bound = max(2*sum_values/numbins, max_values)

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = FFD()
            self.count += algo.counting_compares()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo: Multiway = FFD()
        solution = algo((upper_bound, weights))
        self.count += algo.counting_compares()
        return solution


class MultiBestFit(Multiway):

    def __init__(self):
        self.count = itr

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)
        upper_bound = max(2*sum_values/numbins, max_values)

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = BFD()
            result = algo((c, weights))
            self.count += algo.counting_compares()
            bins = len(result)
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo: Multiway = BFD()
        solution = algo((upper_bound, weights))
        self.count += algo.counting_compares()
        return solution


class MultiWorstFit(Multiway):

    def __init__(self):
        self.count = itr

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)
        upper_bound = max(2*sum_values/numbins, max_values)

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = WFD()
            self.count += algo.counting_compares()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = WFD()
        solution = algo((upper_bound, weights))
        self.count += algo.counting_compares()
        return solution
