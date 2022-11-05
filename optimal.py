from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.model import BinPacker, Online, Offline
from macpacking.factory import BinPackerFactory
from optimal_vals import read_binpp_csv, read_binpp_hard_csv, read_jburkardt_csv

from os import listdir, walk
from os.path import isfile, join, basename
from json import dump

BINPP = './_datasets/binpp'
BINPP_HARD = './_datasets/binpp-hard'
JBURKARDT_CASES = './_datasets/jburkardt'

optimal_binpp = {}
optimal_binpp_hard = {}
optimal_jbur = {}

# NF_off_vals = []; NF_on_vals = []
# FF_off_vals = []; FF_on_vals = []
# BF_off_vals = []; BF_on_vals = []
# WF_off_vals = []; WF_on_vals = []
# BenMaier_vals = []

vals = {}


def main():

    global optimal_binpp, optimal_binpp_hard, optimal_jbur

    print("Creating file lists...")
    binpp = list_binpp_files(BINPP)
    binpp_hard = list_binpp_hard_files(BINPP_HARD)
    jburkardt = list_jbur_files(JBURKARDT_CASES)
    print("done!\n")

    # print(binpp)
    # print(binpp_hard)
    # print(jburkardt)

    optimal_binpp = read_binpp_csv()
    optimal_binpp_hard = read_binpp_hard_csv()
    optimal_jbur = read_jburkardt_csv()

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
        reader: DatasetReader = JburkardtReader(files[0], files[1], files[2])
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
        # append_to_list(algo, len(result) - optimal)
        vals[filename + ' ' + algo] = len(result) - optimal


def online_optimal(filename: str, reader: DatasetReader, algorithms: list[BinPacker], optimal: int):
    for algo in algorithms:
        binpacker = BinPackerFactory.build(algo)
        strategy: Online = binpacker
        result = strategy(reader.online())
        # append_to_list(algo, len(result) - optimal)
        vals[filename + ' ' + algo] = len(result) - optimal


def write_json():

    with open("./outputs/optimal_vals.json", "w") as outfile:
        dump(vals, outfile)


def list_binpp_hard_files(dir: str) -> list[str]:

    return [f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")]


def list_jbur_files(dir: str) -> list[str]:

    files = [f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")]
    trios = []
    index, counter = -1, 3
    for case in files:
        if counter == 3:
            counter = 1
            index += 1
            trios.append([case])
        else:
            trios[index].append(case)
            counter += 1

    return trios


def list_binpp_files(root: str) -> list[str]:

    return [join(path, name) for path, subdirs, files in walk(root) for name in files if not name == "_source.txt"]


if __name__ == "__main__":

    main()
