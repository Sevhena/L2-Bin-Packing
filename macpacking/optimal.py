from os import listdir
from os.path import isfile, join, basename
import csv

binpp = './_datasets/binpp'
BINPP_HARD = './_datasets/binpp-hard'
JBURKARDT_CASES = './_datasets/jburkardt'

def main():
    binpp_hard = list_files(BINPP_HARD)

def get_binpp_csv():
    optimal_binpp = {}
    with open('_dataset\\binpp.csv') as file:
        csvfile = csv.reader(file)

        for lines in csvfile:
            optimal_binpp[lines[0]] = int(lines[1])

    return optimal_binpp

def get_binpp_hard_csv():
    optimal_binpp_hard = {}
    with open('_dataset\\binpp_hard.csv') as file:
        csvfile = csv.reader(file)

        for lines in csvfile:
            optimal_binpp_hard[lines[0]] = int(lines[1])

    return optimal_binpp_hard

def get_jburkardt_csv():
    optimal_jbur = {}
    with open('_dataset\jburkardt.csv') as file:
        csvfile = csv.reader(file)

        for lines in csvfile:
            optimal_jbur[lines[0]] = int(lines[1])

    return optimal_jbur

def list_files():
    return [f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")]

def list_files2():
    [f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f)) and not f.endswith("_source.txt")]
