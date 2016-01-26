__author__ = 'scinawa'

import datetime
# import scipy
import sys
import itertools
# from __future__ import print_function
from partitionsets import ordered_set
from partitionsets import partition
import pickle
from graph import EdgeList
import argparse
from stable import *


def testing():
    import networkx as nx
    import numpy as np

    G = nx.complete_graph(5)
    assert find_stable_partitions(Graoh(G))

def menu():
    parser = argparse.ArgumentParser()

    # mutual exclusion on file type
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--csv", help="path of the csv file of the "
                                           "adjacecny matrix",
                       action='store', dest='csv_file')
    group.add_argument("-n", "--numpy", help='path of the numpy (pickled) '
                                             'graph in form of an adjacency '
                                             'matrix', action='store',
                       dest='numpy_file')

    parser.add_argument("-j", "--justone", help='return the first stable'
                                                'partition found, otherwise '
                                                'will keep searching',
                        action="store_true", dest='just_one')
    parser.add_argument('-o', '--output', help='the path of the output file',
                        dest='output_file')

    parsed_args = parser.parse_args()
    return parsed_args


if __name__ == '__main__':
    parser_args = menu()

    # reading the input form csv|pickle(numpy)
    g = EdgeList(parser_args.csv_file,  kind='csv') if parser_args.csv_file else \
        EdgeList(parser_args.numpy_file, kind='numpy')

    # Find the partition of a set of n elements
    partitions = iterable_partitions(g.node_number)

    # print if just one partition or all of them
    if parser_args.just_one:
        (used_time, stable_partitions) = find_stable_partitions(g, partitions)
        print('It took %s' % used_time) if (used_time > 0) else print("ok")
    else:
        (used_time, stable_partitions) = find_all_stable_partitions(g, partitions)
        print('It took %s' % used_time) if (used_time > 0) else print("ok")

    # Output results
    if parser_args.output_file:
        with open(parser_args.output_file, mode='w') as f_output:
            f_output.writelines(stable_partitions)
    else:
        from pprint import pprint
        pprint(stable_partitions)
    # Bye!
    sys.exit(0)