import matplotlib.pyplot as plt
import numpy as np
import itertools


def ld_plot(ld, labels: list[str]):
    """
    ld_plot(ld, labels: list[str])

    Plot of a Linkage Disequilibrium (LD) matrix

    :param ld: A symmetric LD matrix
    :param labels: A list of position names
    """
    n = ld.shape[0]

    figure = plt.figure()

    # mask triangle matrix
    mask = np.tri(n, k=0)
    ld_masked = np.ma.array(ld, mask=mask)

    # create rotation/scaling matrix
    t = np.array([[1, 0.5], [-1, 0.5]])
    # create coordinate matrix and transform it
    coordinate_matrix = np.dot(np.array([(i[1], i[0])
                                         for i in itertools.product(range(n, -1, -1), range(0, n + 1, 1))]), t)

    # plot
    ax = figure.add_subplot(1, 1, 1)
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.tick_params(axis='x', which='both', top=False)
    plt.pcolormesh(coordinate_matrix[:, 1].reshape(n + 1, n + 1),
                   coordinate_matrix[:, 0].reshape(n + 1, n + 1), np.flipud(ld_masked))
    plt.xticks(ticks=np.arange(len(labels)) + 0.5, labels=labels, rotation='vertical', fontsize=3)
    plt.colorbar()
    return figure
