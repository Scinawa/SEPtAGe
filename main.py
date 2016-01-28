__author__ = 'scinawa'

import sys
from graph import EdgeList
import argparse
from stable import *
import pprint


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


def testing_code_coverage():
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
    parser.add_argument("-v", '--verbose', help='increase verbosity of '
                                                'operations',
                        action='store_true', dest='verbose')
    parser.add_argument('-o', '--output', help='the path of the output file',
                        dest='output_file')

    parsed_args = parser.parse_args()
    return parsed_args


if __name__ == '__main__':
    parser_args = menu()

    if parser_args.csv_file:
        edge_list = EdgeList(parser_args.csv_file,  kind='csv')
        print("Input: ", parser_args.csv_file, ": ", edge_list.node_number,
              "nodes")
        if parser_args.verbose: print(edge_list.edge_list)
    else:
        edge_list = EdgeList(parser_args.numpy_file, kind='numpy')
        print("Input: ", parser_args.csv_file, ": ", edge_list.node_number,
              "nodes")
        if parser_args.verbose: print(edge_list.edge_list)

    partitions = iterable_partitions(edge_list.node_number)

    if parser_args.just_one:
        stable_partitions = find_stable_partition(partitions, edge_list,
                                                  parser_args.verbose)
        stable_partitions=[stable_partitions]
    else:
        (used_time, stable_partitions) = find_all_stable_partitions(
            partitions, edge_list, parser_args.verbose)
        print('It took:  %s' % used_time)

    # Output results
    if parser_args.output_file:
        with open(parser_args.output_file, mode='w') as f_output:
            for element in stable_partitions:
                f_output.writelines(str(element)+'\n')
    else:
        for partition in stable_partitions:
            pprint.pprint(partition)
    print("Stable: ", len(stable_partitions))
    sys.exit(0)