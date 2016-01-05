__author__ = 'scinawa'


import datetime
#import scipy
import sys
import itertools
# from __future__ import print_function
from partitionsets import ordered_set
from partitionsets import partition
import pickle
import graph
import argparse
from stable import find_stable_partitions


def testing():
    import networkx as nx
    import numpy as np

    G= nx.complete_graph(5)
    assert find_stable_partitions(Graoh(G))

def iterable_partitions(number=0):
    A_LIST = list(range(0,number))
    AN_OSET = ordered_set.OrderedSet(A_LIST)
    A_PARTITION = partition.Partition(AN_OSET)
    return A_PARTITION



def menu():
    parser = argparse.ArgumentParser()

    # mutual exclusion on file type
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--csv", help="path of the csv file of the "
                                           "adjacecny matrix",
                       action='store', dest='file_path')
    group.add_argument("-n", "--numpy", help='path of the numpy (pickled) '
                                             'graph in form of an adjacency '
                                             'matrix', action='store',
                       dest='file_path')

    parser.add_argument("-j","--justone", help='return the first stable'
                                               'partition found, otherwise '
                                               'will keep searching',
                        action="store_true")
    parser.add_argument('-o', '--output', help='the path of the output file',
                        dest='output_file')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    menu()


    print('Reading the graph from', filez)
    grafo=Graph.Graph()
    if (sys.argv[1] == '1'):
        grafo.AssumiGrafoPickled(filez)
    else:
        grafo.assumiGrafoNumpy(filez)

    partitions=iterable_partitions(g.nodeNumber)

    (usedtime, partizioni_stabili)=find_stable_partitions(grafo, partitions)
    print('It took %s' % usedtime) if (usedtime>0) else print("ok")

    #### Outputing results
    with open(args.output_file, mode='w') as f_output:
        f_output.writelines(partizioni_stabili)

