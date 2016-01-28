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

		d1=datetime.datetime.now()
		result=function_to_decorate(*args, **kwargs)
		d2=datetime.datetime.now()

		return (d2-d1, result)
	return a_wrapper_accepting_arbitrary_arguments

@timeMeasure
def find_all_stable_partitions(partitions, edge_list):
    """
    Iterate over all yelds and give all the stable partition of the graph.
    :param partitions: an iterable of partition
    :param edge_list: the list of edges
    :return: a list of stable partitions
    """
    stable_partitions = []
    for i in find_stable_partition(partitions, edge_list):
        stable_partitions.append(i)
    return stable_partitions


def find_stable_partition(partitions, edge_list):
    """
    Given an (iterable) list of partitions and the graph, find the next
    stable partition. This is the old version of the algorithm, that iterates
    through all the partitions and then through all the edges. The second
    version is split for readability, but I think this must be preferred
    for performances reasons.

    There are some "hacks" in order to improve the performance of the algorithm:
    (1) If you find JUST one side of the edge in one bucket, it means that for
    that edge, the partition i stable and you can skip to check the next edge

    :param partitions: the iterable of partitions by partitionset package
    :param edge_list: the list of edges [(a,b), (c,b), ... ]
    :return: yield an iterable of stable partitions
    """

    unstable_number = 0
    for a_part in partitions:
        print ("\nPartition: ", a_part, end='')
        unstable = 0
        for edge in edge_list:
            print(' Edge: ', edge, end='')
            jump = 0
            for bucket in a_part:
                print(" Bucket: ", a_part.index(bucket), end='')
                for node in bucket:
                    if node == edge[0] or node == edge[1]:
                        if node == edge[0] and node == edge[1]:  # autoloop
                                unstable_number += 1
                                unstable = 1
                                print (" Unstable (autoloop)")
                                break
                        else:
                            other2find = {edge[0], edge[1]} - {node}
                            missing_node = other2find.pop()
                            for other_nodes in bucket[bucket.index(node):]:
                                if missing_node == other_nodes:
                                    unstable_number += 1
                                    unstable = 1
                                    jump = 1
                                    print (" Unstable (connection)")
                                    break  # good job!
                    else:  # (1)
                        jump = 1
                if jump or unstable: break # (1)
        if not unstable:
            yield a_part

