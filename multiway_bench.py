import pyperf
from os import listdir
from os.path import isfile, join, basename

from macpacking.reader import BinppReader, JburkardtReader
from macpacking.factory import BinPackerFactory
from macpacking.model import BinPacker
from benchtools.optimal_vals import OptimalValues
from benchtools.case_reader import list_files, group_jburkardt_files


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
N4_CASES = './_datasets/binpp/N4C2W2'
N2_CASES = './_datasets/binpp/N2C3W4'
HARD_CASES = './_datasets/binpp-hard'
JBURKARDT_CASES = './_datasets/jburkardt'

optimal_binpp = {}
optimal_binpp_hard = {}
optimal_jbur = {}


def main():

    global optimal_binpp, optimal_binpp_hard, optimal_jbur

    algorithms = ['MNF', 'MFF', 'MBF', 'MWF', 'BenMaierM']

    runner = pyperf.Runner()

    optimals = OptimalValues()
    optimal_binpp = optimals.binpp
    optimal_binpp_hard = optimals.binpp_hard
    optimal_jbur = optimals.jburkardt

    binpp_cases = [list_files(N4_CASES), list_files(N2_CASES), list_files(HARD_CASES)]
    run_binpp_bench(runner, binpp_cases, algorithms)

    jburkardt_cases = group_jburkardt_files(list_files(JBURKARDT_CASES))
    run_jburkardt_bench(runner, jburkardt_cases, algorithms)


def run_binpp_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:

    # runner = pyperf.Runner()
    # print(cases)
    for case in cases:
        for casefile in case:
            name = basename(casefile)
            numbins: int = None
            if name[:4] == "HARD":
                numbins: int = optimal_binpp_hard[basename(casefile)[:-8]]
            else:
                numbins: int = optimal_binpp[basename(casefile)[:-8]]
            name += " multiway"
            data = BinppReader(casefile).multiway()
            for algo in off_algorithms:
                binpacker = BinPackerFactory.build(algo)
                runner.bench_func(name + " " + algo, binpacker, data, numbins)


def run_jburkardt_bench(runner, cases: list[str], on_algorithms: list[BinPacker]) -> None:

    # print(trios)
    for case in cases:
        name = basename(case[0])[:3]
        numbins: int = optimal_jbur[name]
        name += " multiway"
        data = JburkardtReader(case[0], case[1]).multiway()
        for algo in on_algorithms:
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data, numbins)


if __name__ == "__main__":

    main()
