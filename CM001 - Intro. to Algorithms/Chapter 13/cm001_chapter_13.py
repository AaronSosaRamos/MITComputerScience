# -*- coding: utf-8 -*-
"""CM001 - Chapter 13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x-grhZiRpW7CAIqv7DpbvpbVEX0N29gE

#All-Pair Shortest Paths
"""

INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example directed graph
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

all_pairs_shortest_paths = floyd_warshall(graph)

for row in all_pairs_shortest_paths:
    print(row)

# Example undirected graph
graph = [
    [0, 3, INF, 7],
    [3, 0, 2, INF],
    [INF, 2, 0, 1],
    [7, INF, 1, 0]
]

all_pairs_shortest_paths = floyd_warshall(graph)

for row in all_pairs_shortest_paths:
    print(row)