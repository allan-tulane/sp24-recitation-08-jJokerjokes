from collections import deque
import heapq

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    distances = {vertex: float('infinity') for vertex in graph}
    edge_counts = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    edge_counts[source] = 0
    queue = [(0, 0, source)]  # (distance, edge_count, vertex)

    while queue:
        current_distance, current_edge_count, u = heapq.heappop(queue)

        if current_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_distance + weight
            edges = current_edge_count + 1
            if (distance < distances[v]) or (distance == distances[v] and edges < edge_counts[v]):
                distances[v] = distance
                edge_counts[v] = edges
                heapq.heappush(queue, (distance, edges, v))

    return {vertex: (distances[vertex], edge_counts[vertex]) for vertex in graph}


    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    queue = deque([source])
    while queue:
      current_node = queue.popleft()
      for neighbor in graph[current_node]:
          if neighbor not in parents:  
              parents[neighbor] = current_node  
              queue.append(neighbor)  
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
  
    while parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]
    
    return ''.join(path[::-1])

