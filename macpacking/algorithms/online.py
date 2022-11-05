from .. import Solution, WeightStream
from ..model import Online


class NextFit(Online):

    def __init__(self):
        self.count = 0

    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity

        for w in stream:
            self.count += 1
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution


class BadFit(Online):  # The most terrible bin packing algorithm from T1

    def __init__(self):
        self.count = 0

    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = [[w] for w in stream]
        return solution


class FirstFit(Online):

    def __init__(self):
        self.count = 0

    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bins = 0
        solution = [[]]
        remainders = [capacity]
        for w in stream:
            i = 0
            while i < bins:
                self.count += 1
                if remainders[i] >= w:
                    solution[i].append(w)
                    remainders[i] -= w
                    break
                i += 1
            else:
                bins += 1
                solution.append([w])
                remainders.append(capacity-w)
        return solution


class RefinedFirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        Apiece = []
        B1piece = []
        B2piece = []
        Xpiece = []

        Class1 = [[]]
        Class2 = [[]]
        Class3 = [[]]
        Class4 = [[]]

        m = [6, 7, 8, 9]
        counter = 0

        pieceMapping = {'Class1': Apiece, 'Class2': B1piece, 'Class3': B2piece, 'Class4': Xpiece}
        classMapping = {'Class1': Class1, 'Class2': Class2, 'Class3': Class3, 'Class4': Class4}

        for w in stream:
            counter += 1
            if (w / capacity) > 1/2 and (w / capacity) <= 1:
                Apiece.append(w)
            elif (w / capacity) > 2/5 and (w / capacity) <= 1/2:
                B1piece.append(w)
            elif (w / capacity) > 1/3 and (w / capacity) <= 2/5:
                if counter % m[0] == 0 or counter % m[1] == 0 or counter % m[2] == 0 or counter % m[3] == 0:
                    Apiece.append(w)
                else:
                    B2piece.append(w)
            else:
                Xpiece.append(w)

        for Class in classMapping:
            bin_index = 0
            remainders = [capacity]
            for w in pieceMapping[Class]:
                found_fit = False
                for i in range(bin_index):
                    if remainders[i] >= w:
                        classMapping[Class][i].append(w)
                        remainders[i] -= w
                        found_fit = True
                        break
                if not found_fit:
                    bin_index += 1
                    classMapping[Class].append([w])
                    remainders.append(capacity - w)

        solution = classMapping['Class1'] + classMapping['Class2'] + classMapping['Class3'] + classMapping['Class4']
        return [x for x in solution if x]


class BestFit(Online):

    def __init__(self):
        self.count = 0

    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remainders = [capacity]
        for w in stream:
            if solution[bin_index] == [] or len(solution) == 1:
                self.count += 1
                if remainders[bin_index] >= w:
                    solution[bin_index].append(w)
                    remainders[bin_index] -= w
                else:
                    bin_index += 1
                    solution.append([w])
                    remainders.append(capacity - w)
                continue
            max_load = [-1, capacity + 1]
            for i in range(bin_index):
                self.count += 1
                if remainders[i] >= w:
                    if remainders[i] < max_load[1]:
                        max_load[0] = i
                        max_load[1] = remainders[i]
            if max_load[0] >= 0:
                solution[max_load[0]].append(w)
                remainders[max_load[0]] -= w
            else:
                solution.append([w])
                bin_index += 1
                remainders.append(capacity-w)
        return solution


class WorstFit(Online):

    def __init__(self):
        self.count = 0

    def counting_compares(self):
        return self.count

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remainders = [capacity]
        for w in stream:
            if solution[bin_index] == [] or len(solution) == 1:
                self.count += 1
                if remainders[bin_index] >= w:
                    solution[bin_index].append(w)
                    remainders[bin_index] -= w
                else:
                    bin_index += 1
                    solution.append([w])
                    remainders.append(capacity - w)
                continue
            min_load = [-1, -1]
            for i in range(bin_index):
                self.count += 1
                if remainders[i] >= w:
                    if remainders[i] > min_load[1]:
                        min_load[0] = i
                        min_load[1] = remainders[i]
            if min_load[0] >= 0:
                solution[min_load[0]].append(w)
                remainders[min_load[0]] -= w
            else:
                solution.append([w])
                bin_index += 1
                remainders.append(capacity-w)
        return solution
