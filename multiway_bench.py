import pyperf
from os import listdir
from os.path import isfile, join, basename

from macpacking.reader import BinppReader, JburkardtReader
from macpacking.factory import BinPackerFactory
from macpacking.model import BinPacker
from optimal_vals import read_binpp_csv, read_binpp_hard_csv, read_jburkardt_csv


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

    optimal_binpp = read_binpp_csv()
    optimal_binpp_hard = read_binpp_hard_csv()
    optimal_jbur = read_jburkardt_csv()

    binpp_cases = [list_case_files(N4_CASES), list_case_files(N2_CASES), list_case_files(HARD_CASES)] 
    run_binpp_bench(runner, binpp_cases, algorithms)

    jburkardt_cases = list_case_files(JBURKARDT_CASES)
    run_jburkardt_bench(runner, jburkardt_cases, algorithms)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")])

def run_binpp_bench(runner, cases: list[str], off_algorithms: list[BinPacker]) -> None:
    #runner = pyperf.Runner()
    #print(cases)
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
    #runner = pyperf.Runner()
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

    #print(trios)
    for trio in trios:
        name = basename(trio[0])[:3]
        numbins: int = optimal_jbur[name]
        name += " multiway"
        data = JburkardtReader(trio[0], trio[1], trio[2]).multiway()
        for algo in on_algorithms: 
            binpacker = BinPackerFactory.build(algo)
            runner.bench_func(name + " " + algo, binpacker, data, numbins)

if __name__ == "__main__":
    main()
