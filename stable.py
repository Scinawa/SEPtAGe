__author__ = 'scinawa'

from graph import EdgeList
from partitionsets import ordered_set
from partitionsets import partition


def iterable_partitions(number=0):
    A_LIST = list(range(0, number))
    AN_OSET = ordered_set.OrderedSet(A_LIST)
    A_PARTITION = partition.Partition(AN_OSET)
    return A_PARTITION


def stable_partitions_from_networkx(G):
    """
    TODO: check if directed or undirected.
    :param G: a NetworkX graph.
    :return: an iterator over the list of stable partitions
    """
    import networkx as nx
    n = G.nodes()
    edge_list = G.edge_list()

    return


def stable_partition_from_numpy(matrix):
    """
    To be defined
    :param matrix:
    :return:
    """
    edge_list = EdgeList()
    return find_all_stable_partitions(EdgeList(matrix, kind=""))


def find_all_stable_partitions(A_PARTITION, edge_list):
    """
    Iterate over all yelds and give all the stable partition of the graph.
    :param grafo:
    :param A_PARTITION:
    :return:
    """

    stable_partitions = []
    for i in find_stable_partitions(A_PARTITION, edge_list):
        stable_partitions.append(i)
    return stable_partitions


def find_stable_partitions(edge_list, partitions):
    """
    Given an (iterable) list of partitions and the graph, find the next
    stable partition. This is the old version of the algorithm, that iterates
    through all the partitions and then through all the edges. The second
    versoin is splitted for readability, but I think this must be preferred
    for performances reasons.

    There are some "hacks" in order to improve the performance of the algorithm:
    (1) If the bucket of the partition is empty or it has only one element =>
    skip the bucket and go to the next one
    (2) If you find JUST one side of the edge in one bucket, it means that for
    that edge, the partition i stable and you can skip to check the next edge
    (3) If you are testing for an auto loop =>



    :param partitions: the iterable of partitions by partitionset package
    :param edge_list: the list of edges [(a,b), (c,b), ... ]
    :return: an iterable
    """

    unstable_number = 0
    for a_part in partitions:
        unstable = 0
        for edge in edge_list:
            print('edge1', i)
            jump = 0
            for bucket in [i for i in a_part if len(i) > 1]:  # (1)
                print("\t\til bucket", bucket)
                for node in bucket:
                    if (node == edge[0] or node == edge[1]):
                        if (edge[0] == edge[1]): # (3)
                                unstable_number += 1
                                unstable = 1
                                break  # good job!
                        else:
                            other2find = {edge[0], edge[1]} - {node}
                            missing_node = other2find.pop()
                            for other_nodes in bucket[bucket.index(node):]:
                                if missing_node == other_nodes:
                                    unstable_number += 1
                                    unstable = 1
                                    break  # good job!
                        jump = 1  # one extreme found, goto next edge (2)
                        break
                if jump or unstable: break
            if jump or unstable: break
        if not unstable:
            yield a_part

def is_stable(partition, edges):
    for i in edges:
        edge = grafo.edgeList[i]
        for bucket in [i for i in a_part if len(i) > 1]:  # skip bucket <= 1
            a = str(edge[0])
            b = str(edge[1])
            j = 0
            for chr in bucket:
                j = j + 1
                chr = str(chr)
                # se ho trovato un arco, devo solo cercare l'altro
                # perche'  sono sicuro che tutta la partizione sia stabile
                if (
                        chr == a or chr == b):  # print "trovato un carattere", a,b,chr
                    # print "\t\t\t\ttrovato in partizione", a_part, "bucket", bucket, "chr", chr, "a,", a, "b, ", b
                    other2find = set(set((a, b,)) - set((chr,)))
                    chr2 = int(other2find.pop())
                    skip1 = 1
                    for succ in range(j, len(bucket)):
                        # print "\t\t\t\tbucket[succ]",bucket[succ]
                        if (chr2 == bucket[
                            succ]):  # print "trovato il secondo"
                            unstableNumber = unstableNumber + 1
                            # print "\t\t\tnon stabile:", a_part,a,b,bucket,unstableNumber
                            skip2 = 1
                            break  # smette di cercare nei caratteri del bucket
                    break  # smette di cercare carattere nel bucket,
                    # tanto so che ha trovato un nodo, l'altro non e' dentro
                    #  e quindi sara' da un'altra parte, e quindi e' stabile (skip=0)
                else:
                    # print "nessuno dei due char in bucket", bucket, a,b
                    # pass # non ho trovato uno dei due caratteri, vado al succesivo
                    pass
                    # if (skip1): # se ho trovato un solo carattere, skippo i bucket e vado all'arco successivo.
                    #    break
        if (skip2):  # non serve controllare per ogni arco che questa
            # non sia stabile se non e gia stabile
            # print "break arco"
            break
        if (not skip2):
            # print "stabile: ", a_part
            stabili.append(a_part)
            yield a_part
            skip2 = 0
    return stabili
