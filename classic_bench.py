import pyperf
from os import listdir
from os.path import isfile, join, basename

from macpacking.reader import BinppReader, JburkardtReader
from macpacking.factory import BinPackerFactory
from macpacking.model import BinPacker
from benchtools.case_reader import list_files, group_jburkardt_files


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
N4_CASES = './_datasets/binpp/N4C2W2'
N2_CASES = './_datasets/binpp/N2C3W4'
HARD_CASES = './_datasets/binpp-hard'
JBURKARDT_CASES = './_datasets/jburkardt'


def main():

    off_algorithms = ['NF_Off', 'FFDesc', 'BFDesc', 'WFDesc', 'BenMaier']
    on_algorithms = ['NF_On', 'FF', 'BF', 'WF', 'RFF']

    runner = pyperf.Runner()

    binpp_cases = [list_files(N4_CASES), list_files(N2_CASES), list_files(HARD_CASES)]
    run_off_binpp_bench(runner, binpp_cases, off_algorithms)
    run_on_binpp_bench(runner, binpp_cases, on_algorithms)

    jburkardt_cases = group_jburkardt_files(list_files(JBURKARDT_CASES))
    run_off_jburkardt_bench(runner, jburkardt_cases, off_algorithms)
    run_on_jburkardt_bench(runner, jburkardt_cases, on_algorithms)


def run_off_binpp_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:

    for case in cases:
        for casefile in case:
            name = basename(casefile) + " offline"
            data = BinppReader(casefile).offline()
            for algo in off_algorithms:
                binpacker = BinPackerFactory.build(algo)
                runner.bench_func(name + " " + algo, binpacker, data)


def run_on_binpp_bench(runner, cases: list[str], on_algorithms: list[BinPacker]) -> None:

    for case in cases:
        for casefile in case:
            name = basename(casefile) + " online"
            data = BinppReader(casefile).online()
            for algo in on_algorithms:
                binpacker = BinPackerFactory.build(algo)
                runner.bench_func(name + " " + algo, binpacker, data)


def run_off_jburkardt_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:

    for case in cases:
        name = basename(case[0])[:3] + " offline"
        data = JburkardtReader(case[0], case[1]).offline()
        for algo in off_algorithms:
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data)


def run_on_jburkardt_bench(runner, cases: list[str], on_algorithms: list[BinPacker]) -> None:

    for case in cases:
        name = basename(case[0])[:3] + " online"
        data = JburkardtReader(case[0], case[1]).online()
        for algo in on_algorithms:
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data)


if __name__ == "__main__":

    main()
