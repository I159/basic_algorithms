#!/usr/bin/env python
"""
Inspirated by David Cain:
https://gist.github.com/DavidCain/4032399https://gist.github.com/DavidCain/4032399
"""

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
    paths = dict(matrix) # a gentle copy
    for k in vertices:
        for i in vertices:
            for j in vertices:
                print log_string.format(
                        paths[i][j],
                        paths[i][k],
                        paths[k][j])
                paths[i][j] = min(paths[i][j], paths[i][k] + paths[k][j])
    return paths



def test_fw():
    graph = {
            'a': {'b':3, 'c':8, 'e':-4},
            'b': {'d':1, 'e':7},
            'c': {'b': 4},
            'd': {'a':2, 'c':-5},
            'e': {'d':6}
            }
    matrix = conv_to_adj_matrix(graph)
    print 'Matrix: {}\n'.format(matrix)
    print 'Paths: {}\n'.format(fw(matrix))