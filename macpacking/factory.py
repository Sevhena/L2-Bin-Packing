import macpacking.algorithms.offline as off_algo
import macpacking.algorithms.online as on_algo
import macpacking.algorithms.multiway as multi_algo
import macpacking.algorithms.baseline as base
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
            case 'MNF':
                selected = multi_algo.MultiNextFit()
            case 'FF':
                selected = on_algo.FirstFit()
            case 'RFF':
                selected = on_algo.RefinedFirstFit()
            case 'FFDesc':
                selected = off_algo.FirstFitDecreasing()
            case 'MFF':
                selected = multi_algo.MultiFirstFit()
            case 'BF':
                selected = on_algo.BestFit()
            case 'BFDesc':
                selected = off_algo.BestFitDecreasing()
            case 'MBF':
                selected = multi_algo.MultiBestFit()
            case 'WF':
                selected = on_algo.WorstFit()
            case 'WFDesc':
                selected = off_algo.WorstFitDecreasing()
            case 'MWF':
                selected = multi_algo.MultiWorstFit()
            case 'BenMaier':
                selected = base.BenMaier()
            case 'BenMaierM':
                selected = base.BenMaierM()
            case _:
                raise ValueError(name)
        return selected
