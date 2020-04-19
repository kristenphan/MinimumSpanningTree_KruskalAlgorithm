#Uses python3
import sys
import math
from collections import namedtuple
from heapq import heappush, heappop


class Node:
    '''
    A node class which stores the value, rank and parent, for use in DisjointSet class (make_set function).
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, val, rnk):
        self.val = val
        self.rank = rnk
        self.parent = self


class DisjointSet:
    '''
    A disjoint set data structure, for implementing union find operations.
    '''

    def __init__(self):
        # The 'members' dictionary maps the value (val) to the corresponding node (Node class)
        self.members = dict()

    '''
    Input: Value to be retrieved from sets.
    Output: Node corresponding to the value if it is present, None otherwise.
    '''
    def get(self, val):
        if val in self.members:
            return self.members[val]
        else:
            return None

    def make_set(self, val):
        if val not in self.members:
            # The rank is initially 0 since it is a new set
            self.members[val] = Node(val, 0)

    '''
    Takes input of a given node in the members dictionary.
    Returns the root of its set.
    '''
    def find(self, n):
        '''
        Uses path compression heuristics to keep the tree representing the disjoint set low
        '''
        if n.parent != n:
            self.members[n.val].parent = self.find(n.parent)
        return n.parent

    def union(self, n1, n2):
        '''
        Uses union by rank heuristics to keep the tree representing the disjoint set low
        '''
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)

        if root_n1 == root_n2:
            return True
        else:
            if root_n1.rank > root_n2.rank:
                self.members[root_n2.val].parent = self.members[root_n1.val]
            elif root_n1.rank < root_n2.rank:
                self.members[root_n1.val].parent = self.members[root_n2.val]
            else:
                self.members[root_n2.val].parent = self.members[root_n1.val]
                self.members[root_n1.val].rank = root_n1.rank+1


# this named tuple represents a vertex by its coordinate (x, y)
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


def minimum_length(n, x, y):
    '''
    Implements the Kruskal's algorithm and builds a minimum spanning tree (MST) that spans all n vertices represented by coordinates x, y
    Calculates and returns the length of the MST
    Input: n = number of vertices, a list of x coordinates (x) and y coordinates (y) with each pair (x,y) represents a vertex
    Output: length of the MST
    '''

    min_len = 0
    v, pq_edges = build_edges(n, x, y)
    ds = DisjointSet()
    for vertex in v:
        ds.make_set(vertex)

    while pq_edges:
        min_edge = heappop(pq_edges)
        w = min_edge[0]
        v1 = min_edge[1]
        v2 = min_edge[2]
        if ds.find(ds.get(v1)) != ds.find(ds.get(v2)):
            ds.union(ds.get(v1), ds.get(v2))
            min_len += w

    return min_len


# this program reads the input that represents n vertices and returns the length of the MST connecting all n vertices
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_length(n, x, y)))
