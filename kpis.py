from matplotlib import pyplot as plt


def wasted_space(capacity, bin_packing):

    empty_space = 0
    for bin in bin_packing:
        empty_space += capacity - sum(bin)

    return empty_space


def weight_distribution(bin_packing):

    bin_sums = [sum(bin) for bin in bin_packing]
    print(bin_sums)
    bin_indexes = [x for x in range(len(bin_packing))]

    plt.plot(bin_indexes, bin_sums)

    plt.xlabel('bin index')

    # naming the y axis
    plt.ylabel('weight of bins')

    # giving a title to my graph
    plt.title('Weight distribution')

    # function to show the plot
    plt.show()
