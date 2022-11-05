import csv

def read_binpp_csv():
    optimal_binpp = {}
    with open('./_datasets/binpp.csv') as file:
        csvfile = csv.reader(file)

        next(csvfile)

        for lines in csvfile:
            optimal_binpp[lines[0]] = int(lines[1])
    return optimal_binpp

def read_binpp_hard_csv():
    optimal_binpp_hard = {}
    with open('./_datasets/binpp_hard.csv') as file:
        csvfile = csv.reader(file)

        next(csvfile)

        for lines in csvfile:
            optimal_binpp_hard[lines[0]] = int(lines[1])

    return optimal_binpp_hard

def read_jburkardt_csv():
    optimal_jbur = {}
    with open('./_datasets/jburkardt.csv') as file:
        csvfile = csv.reader(file)

        next(csvfile)

        for lines in csvfile:
            optimal_jbur[lines[0]] = int(lines[1])

    return optimal_jbur