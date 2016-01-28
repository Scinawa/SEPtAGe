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


def testing_networkx():
    import networkx as nx

    G = nx.complete_graph(5)

    edge_list=EdgeList(G, kind='numpy')
    partitions = iterable_partitions(edge_list.node_number)

    assert find_stable_partitions(partitions, edge_list)

def testing_numpy():
    import numpy as np

    edge_list=EdgeList(matrix, kind='numpy')
    partitions = iterable_partitions(edge_list.node_number)

    assert find_stable_partition(partitions, edge_list) == 0




def testing_algorithm():
    pass





def menu():
    parser = argparse.ArgumentParser()

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

    if parser_args.csv_file:
        edge_list = EdgeList(parser_args.csv_file,  kind='csv')
    else:
        edge_list = EdgeList(parser_args.numpy_file, kind='numpy')

    partitions = iterable_partitions(edge_list.node_number)

    if parser_args.just_one:
        stable_partitions = find_stable_partition(partitions, edge_list )
        stable_partitions=[stable_partitions]
    else:
        (used_time, stable_partitions) = find_all_stable_partitions(
                                                        partitions, edge_list)
        print('It took %s' % used_time)

    # Output results
    if parser_args.output_file:
        with open(parser_args.output_file, mode='w') as f_output:
            for element in stable_partitions:
                print(element)
                f_output.writelines(str(element)+'\n')
    else:
        print ("Your stable partition:")
        for partition in stable_partitions:
            pass
            # print(partition)
    # Bye!
    sys.exit(0)