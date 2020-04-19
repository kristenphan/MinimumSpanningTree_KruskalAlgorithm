import sys
import math
from collections import namedtuple
from heapq import heappush, heappop
from disjoint_set import DisjointSet


Coordinates = namedtuple('Coordinates', ['x', 'y'])


def build_edges(n, x, y):
    '''
    Calculates the weights of all n vertices represented by coordinate x, y
    Input: n = number of vertices, a list of x coordinates (x) and y coordinates (y) with each pair (x,y) represents a vertex
    Output:
    (1) list of all vertices represented by its coordinates (v)
    (2) the weights of all edges in the form of a priority queue (pq_edges) for easy extraction of the edge of the minimum weight
    '''

    # create a list of vertices, each represented by their coordinates (x, y)
    v = []
    for i in range(n):
        vertex = Coordinates(x[i], y[i])
        v.append(vertex)
    assert n == len(v)

    # create a list of edges in the graph
    # each edge is represented by its two end vertices (v1, v2)
    # this list will include duplicate edges such as (v1, v2) and (v1, v2)
    # however, this will not interfere with calculating the minimum length of the minimum spanning tree (MST)
    lst_edges = []
    for v1 in v:
        for v2 in v:
            if v1 != v2:
                edge = (v1, v2)
                lst_edges.append(edge)

    # create a priority queue to store the vertices and their weights
    pq_edges = []

    # calculate the weight for each unique edge
    # and add the edge, represented by with its weight (w) and the two end vertices (v1, v2), to edges_pq
    for v1, v2 in lst_edges:
        w = math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)
        heappush(pq_edges, (w, v1, v2))

    return v, pq_edges


def minimum_distance(n, x, y):
    '''
    Implements the Kruskal's algorithm and builds a minimum spanning tree (MST) that spans all n vertices represented by coordinates x, y
    Calculates and returns the length of the MST
    Input: n = number of vertices, a list of x coordinates (x) and y coordinates (y) with each pair (x,y) represents a vertex
    Output: length of the MST
    '''

    result = 0
    v, heap = build_edges(n, x, y)
    ds = DisjointSet()
    while heap:
        min_edge = heappop(heap)
        w = min_edge[0]
        u = min_edge[1]
        v = min_edge[2]
        if not ds.connected(min_edge[1], min_edge[2]):
            ds.union(u, v)
            result += w

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance(n, x, y)))
