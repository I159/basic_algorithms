#!/usr/bin/env python
graph = {'a': ['b', 'c'],
        'b': ['c', 'd'],
        'c': ['d', 'e'],
        'd': ['c',],
        'e': ['f',],
        'f': ['d',]}


def find_path(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    if end in graph[start]:
        path += end
        return path
    for node in graph[start]:
        if node not in path:
            return find_path(graph, node, end, path)
    return None


def test_find_path():
    path = find_path(graph, 'a', 'd')
    assert path
    print path
