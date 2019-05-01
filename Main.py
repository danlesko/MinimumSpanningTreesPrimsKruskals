from Graph import Graph
import random
import time
import csv

def print_MST(MST, type, pretty):

    if type == 1:
        print("Kruskals: ")
    if type == 2:
        print("Prims: ")

    prettyMST = []
    for list in MST:
        prettylist = [int(list[0]), int(list[1]), int(list[2])]
        prettierlist = [chr(prettylist[0] + 97), chr(prettylist[1] + 97), prettylist[2]]
        prettyMST.append(prettierlist)

    if pretty:
        for list in prettyMST:
            print(str(list[0]) + " " + str(list[1]) + " -> " + str(list[2]))
    else:
        for list in MST:
            print(str(list[0]) + " " + str(list[1]) + " -> " + str(list[2]))

def create_completed_graph(G):

    for i in range(len(G)):
        for j in range (i+1,len(G)):
            weight = random.randint(1,10)
            G.add_edge(i, j, weight)

def create_sparse_graph(G):

    for i in range(len(G)):
        for j in range (i+1,len(G)):
            weight = random.randint(1,10)
            G.add_edge(i, j, weight)
            if j == i+3:
                break

if __name__=="__main__":
    g = Graph(10)

    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 3)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 4, 3)
    g.add_edge(1, 5, 1)
    g.add_edge(2, 4, 6)
    g.add_edge(2, 5, 5)
    g.add_edge(2, 9, 2)
    g.add_edge(3, 4, 2)

    g.add_edge(3, 7, 2)
    g.add_edge(3, 6, 3)
    g.add_edge(4, 7, 4)
    g.add_edge(4, 6, 5)
    g.add_edge(4, 5, 7)
    g.add_edge(4, 8, 3)
    g.add_edge(5, 9, 5)
    g.add_edge(5, 8, 3)
    g.add_edge(6, 7, 3)
    g.add_edge(7, 5, 1)

    g.add_edge(8, 9, 9)
    g.add_edge(3, 2, 7)
    g.add_edge(6, 5, 3)
    g.add_edge(9, 0, 2)
    g.add_edge(9, 6, 8)

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in g.adj_matrix]))

    primStart = time.time()
    MST = g.primHeap()
    primFinish = time.time()
    primTime = primFinish - primStart
    print(dict(MST))

    kruskalStart = time.time()
    MST = g.kruskal()
    kruskalFinish = time.time()
    kruskalTime = kruskalFinish - kruskalStart
    print_MST(MST, 1, False)

    # verticeList = [5, 10, 15, 20, 25, 50, 100, 200, 300, 400, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500, 5000, 7500, 10000]

    # for numVertex in verticeList:

        # for run in range(5):
        #
        #     g = Graph(numVertex)
        #
        #     adj_matrix = create_completed_graph(g)
        #
        #     primStart = time.time()
        #     MST = g.primHeap()
        #     primFinish = time.time()
        #     primTime = primFinish - primStart
        #     #print_MST(MST, 2, False)
        #
        #     kruskalStart = time.time()
        #     MST = g.kruskal()
        #     kruskalFinish = time.time()
        #     kruskalTime = kruskalFinish - kruskalStart
        #     #print_MST(MST, 1, False)
        #
        #     with open('project2_file_complete_v2.csv', mode='a+') as project_file:
        #         project_writer = csv.writer(project_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #
        #         # [arraysize, inversionsOriginal, inversionsSelection, (selectionInversions / inversionsOriginal), mergeTime, selectionTime]
        #         print(
        #             ["complete", numVertex, primTime, kruskalTime])
        #         project_writer.writerow(
        #             ["complete", numVertex, primTime, kruskalTime])

    # for numVertex in verticeList:
    #
    #     for run in range(5):
    #
    #         g = Graph(numVertex)
    #
    #         adj_matrix = create_sparse_graph(g)
    #
    #         primStart = time.time()
    #         MST = g.primHeap()
    #         primFinish = time.time()
    #         primTime = primFinish - primStart
    #         #print_MST(MST, 2, False)
    #
    #         kruskalStart = time.time()
    #         MST = g.kruskal()
    #         kruskalFinish = time.time()
    #         kruskalTime = kruskalFinish - kruskalStart
    #         #print_MST(MST, 1, False)
    #
    #         with open('project2_file_sparse_v3.csv', mode='a+') as project_file:
    #             project_writer = csv.writer(project_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #
    #             # [arraysize, inversionsOriginal, inversionsSelection, (selectionInversions / inversionsOriginal), mergeTime, selectionTime]
    #             print(
    #                 ["complete", numVertex, primTime, kruskalTime])
    #             project_writer.writerow(
    #                 ["sparse", numVertex, primTime, kruskalTime])