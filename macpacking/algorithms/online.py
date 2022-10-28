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

class BadNextFit(Online): #The most terrible bin packing algorithm from T1

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
        bin_index = 0
        solution = [[]]
        remainders = [capacity]
        for w in stream:
            found_fit = False
            for i in range(bin_index):
                self.count += 1
                if remainders[i] >= w:
                    solution[i].append(w)
                    remainders[i] -= w
                    found_fit = True
                    break
            if not found_fit:
                bin_index += 1
                solution.append([w])
                remainders.append(capacity-w)
        return solution

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
                        max_load[0] = i; max_load[1] = remainders[i]
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
                        min_load[0] = i; min_load[1] = remainders[i]
            if min_load[0] >= 0:
                solution[min_load[0]].append(w)
                remainders[min_load[0]] -= w
            else:
                solution.append([w])
                bin_index += 1
                remainders.append(capacity-w)
        return solution



strategy: Online = NextFit()
count: int = NextFit().counting_compares()

print(count)