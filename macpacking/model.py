from abc import ABC, abstractmethod
from typing import Iterator
from . import WeightStream, WeightSet, Solution


class BinPacker(ABC):
    pass


class Online(BinPacker):

    def __call__(self, ws: WeightStream):
        capacity, stream = ws
        return self._process(capacity, stream)

    @abstractmethod
    def __init__(self):
        pass

    def counting_compares(self):
        return self.count

    @abstractmethod
    def _process(self, c: int, stream: Iterator[int]) -> Solution:
        pass


class Offline(BinPacker):

    def __call__(self, ws: WeightSet):
        capacity, weights = ws
        return self._process(capacity, weights)

    @abstractmethod
    def __init__(self):
        pass

    def counting_compares(self):
        return self.count

    @abstractmethod
    def _process(self, c: int, weights: list[int]) -> Solution:
        pass


class Multiway(BinPacker):

    def __call__(self, ws: WeightSet, bin_num: int):
        return self._process(ws, bin_num)

    @abstractmethod
    def __init__(self):
        pass

    def counting_compares(self):
        return self.count

    @abstractmethod
    def _process(self, weights: list[int], bin_num: int) -> Solution:
        pass
