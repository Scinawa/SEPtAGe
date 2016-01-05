__author__ = 'user'




class Graphs:
    """
    Purpose of this class is extracting and converting all the possibile
    graph format (NetworkX, Numpy adjacecny matrix, csv, etc..) and give a
    edge_list which is a list that we need in order to run our algorithm.
    """
    def __init__(self):
        self.__vertList = {}
        self.__edgeList = {}
        self.__numVertices = 0
        self.__numEdges = 0

    def read_graph_from_csv(self, file_path):
        """
        Read the csv file and populate the attributes properly.

        :param file_path: the path of the csv file
        :return: None
        """
        f = open(file_path, "r")
        file_content = f.readlines()
        f.close()


        # I nodi vengono creati automaticamente alla creazione dell'arco
        # ma ho speso 10 minuti a capire che un nodo senza archi puo far parte del grafo,
        # e quindi sono importanti anche le righe di soli 0 per specificare un grafo
        # senza le linee seguenti questi nodi non vengono creati
        for i in range(0, len(file_content)):
            self.add_vertex(i)

        # creiamo gli archi
        for i in range(0, len(file_content)):
            rigasplittata = file_content[i].split(',')
            # print rigasplittata
            rigasplittata.append(rigasplittata.pop().rstrip())
            # print rigasplittata,"!"
            for j in range(0, len(rigasplittata)):
                # print ord(rigasplittata[j])
                if (ord(rigasplittata[j]) == 48):
                    pass
                elif (ord(rigasplittata[j]) == 49):
                    self.addEdge(i, j)  # aggiungo arco a liste di incidenza
                    self.addEdge2(i, j)  # aggiungo arco a matrici di adiacenza
                    # print "arco aggiunto", i, j
        return 0

    def read_graph_from_numpy_pickled(self, file_path):
        f = open(file_path, "r")
        fileContent = pickle.load(f)
        # pprint(fileContent)
        f.close()


        # I nodi vengono creati automaticamente alla creazione dell'arco
        # ma ho speso 10 minuti a capire che un nodo senza archi puo far parte del grafo,
        # e quindi sono importanti anche le righe di soli 0 per specificare un grafo
        # senza le linee seguenti questi nodi non vengono creati
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
                    self.addEdge2(i, j)
        return 0

    def add_vertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex.Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not in self.vertList:
            nv = self.add_vertex(t)
        # print "adding edge", f,t
        self.vertList[f].addNeighbor(self.vertList[t])

    def addEdge2(self, f, t, cost=0):
        # print "aE2", f,t
        self.edgeList[self.numEdges + 1] = (f, t)
        self.numEdges = self.numEdges + 1

    def getEdges(self):
        return self.edgeList

    def __iter__(self):
        return iter(self.vertList.values())
