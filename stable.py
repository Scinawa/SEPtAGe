__author__ = 'scinawa'



def stable_partitions_from_networkx(G):
    """
    To be defined
    :param G:
    :return:
    """
    pass




def stable_partition_from_numpy(matrix):
    """
    To be defined
    :param matrix:
    :return:
    """
    pass




def find_all_stable_partitions(A_PARTITION, edge_list):
    """
    Iterate over all yelds and give all the stable partition of the graph.
    :param grafo:
    :param A_PARTITION:
    :return:
    """

    stable_partitions=[]
    for i in find_stable_partitions(A_PARTITION, edge_list):
        stable_partitions.append(i)
    return stable_partitions


def find_stable_partitions1(A_PARTITION, edge_list):
    """
    Given an (iterable) list of partitions and the graph, find the next
    stable partition. This is the old version of the algorithm, that iterates
    through all the partitions and then through all the edges. The second
    versoin is splitted for readability, but I think this must be preferred
    for performances reasons.

    :param A_PARTITION: the iterable of partitions by partitionset package
    :param edge_list: the list of edges [(a,b), (c,b), ... ]
    :return: an iterable
    """
    edges=edge_list
    unstableNumber = 0
    for a_part in A_PARTITION:
        skip1 = 0
        skip2 = 0
        for i in edges:
            edge = grafo.edgeList[i]
            for bucket in [i for i in a_part if len(i) > 1]: #skip bucket <= 1
                # print "\t\til bucket", bucket
                a = str(edge[0])
                b = str(edge[1])
                j = 0
                for chr in bucket:
                    j = j + 1
                    chr = str(chr)
                    # se ho trovato un arco, devo solo cercare l'altro
                    # perche'  sono sicuro che tutta la partizione sia stabile
                    if (chr == a or chr == b):  # print "trovato un carattere", a,b,chr
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



def is_stable(partition, edges):
    for i in edges:
        edge = grafo.edgeList[i]
        for bucket in [i for i in a_part if len(i) > 1]: #skip bucket <= 1
            a = str(edge[0])
            b = str(edge[1])
            j = 0
            for chr in bucket:
                j = j + 1
                chr = str(chr)
                # se ho trovato un arco, devo solo cercare l'altro
                # perche'  sono sicuro che tutta la partizione sia stabile
                if (chr == a or chr == b):  # print "trovato un carattere", a,b,chr
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