"""
BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) 
and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node).
You must then move towards the next-level neighbour nodes.
"""

import collections

class BFS:

    @staticmethod
    def bfs(graph, root):

        visited, queue = set(), collections.deque([root])

        visited.add(root)

        while queue:

            # dequeue a vertex from queue
            vertex = queue.popleft()

            print(str(vertex) + " ", end = "")

            #  If not visited, mark it as visited, and
            # enqueue it

            for neighbour in graph[vertex]:                
            
                if neighbour not in visited:
                    
                    visited.add(neighbour)

                    queue.append(neighbour)


class Main:

    graph = {
        0 : [1, 2],
        1 : [2],
        2 : [3],
        3 : [1, 2],
    }

    bfsObj = BFS()

    bfsObj.bfs(graph, 0)