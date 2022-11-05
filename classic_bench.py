import pyperf
from os import listdir
from os.path import isfile, join, basename

from macpacking.reader import BinppReader, JburkardtReader
from macpacking.factory import BinPackerFactory
from macpacking.model import BinPacker


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

    n4_cases = list_case_files(N4_CASES)
    n2_cases = list_case_files(N2_CASES)
    hard_cases = list_case_files(HARD_CASES)
    binpp_cases = [n4_cases, n2_cases, hard_cases]
    run_off_binpp_bench(runner, binpp_cases, off_algorithms)
    run_on_binpp_bench(runner, binpp_cases, on_algorithms)

    jburkardt_cases = list_case_files(JBURKARDT_CASES)
    run_off_jburkardt_bench(runner, jburkardt_cases, off_algorithms)
    run_on_jburkardt_bench(runner, jburkardt_cases, on_algorithms)


def list_case_files(dir: str) -> list[str]:

    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")])


def run_off_binpp_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:

    # runner = pyperf.Runner()
    # print(cases)
    for case in cases:
        for casefile in case:
            name = basename(casefile) + " offline"
            data = BinppReader(casefile).offline()
            for algo in off_algorithms:
                binpacker = BinPackerFactory.build(algo)
                runner.bench_func(name + " " + algo, binpacker, data)


def run_on_binpp_bench(runner, cases: list[str], on_algorithms: list[BinPacker]) -> None:

    # runner = pyperf.Runner()
    for case in cases:
        for casefile in case:
            name = basename(casefile) + " online"
            data = BinppReader(casefile).online()
            for algo in on_algorithms:
                binpacker = BinPackerFactory.build(algo)
                runner.bench_func(name + " " + algo, binpacker, data)


def run_off_jburkardt_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:

    # runner = pyperf.Runner()
    trios = []
    index, counter = -1, 3
    for case in cases:
        if counter == 3:
            counter = 1
            index += 1
            trios.append([case])
        else:
            trios[index].append(case)
            counter += 1

    # print(trios)
    for trio in trios:
        name = basename(trio[0])[:3] + " offline"
        data = JburkardtReader(trio[0], trio[1], trio[2]).offline()
        for algo in off_algorithms:
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data)


def run_on_jburkardt_bench(runner, cases: list[str], on_algorithms: list[BinPacker]) -> None:

    # runner = pyperf.Runner()
    trios = []
    index, counter = -1, 3
    for case in cases:
        if counter == 3:
            counter = 1
            index += 1
            trios.append([case])
        else:
            trios[index].append(case)
            counter += 1

    # print(trios)
    for trio in trios:
        name = basename(trio[0])[:3] + " online"
        data = JburkardtReader(trio[0], trio[1], trio[2]).online()
        for algo in on_algorithms:
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data)


if __name__ == "__main__":

    main()
