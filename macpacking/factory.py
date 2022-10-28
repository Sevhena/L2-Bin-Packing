import macpacking.algorithms.offline as off_algo
import macpacking.algorithms.online as on_algo
from macpacking.model import BinPacker

class BinPackerFactory():

    @staticmethod
    def build(name: str) -> BinPacker:
        selected = None
        match name:
            case 'NF_On':
                selected = on_algo.NextFit()
            case 'NF_Off':
                selected = off_algo.NextFit()
            case 'FF':
                selected = on_algo.FirstFit()
            case 'FFDesc':
                selected = off_algo.FirstFitDecreasing()
            case 'BF':
                selected = on_algo.BestFit()
            case 'BFDesc':
                selected = off_algo.BestFitDecreasing()
            case 'WF':
                selected = on_algo.WorstFit()
            case 'WFDesc':
                selected = off_algo.WorstFitDecreasing()
            case _:
                raise ValueError(name)
        return selected