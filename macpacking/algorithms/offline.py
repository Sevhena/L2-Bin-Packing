from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online, FirstFit as FF_online, BestFit as BF_online, WorstFit as WF_online


class NextFit(Offline):
    
    def __init(self):
        self.count = 0
        
    def counting_compares(self):
        return self.count
    
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        weights = sorted(weights, reverse=True)
        delegation = Nf_online()
        self.count = delegation.counting_compares()
        return delegation((capacity, weights))

class FirstFitDecreasing(Offline):
    
    def __init(self):
        self.count = 0
        
    def counting_compares(self):
        return self.count
    
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = FF_online()
        self.count = delegation.counting_compares()
        return delegation((capacity, weights))

class BestFitDecreasing(Offline):
    
    def __init(self):
        self.count = 0
        
    def counting_compares(self):
        return self.count
        
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = BF_online()
        self.count = delegation.counting_compares()
        return delegation((capacity, weights))

class WorstFitDecreasing(Offline):
    
    def __init(self):
        self.count = 0
        
    def counting_compares(self):
        return self.count
        
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = WF_online()
        self.count = delegation.counting_compares()
        return delegation((capacity, weights))
