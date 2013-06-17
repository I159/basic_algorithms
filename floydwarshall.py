#!/usr/bin/env python
"""
Inspirated by David Cain:
https://gist.github.com/DavidCain/4032399https://gist.github.com/DavidCain/4032399
"""
from copy import deepcopy

log_string = "paths[i][j]: {}\npats[i][k]: {}\npaths[k][j]: {}\n============="

def conv_to_adj_matrix(graph):
    """
    Convert directed weighted graph to a adjacency matrix.
    """
    vertices = graph.keys()
    mtrix = {}

    for i in vertices:
        mtrix[i] = {}
        for j in vertices:
            try:
                mtrix[i][j] = graph[i][j]
            except KeyError:
                if i == j:
                    mtrix[i][j] = 0
                else:
                    mtrix[i][j] = float('inf')
    return mtrix


def fw(matrix):
# Note, an incoming graph is already a matrix of adjacency!
    vertices = matrix.keys()
    paths = deepcopy(matrix)
    for k in vertices:
        for i in vertices:
            for j in vertices:
# Compare one edge path from `i` node to `j` node with path through a `k` node
                paths[i][j] = min(paths[i][j], paths[i][k] + paths[k][j])
                print """Current minimal path from `{}`
to `{}` through `{}`: {}""".format(i, j, k, paths[i][j])
    return paths


def test_fw():
    line_print = lambda k, v: "{}: {}".format(k, v)
    graph = {
            'a': {'b':3, 'c':8, 'e':-4},
            'b': {'d':1, 'e':7},
            'c': {'b': 4},
            'd': {'a':2, 'c':-5},
            'e': {'d':6}
            }
    matrix = conv_to_adj_matrix(graph)

    print "GRAPH:\n"
    for k, v in graph.items():
        print line_print(k, v)
    print "\n"*2
    print "MATRIX:\n"
    for k, v in matrix.items():
        print line_print(k, v)
    print '\n'*2
    print 'PATHS: \n'
    for k, v in fw(matrix).items():
        print line_print(k, v)
