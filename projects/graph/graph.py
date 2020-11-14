"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # vertex_id --> set of neighbors 
        self.vertices = {}
        self.stack = deque()
        self.queue = deque()
        self.visited = set()


    def __repr__(self):
        return str (self.vertices)


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with vertex id and  set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, from_vertex_id, to_vertex_id):
        """
        Add a directed edge to the graph.
        """
        # find vertex v1 in our vertices, add v2 to the set of edges
        if from_vertex_id in self.vertices and to_vertex_id in self.vertices:
            self.vertices[from_vertex_id].add(to_vertex_id)
        else:
            print("Atempting to add edge to non-existing nodes")
            return


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def remove_vertex(self, vertex_id):
        """
        Remove vertex and all assosiated edges with it 
        """
        if vertex_id not in self.vertices:
            print("Attempting to remove non-existing node")
            return
        self.vertices.pop(vertex_id)
        print(f'after pop {self.vertices}')
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)


    def remove_edges(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to remove edges from non-existent vertex")
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            curNode = queue.popleft()
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.vertices[curNode]:
                    queue.append(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            curNode = stack.pop()
            if curNode not in visited:
                visited.add(curNode)
                print(curNode)
                for neighbor in self.vertices[curNode]:
                    stack.append(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        return self.dft_recursive_helper(starting_vertex, visited)

            
    def dft_recursive_helper(self, curr_vertex, visited):
        """
        recurrsion helper for depth-first traversal, in order to reference visited set
        """
        visited.add(curr_vertex)
        print(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                # recursive call
                self.dft_recursive_helper(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        # push the current path you're on onto the queue, instead of just a single vertex
        queue.append([starting_vertex])
        while len(queue) > 0:
            curPath = queue.popleft()
            # the current node you're on is the last nodein the path
            curNode = curPath[-1]
            if curNode == destination_vertex:
                return curPath
            if curNode not in visited:
                visited.add(curNode)
                for neighbor in self.vertices[curNode]:
                    newPath = list(curPath)  # make a copy of the current path
                    newPath.append(neighbor)
                    queue.append(newPath)


    # Returns a path to th descination_vertex from starting_vertex
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = deque()
        # push the current path you're on onto the stack, instead of just a single vertex
        stack.append([starting_vertex])
        while len(stack) > 0:
            curPath = stack.pop()
            curNode = curPath[-1] # the current node you're on is the last nodein the path
            if curNode == destination_vertex:
                return curPath
            if curNode not in visited:
                visited.add(curNode)
                for neighbor in self.vertices[curNode]:
                    newPath = list(curPath) # make a copy of the current path
                    newPath.append(neighbor)
                    stack.append(newPath)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)
    # print(graph.get_neighbors(7))
    # graph.remove_vertex(2)
    # graph.remove_edges(3,5)
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
