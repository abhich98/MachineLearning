import matplotlib.pyplot as plt
from matplotlib import gridspec


def plot_neurons_in_light(neuron_array, light_array):
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharex=ax1)

    ax1.plot(light_array)
    for n in neuron_array:
        ax2.plot(n)

    ax2.set_xlabel("Time")
    ax1.set_ylabel("Light level")
    ax2.set_ylabel("Norm. neuron activity")

    fig.suptitle("Testing")
    plt.show()


def plot_light_level(light_array, light_level_bins):
    fig = plt.figure()
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharey=ax1)

    ax1.plot(light_array)
    ax2.hist(light_array, bins=light_level_bins, orientation='horizontal')
    plt.show()