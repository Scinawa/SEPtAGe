__author__ = 'user'

import pickle


class EdgeList:
    """
    Purpose of this class is extracting and converting all the possibile
    graph format (NetworkX, Numpy adjacecny matrix, csv, etc..) and give a
    edge_list which is a list that we need in order to run our algorithm.
    """

    def __init__(self, input, kind=None):
        self.__edge_list = []
        self.__num_edges = 0
        self.__num_nodes = 0
        if kind == 'numpy':
            self.read_graph_from_numpy(input)
        elif kind == 'csv':
            self.edge_list_from_csv(input)
        else:
            raise Exception("DISAGIOOO")

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

        # creiamo gli archi
        for i in range(0, len(file_content)):
            splitted_row = file_content[i].split(',')

            # removing f*ing  trailing character EOL
            splitted_row.append(splitted_row.pop().rstrip())

            print(splitted_row)

            for j in range(0, len(splitted_row)):
                if (ord(splitted_row[j]) == 48):
                    pass
                elif (ord(splitted_row[j]) == 49):
                    self.add_edge(i, j)
                else:
                    raise Exception("Unable to load csv file: strange char "
                                    "found")
        return

    def read_graph_from_numpy(self, file_path):
        """
        Read the pickle file and populate the attributes properly.
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
            fileContent = pickle.load(f)
            f.close()
        except Exception as e:
            raise Exception("Unable to read pickled numpy matrix")

        for i in range(0, len(fileContent)):
            self.add_vertex(i)
        # print "vertex added"


        # creiamo gli archi
        for i in range(0, len(fileContent)):
            # print "\nriga", i,
            rigasplittata = fileContent[i]
            # print "rigasplittata", rigasplittata
            for j in range(0, len(rigasplittata)):
                # print j
                if (rigasplittata[j] == 0):
                    pass
                else:
                    self.addEdge(i, j)
        return 0

    def addEdge(self, a, b):
        self.__edgeList.append((a, b))

    def __iter__(self):
        """
        We can iterate on such object, to increase the readability of the
        code, without getting the edge_list.
        :return:
        """
        return iter(self.__edgeList)
