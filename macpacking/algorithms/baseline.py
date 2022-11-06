from .. import Solution
from ..model import Multiway, Offline
import binpacking as bp


class BenMaier(Offline):

    def __init__(self):
        self.count = "This is the baseline!"
        
    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_volume(weights, capacity)


class BenMaierM(Multiway):

    def __init__(self):
        self.count = "This is the baseline!"
        
    def counting_compares(self):
        return self.count

    def _process(self, weights: list[int], bin_num: int) -> Solution:
        return bp.to_constant_bin_number(weights, bin_num)
