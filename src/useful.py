"""This modules just contains global definitions and functions
"""


import numpy as np
import matplotlib.pyplot as plt


BASES_DIR = '../bases/'
CORPORA_DIR = '%scorpora/' % BASES_DIR
FEATURES_DIR = '%sfeatures/' % BASES_DIR
IMAGES_DIR = '../docs/paper/images/'


def plot(x, y, suptitle='', xlabel='', ylabel='', color='blue', fill=False):
    fig = plt.gcf()
    fig.suptitle(suptitle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if fill:
        plt.fill_between(x, y, color=color)
    plt.plot(x, y, color=color)

def plotfile(x, y, suptitle='', xlabel='', ylabel='', filename=None, filecounter=0,
             color='blue', fill=False):
    """Creates a Matplotlib figure and plots the @param y related to @param x.

    @param x: a numpy array.
    @param y: a numpy array of the same size of @param x.
    @param suptitle: the title of the figure.
    @param xlabel: the label of the x axis.
    @param ylabel: the label of the y axis.
    @param filename: name of file to plot.
    @param filecounter: composes the final filename.
    @param color: the color of line (and area filled).
    @param fill: to fill the area beneath the curve.
    """
    plt.clf()
    plot(x, y, suptitle, xlabel, ylabel, color, fill)

    if not filename is None:
        plt.savefig('%s%03d.png' % (filename, filecounter))
        return (filecounter + 1)

    return filecounter

def testmultiplot(x, y, suptitle='', xlabel='', ylabel='', filename=None, filecounter=0,
             color='blue', fill=False):
    """Creates a Matplotlib figure and plots the @param y related to @param x.

    @param x: a numpy array.
    @param y: a numpy array of the same size of @param x.
    @param suptitle: the title of the figure.
    @param xlabel: the label of the x axis.
    @param ylabel: the label of the y axis.
    @param ylim: the limits of the y axis.
    """
    plt.clf()
    fig = plt.gcf()
    fig.suptitle(suptitle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    for i in range(len(y)):
        plt.plot(x, y[i], color=color)

    if not filename is None:
        plt.savefig('%s%03d.png' % (filename, filecounter))