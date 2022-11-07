from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.model import BinPacker, Online, Offline
from macpacking.factory import BinPackerFactory
from benchtools.optimal_vals import OptimalValues
from benchtools.case_reader import list_files, group_jburkardt_files

from os.path import basename
from json import dump

BINPP = './_datasets/binpp'
BINPP_HARD = './_datasets/binpp-hard'
JBURKARDT_CASES = './_datasets/jburkardt'

optimal_binpp = {}
optimal_binpp_hard = {}
optimal_jbur = {}

vals = {}


def main():

    global optimal_binpp, optimal_binpp_hard, optimal_jbur

    print("Creating file lists...")
    binpp = list_files(BINPP)
    binpp_hard = list_files(BINPP_HARD)
    jburkardt = group_jburkardt_files(list_files(JBURKARDT_CASES))
    print("done!\n")

    # print(binpp)
    # print(binpp_hard)
    # print(jburkardt)

    optimals = OptimalValues()
    optimal_binpp = optimals.binpp
    optimal_binpp_hard = optimals.binpp_hard
    optimal_jbur = optimals.jburkardt

    # print(optimal_binpp)
    # print(optimal_binpp_hard)
    # print(optimal_jbur)

    off_algorithms = ['NF_Off', 'FFDesc', 'BFDesc', 'WFDesc', 'BenMaier']
    on_algorithms = ['NF_On', 'FF', 'BF', 'WF', 'RFF']

    print("Evaluating binpp files...")
    for file in binpp:
        name = basename(file)
        reader: DatasetReader = BinppReader(file)
        optimal: int = optimal_binpp[name[:-8]]
        offline_optimal(name, reader, off_algorithms, optimal)
        online_optimal(name, reader, on_algorithms, optimal)

    print("Evaluating binpp_hard files...")
    for file in binpp_hard:
        name = basename(file)
        reader: DatasetReader = BinppReader(file)
        optimal: int = optimal_binpp_hard[name[:-8]]
        offline_optimal(name, reader, off_algorithms, optimal)
        online_optimal(name, reader, on_algorithms, optimal)

    print("Evaluating jburkardt files...\n")
    for files in jburkardt:
        name = basename(files[0])[:3]
        reader: DatasetReader = JburkardtReader(files[0], files[1])
        optimal: int = optimal_jbur[name]
        offline_optimal(name, reader, off_algorithms, optimal)
        online_optimal(name, reader, on_algorithms, optimal)

    print("Writing json file...\n")
    write_json()

    print("Bench complete")


def offline_optimal(filename: str, reader: DatasetReader, algorithms: list[BinPacker], optimal: int):

    for algo in algorithms:
        binpacker = BinPackerFactory.build(algo)
        strategy: Offline = binpacker
        result = strategy(reader.offline())
        vals[filename + ' ' + algo] = len(result) - optimal


def online_optimal(filename: str, reader: DatasetReader, algorithms: list[BinPacker], optimal: int):

    for algo in algorithms:
        binpacker = BinPackerFactory.build(algo)
        strategy: Online = binpacker
        result = strategy(reader.online())
        vals[filename + ' ' + algo] = len(result) - optimal


def write_json():

    with open("./outputs/optimal_vals.json", "w") as outfile:
        dump(vals, outfile)


if __name__ == "__main__":

    main()
