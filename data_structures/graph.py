class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, v):
        # Add { v: [] }
        if v not in self.adj_list:
            self.adj_list[v] = []
        
    def display(self):
        # Makes a comarison of all vertex pointing its connections
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
    
    
class UndirectedGraph(Graph):
    def add_edge(self, u, v):
        # Makes sure the vertex exists
        self.add_vertex(u)
        self.add_vertex(v)
        # Defines u -> v and v -> u
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) 

class DirectedGraph(Graph):
    def add_edge(self, u, v):
        # Makes sure the vertex exists
        self.add_vertex(u)
        self.add_vertex(v)
        # Defines u -> v 
        self.adj_list[u].append(v)
        
import heapq        

class WeightedGraph(DirectedGraph):
    def add_edge(self, u, v, weight = 1):
        self.add_vertex(u)
        self.add_vertex(v)
        # Defines u -> v 
        self.adj_list[u].append((v , weight))
        
    def dijkstra(self, start):
        # Creates a new dictionary whith the values of each of them to infinite/float('inf')
        distances = { v: float('inf') for v in self.adj_list }
        # Set start (the place where you want to start) as 0
        distances[start] = 0
        # Creates a tuple of the values of 0 and the vertex name
        heap = [(0, start)] # -> (0, "A")
        
        while heap:
            # Gets the values from the tuple with the smallest distance
            current_dist, u = heapq.heappop(heap)
            
            # Skip this vertex because  we found a shorter path
            if current_dist > distances[u]:
                continue
             
            # For each vertex and weight
            for v, weight in self.adj_list[u]:
                # Distance to neighbor (v) through the smallest weight (u)
                distance = current_dist + weight
                
                # If this path is shorter than any previous one 
                if distance < distances[v]:
                    # Update the shortest
                    distances[v] = distance
                    # Insert the new value
                    heapq.heappush(heap, (distance, v))
                    
        return distances
    
        