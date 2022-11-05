from .. import Solution, WeightSet
from ..model import Multiway
from .offline import NextFit as NFD, FirstFitDecreasing as FFD, BestFitDecreasing as BFD, WorstFitDecreasing as WFD

itr = 10


class MultiNextFit(Multiway):

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)  # With bin-capacity smaller than this, every packing must use more than `numbins` bins.
        upper_bound = max(2*sum_values/numbins, max_values)  # With this bin-capacity, FFD always uses at most `numbins` bins.

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = NFD()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = NFD()
        return algo((upper_bound, weights))


class MultiFirstFit(Multiway):

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)  # With bin-capacity smaller than this, every packing must use more than `numbins` bins.
        upper_bound = max(2*sum_values/numbins, max_values)  # With this bin-capacity, FFD always uses at most `numbins` bins.

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = FFD()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = FFD()
        return algo((upper_bound, weights))


class MultiBestFit(Multiway):

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)  # With bin-capacity smaller than this, every packing must use more than `numbins` bins.
        upper_bound = max(2*sum_values/numbins, max_values)  # With this bin-capacity, FFD always uses at most `numbins` bins.

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = BFD()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = BFD()
        return algo((upper_bound, weights))


class MultiWorstFit(Multiway):

    def _process(self, weights: WeightSet, numbins: int, iterations=itr) -> Solution:

        sum_values = sum(weights)
        max_values = max(weights)
        lower_bound = max(sum_values/numbins, max_values)  # With bin-capacity smaller than this, every packing must use more than `numbins` bins.
        upper_bound = max(2*sum_values/numbins, max_values)  # With this bin-capacity, FFD always uses at most `numbins` bins.

        for _ in range(iterations):
            c = (lower_bound+upper_bound)/2
            algo = WFD()
            bins = len(algo((c, weights)))
            if bins <= numbins:
                upper_bound = c
            else:
                lower_bound = c

        algo = WFD()
        return algo((upper_bound, weights))
