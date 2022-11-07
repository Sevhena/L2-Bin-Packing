from os import walk
from os.path import join, isfile, basename


def list_files(root: str) -> list[str]:

    return sorted([join(path, name)
                  for path, subdirs, files in walk(root)
                  for name in files if isfile(join(path, name))
                  and not name == "_source.txt"])


def group_jburkardt_files(files: list[str]) -> list[list[str]]:
    cases = []
    index, counter = -1, 3
    for case in files:
        if counter == 3:
            counter = 1
            index += 1
            cases.append([case])
        else:
            if basename(case)[4:5] != 's':
                cases[index].append(case)
            counter += 1

    return cases
