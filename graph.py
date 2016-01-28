__author__ = 'user'


class EdgeList:
    """
    Purpose of this class is extracting and converting all the possibile
    graph format (NetworkX, Numpy adjacecny matrix, csv, etc..) and give a
    edge_list which is a list that we need in order to run our algorithm.
    """

    def __init__(self, graph, kind=None):
        self.__edge_list = []
        self.__num_edges = 0
        self.__num_nodes = 0
        if kind == 'numpy':
            self.edge_list_from_numpy(graph)
        elif kind == 'csv':
            self.edge_list_from_csv(graph)
        elif kind == 'networkx':
            self.edge_list_from_networkx(graph)
        else:
            raise Exception("Format not recognized")

    @property
    def node_number(self):
        return self.__num_nodes

    @property
    def edge_list(self):
        """
        For Christ sake, use getter and setter (cit. Java boy)
        :return: edge_list
        """
        return self.__edge_list

    def edge_list_from_csv(self, file_path):
        """
        Read the csv file and populate the attributes properly.
        The file should be an adjacecny matrix of the graph, that is,
        a NxN matrix of 0 and 1 comma separated, where 0 means no edge,
        and 1 in row i, column j means that there is a directed arc from i to j
        Example:

        0,0,0,0
        0,1,0,0
        1,0,0,1
        1,1,1,1

        :param file_path: the path of the csv file
        :return: None
        """
        try:
            f = open(file_path, "r")
            file_content = f.readlines()
            f.close()
        except Exception as e:
            print('I cannot open the csv file, %', e)
            raise Exception

        self.__num_nodes = len(file_content)  #

        # create arcs
        for (i, line) in enumerate(file_content):
            splitted_row = line.split(',')

            # removing trailing char from line
            splitted_row[-1] = splitted_row[-1].rstrip()

            for (j, col) in enumerate(splitted_row):
                if col == '0':
                    pass
                elif col == '1':
                    self.__edge_list.append((i, j))
                elif col == '':
                    pass # ship happends
                else:
                    raise Exception("Unable to load csv file: strange char ",
                                    "found: %d" % col)

    def edge_list_from_networkx(self, graph):
        self.__edge_list = graph.edges()


    def edge_list_from_numpy(self, matrix):
        """
        Convert to edge list

        :param matrix:
        :return:
        """
        import numpy as np

        for (x,y), value in np.ndenumerate(matrix):
            if value == 1:
                self.__edge_list.append((x, y))



    def __iter__(self):
        """
        We can iterate on such object, to increase the readability of the
        code, without getting the edge_list.
        :return:
        """
        return iter(self.__edge_list)
