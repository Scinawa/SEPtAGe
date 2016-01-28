# Synopsis

[![Requirements Status](https://requires.io/github/Scinawa/stablepartitions/requirements.svg?branch=master)](https://requires.io/github/Scinawa/stablepartitions/requirements/?branch=master)

[![Coverage Status](https://coveralls.io/repos/github/Scinawa/stablepartitions/badge.svg?branch=master)](https://coveralls.io/github/Scinawa/stablepartitions?branch=master)

[![Build Status](https://drone.io/github.com/Scinawa/stablepartitions/status.png)](https://drone.io/github.com/Scinawa/stablepartitions/latest)

[![Documentation Status](https://readthedocs.org/projects/stablepartitions/badge/?version=latest)](http://stablepartitions.readthedocs.org/en/latest/?badge=latest)



This software can calculate all the stable partition of a graph. A partition 
of the nodes is said to be stable if there are no edges connecting two  
different partition, i.e., the edges of the node of a  partition are within 
the nodes of the partition itself. More formally: Given a graph G=(V,E) and a
 partition of the nodes P=P_1, P_2, ... P_k, there are no edges (a,b) such as
  a is in P_i and b is in P_j.


# Motivation

This software has been written for the exam of Combinatorics (Graph Theory), 
but has been edited, tested, refactored in the following months. To my 
knowledge, there are no other OS software that calculates stable partition of
 a graph. Stable partitions can be used (perhaps with some modifications) to 
 cluster nodes, or other jobs related to machine learning or graph theory. [1]

# Algorithm

The number of partition is exponential in the number of nodes of the 
graph, and therefore the software cannot work for graph bigger than 20 nodes.
It is well known that this problem is NP-hard [2]. The algorithms simply 
iterate through all the possible partition and check whether is stable or not.

# Possible improvements

The software can be easily adapted to be multithread or even to be distributed.
It does make little sense, since the problem is exponential in the number of 
nodes. The only sensible tuning is to add "@memoization"

# Installation
Simply run:
`git clone https://github.com/Scinawa/SEPtAGe`
You can already run the software with:

      bash $ python3 main.py --help
      usage: main.py [-h] (-c CSV_FILE | -n NUMPY_FILE) [-j] [-v] [-o OUTPUT_FILE]
      
      optional arguments:
        -h, --help            show this help message and exit
        -c CSV_FILE, --csv CSV_FILE
                              path of the csv file of the adjacecny matrix
        -n NUMPY_FILE, --numpy NUMPY_FILE
                              path of the numpy (pickled) graph in form of an
                              adjacency matrix
        -j, --justone         return the first stable partition found, 
                              otherwise will
                              keep searching
        -v, --verbose         increase verbosity of operations
        -o OUTPUT_FILE, --output OUTPUT_FILE
                              the path of the output file
      


## As a library
 
In order use this software as a library in your software, you simply need to 

`python3 setup.py install`

and then, in your code:

`from stable import find_stable_partitions`

or

`from stable import find_all_stable_partitions`

### Networkx

`stable_partition_from_networkx(matrix)`

`all_stable_partition_from_networkx(matrix)`

### Numpy
These are the function for numpy:

`stable_partition_from_numpy(matrix)`

`all_stable_partition_from_numpy(matrix)`

# Testing and code coverage

I wrote some asserts. Specifically I wrote the code for a clique (complete 
graph of n elements), and other graphs.

The software was tested during the course of combinatorics, since the number 
of stable partition of some graphs is well known, and no bugs were found. 

Recently I am running tests for code coverage and tests on the quality of the dependency I use.


# License

GNU General Public License v2.0


# References

[1] http://wwwf.imperial.ac.uk/~mpbara/Partition_Stability/

[2] "Fast Balanced Partitioning is Hard, Even on Grids and Trees". 
Proceedings of the 37th International Symposium on Mathematical Foundations 
Computer Science (Bratislava, Slovakia).