__author__ = 'scinawa'

from graph import EdgeList
from partitionsets import ordered_set
from partitionsets import partition
import datetime


def iterable_partitions(number=0):
    A_LIST = list(range(0, number))
    AN_OSET = ordered_set.OrderedSet(A_LIST)
    A_PARTITION = partition.Partition(AN_OSET)
    return A_PARTITION


################# Networkx ###################################


def stable_partitions_from_networkx(G):
    """
    TODO: check if directed or undirected.
    :param G: a NetworkX graph.
    :return: an iterator over the list of stable partitions
    """
    import networkx as nx
    partitions = iterable_partitions(len(G.nodes()))
    edge_list = EdgeList(G, kind='netwokrx')
    return find_stable_partitions(partitions, edge_list)


def all_stable_partitions_from_networkx(G):
    """
    TODO: check if directed or undirected.
    :param G: a NetworkX graph.
    :return: an iterator over the list of stable partitions
    """
    import networkx as nx
    n = G.nodes()
    edge_list = G.edge_list()

    return


################# NUMPY ###################################

def stable_partition_from_numpy(matrix):
    """
    It calculates the stable partition of a numpy adjacency matrix.

    :param matrix: numpy matrix
    :return:
    """
    edge_list = EdgeList(matrix, kind='numpy')
    partitions = iterable_partitions(edge_list.node_number)
    return find_stable_partitions(partitions, edge_list)


def all_stable_partition_from_numpy(matrix):
    """
    It calculates the stable partition of a numpy adjacency matrix.

    :param matrix: numpy matrix
    :return:
    """
    edge_list = EdgeList(matrix, kind='numpy')
    partitions = iterable_partitions(edge_list.node_number)
    return find_all_stable_partitions(partitions, edge_list)


################# GENERIC ###################################

def timeMeasure(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        d1 = datetime.datetime.now()
        result = function_to_decorate(*args, **kwargs)
        d2 = datetime.datetime.now()

        return (d2 - d1, result)

    return a_wrapper_accepting_arbitrary_arguments


@timeMeasure
def find_all_stable_partitions(partitions, edge_list, verbose):
    """
    Iterate over all yelds and give all the stable partition of the graph.
    :param partitions: an iterable of partition
    :param edge_list: the list of edges
    :return: a list of stable partitions
    """
    stable_partitions = []
    for i in find_stable_partition(partitions, edge_list, verbose):
        stable_partitions.append(i)
    return stable_partitions


def find_stable_partition(partitions, edge_list, verbose):
    """
    Find the next stable partition of the graph

    :param partitions: the iterable of partitions by partitionset package
    :param edge_list: the list of edges [(a,b), (c,b), ... ]
    :return: yield an iterable of stable partitions
    """
    for a_part in partitions:
        unstable = 0
        for edge in edge_list:
            if [i for (i, bucket) in enumerate(a_part) if edge[0] in bucket] \
                    == [i for (i, bucket) in enumerate(a_part) if edge[1] in
                            bucket]:
                if verbose: print(" Partition: ", a_part, ": Not stable!: ",
                                  edge)
                unstable = 1
                break  # go to next partition.
        if unstable == 0:
            if verbose: print(" Partition: ", a_part, ": Stable!")
            yield a_part
        else:
            continue
