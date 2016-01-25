## Synopsis

This software can calculate all the stable partition of a graph. A partition 
of the nodes is said to be stable if there are no edges connecting two different partition, i.e., the edges of the node of a partition are within the nodes of the partition itself. 
Since the software is just a wrapper around a single function, it can be 
easily used as a library compatible with NetworkX and numpy.

## Code Example

python3 main.py --csv graph.csv


> from stable import find_stable_partitions
> 

## Motivation

This software has been written for the exam of Combinatorics (Graph Theory), 
but has been edited, tested, refactored in the following months. To my 
knowledge, there are no other OS software that calculates stable partition of
 a graph. Stable partitions can be used (perhaps with some modifications) to 
 cluster nodes, or other jobs related to machine learning or graph theory. [1]

## Algorithm

The asymptotic of the algorithm is exponential in the number of nodes of the 
graph, and therefore the software cannot work for graph bigger than 20 nodes.
The algorithms simply iterate through all the possibile partition and check 
whether is stable or not (iterating a

## Possibile improvements

The software can be easily adapted to be multithread or even to be distributed.
It does make little sense indeed. 

## Installation

`git pull sdrena`

In order use this software as a library in your software, you simply need to 

from stable import stable_partition

or

from stable import stable_partitions

for both functions, the single parameter is a list of tuple, where each 
element of the list is an edge. 

Eg:

` [(1,2), (2,3), (3,4), (5,7)] `

Same as networkx specification for graphs.

## Testing and code coverage

I wrote some asserts. Specifically I wrote the code for a clique (complete 
graph of n elements), and other graphs.

The software was tested during the course of combinatorics, since the number 
of stable partition of some graphs is well known, and no bugs were found. 

Recently I am running tests for code coverage and tests on the quality of the dependency I use.

[![Requirements Status](https://requires.io/github/Scinawa/stablepartitions/requirements.svg?branch=master)](https://requires.io/github/Scinawa/stablepartitions/requirements/?branch=master)

[![Coverage Status](https://coveralls.io/repos/github/Scinawa/stablepartitions/badge.svg?branch=master)](https://coveralls.io/github/Scinawa/stablepartitions?branch=master)

[![Build Status](https://drone.io/github.com/Scinawa/stablepartitions/status.png)](https://drone.io/github.com/Scinawa/stablepartitions/latest)



## License

GNU General Public License v2.0




[1] http://wwwf.imperial.ac.uk/~mpbara/Partition_Stability/
