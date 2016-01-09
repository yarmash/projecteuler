#!/usr/bin/python

"""Problem 107: Minimal network"""

from heapq import heappush, heappop
from itertools import repeat
from utils import open_data_file


class Edge:
    """Lightweight edge structure for a graph"""
    __slots__ = ("origin", "dest", "weight")

    def __init__(self, origin, dest, weight):
        self.origin = origin
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return "{{{}, {}}} → {}".format(self.origin, self.dest, self.weight)

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge"""
        return self.dest if v == self.origin else self.origin


class Graph:
    """Representation of a simple undirected graph using an adjacency list"""

    def __init__(self, vertices):
        """Create an empty graph"""

        self.vertices = [[] for _ in repeat(None, vertices)]

    def insert_edge(self, u, v, w):
        """Insert and return a new Edge from u to v with weight w"""

        e = Edge(u, v, w)
        self.vertices[u].append(e)
        self.vertices[v].append(e)

    def incident_edges(self, v):
        """Return all edges incident to vertex v in the graph"""

        for edge in self.vertices[v]:
            yield edge


def main():
    size = 40
    total = spanning = 0

    graph = Graph(size)

    with open_data_file("network.txt") as data_file:
        for u, line in enumerate(data_file):
            for v, w in enumerate(line.rstrip().split(",")):
                if v > u and w != "-":
                    w = int(w)
                    total += w
                    graph.insert_edge(u, v, w)

    # Implement the Prim–Jarník algorithm
    D = [float("inf")] * size
    root = 0  # can be any vertex of the graph

    heap = [(0, root)]
    seen = [False] * size

    while heap:
        w, u = heappop(heap)
        if not seen[u]:
            spanning += w
            seen[u] = True

            for e in graph.incident_edges(u):
                v = e.opposite(u)
                if e.weight < D[v]:
                    D[v] = e.weight
                    heappush(heap, (e.weight, v))

    return total - spanning


if __name__ == "__main__":
    print(main())
