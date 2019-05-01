# https://www.programiz.com/dsa/graph-adjacency-matrix for basic graph functionality
# additional functionality added by Dan Lesko

from collections import defaultdict
import heapq
import sys

class Graph(object):
    def __init__(self, vertices):
        self.adj_matrix = []
        for i in range(vertices):
            self.adj_matrix.append([0 for i in range(vertices)])
        self.V = vertices
        self.graph_list = []
        self.primMST = []
        self.kruskalMST = []
        self.graph_dict_v2 = dict()

    def add_edge(self, v1, v2, w):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adj_matrix[v1][v2] = w
        self.adj_matrix[v2][v1] = w
        self.graph_list.append([v1, v2, w])

        if str(v1) in self.graph_dict_v2:
            temp = self.graph_dict_v2[str(v1)]
            temp.update({str(v2): int(w)})
            self.graph_dict_v2[str(v1)] = temp
        else:
            self.graph_dict_v2[str(v1)] = {str(v2): int(w)}

        if str(v2) in self.graph_dict_v2:
            temp = self.graph_dict_v2[str(v2)]
            temp.update({str(v1): int(w)})
            self.graph_dict_v2[str(v2)] = temp
        else:
            self.graph_dict_v2[str(v2)] = {str(v1): int(w)}

    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def contains_edge(self, v1, v2):
        return True if self.adj_matrix[v1][v2] > 0 else False

    def __len__(self):
        return self.V

    def to_string(self):
        for row in self.adj_matrix:
            for val in row:
                print('{:4}'.format(val)),
            print

    ### The following implemented for this project: ###

    # from textbook
    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        return i

    # from textbook page 571
    def union(self, parent, rank, x, y):
        xfind = self.find(parent, x)
        yfind = self.find(parent, y)
        if rank[xroot] < rank[yfind]:
            parent[xfind] = yfind
        elif rank[xfind] > rank[yfind]:
            parent[yfind] = xfind
        else:
            parent[yfind] = xfind
            rank[xfind] += 1

    # O(ElogV)
    def kruskal(self):
        result = []

        # initialize iterators
        i, e = 0, 0

        # sort the edges by weight
        self.graph_list = sorted(self.graph_list, key=lambda item: item[2])

        # create parent and edge rank arrays
        parent = [];
        rank = []

        # append every node to the rank and parent arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # iterate through the vertices
        while e < self.V - 1:
            v1, v2, w = self.graph_list[i]
            i = i + 1
            x = self.find(parent, v1)
            y = self.find(parent, v2)
            # do edges belong to the same tree?
            if x != y:
                e = e + 1
                result.append([v1, v2, w])
                self.union(parent, rank, x, y)

        self.kruskalMST = result
        return result

    # shitty implementation
    def prims(self):  # , num vertices, Graph
        V = self.V
        G = self.adj_matrix

        # arbitrarily choose initial vertex from graph
        vertex = 0

        # initialize empty edges array and empty MST
        MST = []
        edges = []
        visited = []
        minEdge = [None, None, sys.maxsize]

        # run prims algorithm until we create an MST
        # that contains every vertex from the graph
        while len(MST) != V - 1:

            # mark this vertex as visited
            visited.append(vertex)

            # add each edge to list of potential edges
            for r in range(0, V):
                if G[vertex][r] != 0:
                    edges.append([vertex, r, G[vertex][r]])

            # find edge with the smallest weight to a vertex
            # that has not yet been visited
            for e in range(0, len(edges)):
                if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                    minEdge = edges[e]

            # remove min weight edge from list of edges
            edges.remove(minEdge)

            # push min edge to MST
            MST.append(minEdge)

            # start at new vertex and reset min edge
            vertex = minEdge[1]
            minEdge = [None, None, float('inf')]

        self.primMST =  MST
        return MST

    # should be O(m +nlogn)
    def primHeap(self):
        # arbitrarily choose initial vertex from graph
        start = '0'

        graph = self.graph_dict

        # initialize empty edges array and empty MST
        MST = dict()
        visited = set([starting_vertex])

        # initialize all edges from starting vertex
        edges = [
            (cost, start, next)
            for next, cost in graph[start].items()
        ]

        #create priority queue
        heapq.heapify(edges)

        # while edges still exist in heap
        while edges:

            # get edge
            weight, last, next = heapq.heappop(edges)

            # if we have not gone to that vertex
            if next not in visited:

                # add to visited
                visited.add(next)
                # add to mst
                MST[last].add(next)

                #add next set of edges to heap
                for to_next, weight in graph[next].items():
                    if to_next not in visited:
                        heapq.heappush(edges, (weight, next, to_next))

        return mst