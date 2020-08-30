"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) 
and explores as far as possible along each branch before backtracking.
"""

class DFS:

    @staticmethod
    def dfs(graph, start, visited=None):

        if visited is None:

            visited = set()

        visited.add(start)

        print(start)

        for next in graph[start] - visited:

            DFS.dfs(graph, next, visited)

        return visited


class Main:

    graph = {
        '0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0']),
        '3': set(['1']),
        '4': set(['2', '3']),
    }

    dfsObj = DFS()

    dfsObj.dfs(graph, '0')