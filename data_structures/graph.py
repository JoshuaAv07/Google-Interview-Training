class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, v):
        # Add { v: [] }
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def add_edge(self, u, v):
        # Creates the vertex if not exist
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        
        # Defines u -> v and v -> u
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # Undirected
        
    def display(self):
        # Makes a comarison of all vertex pointing its connections
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
    