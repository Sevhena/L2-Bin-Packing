import macpacking.algorithms.online as online
import macpacking.algorithms.offline as offline
from macpacking.model import Online, Offline

# Online
# -------------------------------------------
# -------------------------------------------

empty = (50, iter([]))
at_c = (10, iter([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
regular = (20, iter([10, 8, 15, 4, 20, 18, 9, 2, 19, 1, 5, 2]))

# Bad Fit
# -------------------------------------------

def test_BadFit_empty_list():

    strategy: Online = online.BadFit()
    result = strategy(empty)

    assert len(result) == 0
    assert result == []


def test_BadFit_regular():

    strategy: Online = online.BadFit()
    result = strategy(regular)

    assert len(result) == 12
    assert result == [[10], [8], [15], [4], [20], [18], [9], [2], [19], [1], [5], [2]]

# Next Fit
# -------------------------------------------

def test_nextFit_empty_list():

    strategy: Online = online.NextFit()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_nextFit_at_capacity():

    strategy: Online = online.NextFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_nextFit_regular():

    strategy: Online = online.NextFit()
    result = strategy(regular)

    assert len(result) == 7
    assert result == [[10, 8], [15, 4], [20], [18], [9, 2], [19,  1], [5, 2]]

# First Fit
# -------------------------------------------


def test_FirstFit_empty_list():

    strategy: Online = online.FirstFit()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_FirstFit_at_capacity():

    strategy: Online = online.FirstFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_FirstFit_regular():

    strategy: Online = online.FirstFit()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[10, 8, 2], [15, 4,  1], [20], [18, 2], [9, 5], [19]]


# Refined First Fit
# -------------------------------------------


def test_RFF_empty_list():

    strategy: Online = online.RefinedFirstFit()
    result = strategy(empty)

    assert len(result) == 0
    assert result == []


def test_RFF_at_capacity():

    strategy: Online = online.RefinedFirstFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_RFF_regular():

    strategy: Online = online.RefinedFirstFit()
    result = strategy(regular)

    assert len(result) == 7
    assert result == [[10, 8, 2], [15, 4,  1], [20], [18, 2], [9, 5], [19]]


# Best Fit
# -------------------------------------------

def test_BestFit_empty_list():

    strategy: Online = online.BestFit()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_BestFit_at_capacity():

    strategy: Online = online.BestFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_BestFit_regular():

    strategy: Online = online.BestFit()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[10, 8, 2], [15, 4,  1], [20], [18, 2], [9, 5], [19]]


# Worst Fit
# -------------------------------------------

def test_WorstFit_empty_list():

    strategy: Online = online.WorstFit()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_WorstFit_at_capacity():

    strategy: Online = online.WorstFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_WorstFit_regular():

    strategy: Online = online.WorstFit()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[10, 8], [15, 4], [20], [18], [9, 2,  1, 5, 2], [19]]


# Offline
# -------------------------------------------
# -------------------------------------------

empty = (50, [])
at_c = (10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
regular = (20,  [10, 8, 15, 4, 20, 18, 9, 2, 19,  1, 5, 2])

# Next Fit
# -------------------------------------------


def test_NextFit_off_empty_list():

    strategy: Offline = offline.NextFit()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_NextFit_off_at_capacity():

    strategy: Offline = offline.NextFit()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_NextFit_off_regular():

    strategy: Offline = offline.NextFit()
    result = strategy(regular)

    assert len(result) == 7
    assert result == [[20], [19], [18], [15], [10, 9], [8, 5, 4, 2], [2,  1]]


# First Fit
# -------------------------------------------

def test_FirstFit_off_empty_list():

    strategy: Offline = offline.FirstFitDecreasing()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_FirstFit_off_at_capacity():

    strategy: Offline = offline.FirstFitDecreasing()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_FirstFit_off_regular():

    strategy: Offline = offline.FirstFitDecreasing()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[20], [19,  1], [18, 2], [15, 5], [10, 9], [8, 4, 2]]


# Best Fit
# -------------------------------------------

def test_BestFit_off_empty_list():

    strategy: Offline = offline.BestFitDecreasing()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_BestFit_off_at_capacity():

    strategy: Offline = offline.BestFitDecreasing()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_BestFit_off_regular():

    strategy: Offline = offline.BestFitDecreasing()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[20], [19,  1], [18, 2], [15, 5], [10, 9], [8, 4, 2]]


# Worst Fit
# -------------------------------------------

def test_WorstFit_off_empty_list():

    strategy: Offline = offline.WorstFitDecreasing()
    result = strategy(empty)

    assert len(result) == 1
    assert result == [[]]


def test_WorstFit_off_at_capacity():

    strategy: Offline = offline.WorstFitDecreasing()
    result = strategy(at_c)

    assert len(result) == 1
    assert result == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_WorstFit_off_regular():

    strategy: Offline = offline.WorstFitDecreasing()
    result = strategy(regular)

    assert len(result) == 6
    assert result == [[20], [19], [18], [15, 2, 2], [10, 9], [8, 5, 4,  1]]
