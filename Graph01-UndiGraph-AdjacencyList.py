# 采用邻接列表实现图（AdjacencyList）

# 数据的输入形式是边与权重

# 顶点类与边类嵌套在图类中
class Graph:
    
    # -------------------------Nested Vertex Class -----------------------------------
    class Vertex:  # 顶点类
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'
        
        def __init__(self, x):
            """Do not call constructor directly, Use Graph's insert_vertex(x)."""
            self._element = x
        
        def element(self):
            """Return element associated with this vertex."""
            return self._element
        
        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))
    
    # ------------------------Nested Edge Class----------------------------------
    class Edge:  # 边类
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'
        
        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x
        
        def endpoints(self):
            """Return (u,v) tuple for vertexes u and v."""
            return self._origin, self._destination
        
        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            return self._destination if v == self._origin else self._origin
        
        def element(self):
            """Return element associated with this edge."""
            return self._element
        
        def __hash__(self):  # will allow edge to be a map/set key.
            return hash(id(self))
    
    # --------------Graph Methods------------------
    """Representation of a simple graph using an adjacency map."""
    def __init__(self, directed=False):
        """Create an empty Graph(undirected,by default)."""
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected.
        self._incoming = {} if directed else self._outgoing
    
    def is_directed(self):
        
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        
        return len(self._outgoing)
    
    def vertices(self):
        
        return self._outgoing.keys()
    
    def get_vertex(self, ver):
        for vertex in self.vertices():
            if vertex.element() == ver:
                return vertex
        
        return None
    
    def edge_count(self):
        
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges.
        return total if self.is_directed() else total//2
    
    def edges(self):
        edges = set()
        
        for secondary_map in self._outgoing.values():
            edges.update(secondary_map.values())
        return edges
        
    def get_edge(self, u, v):
        
        return self._outgoing[u].get(v)  # returns None if v not adjacent
    
    def degree(self, v, outgoing=True):
        
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        
        adj = self._outgoing if outgoing else self._incoming
        if v not in adj:
            return None
        for edge in adj[v].values():
            yield edge
            
    def adjacent_vertices(self, v, outgoing=True):
        if outgoing:
            if v in self._outgoing:
                return self._outgoing[v].keys()
            else:
                return None
        else:
            if v in self._incoming:
                return self._incoming[v].keys()
            else:
                return None
    
    def insert_vertex(self, x=None):
        for vertex in self.vertices():
            if vertex.element() == x:
                raise Exception('Vertex already exists')
        
        v = self.Vertex(x)
        self._outgoing[v] = {}
        
        if self.is_directed():
            self._incoming[v] = {}
        
        return v
    
    def insert_edge(self, u, v, x=None):
        if (v not in self._outgoing) or (u not in self._outgoing):
            raise Exception('One of the vertex dones not exist')
        if self.get_edge(u, v):
            raise Exception('Edge already exists.')
        
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e
    
    def delete_edge(self, u, v):
        if not self.get_edge(u, v):
            raise Exception('Edge is already non-existent.')
        
        u_neighbours = self._outgoing[u]
        del u_neighbours[v]
        v_neighbours = self._incoming[v]
        del v_neighbours[u]
        
        return None
    
    def delete_vertex(self, x):
        if (x not in self._outgoing) and (x not in self._incoming):
            raise Exception('Vertex already non-existent')
        
        secondary_map = self._outgoing[x]
        for vertex in secondary_map:
            # delete reference to incident edges
            if self.is_directed():
                del self._incoming[vertex][x]
            else:
                del self._outgoing[vertex][x]

        # delete reference to the vertex itself
        del self._outgoing[x]
        return None
    
    @staticmethod
    def create_graph(sequence, is_directed=False):
        graph = Graph(directed=is_directed)
        weight_mapping = {}
        
        if len(sequence[0]) == 3:
            weighted = True
        else:
            weighted = False
        
        for edge in sequence:
            source, destination = edge[0:2]
            if graph.get_vertex(source) is not None:
                source_vertex = graph.get_vertex(source)
            else:
                source_vertex = graph.insert_vertex(source)
                
            if graph.get_vertex(destination) is not None:
                destination_vertex = graph.get_vertex(destination)
            else:
                destination_vertex = graph.insert_vertex(destination)
                
            new_edge = graph.insert_edge(source_vertex,
                                         destination_vertex,
                                         str(source) + str(destination))
            if weighted:
                weight_mapping[new_edge] = edge[2]
            else:
                weight_mapping[new_edge] = 1
        
        return graph, weight_mapping
  

# 主函数
if __name__ == "__main__":
    # -------undirected Graph-----------
    g = Graph()
    # E = [('A', 'B'), ('B', 'C'), ('A', 'C')]
    E = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, weight = g.create_graph(E)
    print('>> Is the graph directed?: ' + str(G.is_directed()))
    A = G.get_vertex('a')
    print(G.incident_edges(A))
    print('A:', A)
    print(A.element())
    
    print('>> Incident edges to: ' + A.element())
    for arc in G.incident_edges(A):
        print(arc.element())
    print('>> Adjacency vertexes to: ' + A.element())
    adj_vers = G.adjacent_vertices(A, outgoing=True)
    for node in adj_vers:
        print(node.element())
    print('>> Deleting vertex "A"')
    G.delete_vertex(A)
    print(G.get_vertex(A))
    print('>> Vertexes count of G: ' + str(G.vertex_count()))
    for node in G.vertices():
        print(node.element())
    print('>> Edges count of G: ' + str(G.edge_count()))
    for arc in G.edges():
        print(arc.element())
    print('>> vertex count:')
    print(G.vertex_count())
    print([arc.element() for arc in G.edges()])
    
    # ----Directed Graph--------
    g = Graph()
    E = [('a', 'b', 10), ('b', 'c', 20), ('a', 'c', 30)]
    G, weight = g.create_graph(E, is_directed=True)
    print('>> Is the graph directed?: ' + str(G.is_directed()))
    A = G.get_vertex('a')
    print(G.incident_edges(A))
    print('>> Weight of Edges:')
    for key, value in weight.items():
        print('Edge:', key.element(), 'Value:', value)

    print('>> Incident edges to: ' + A.element())
    for arc in G.incident_edges(A):
        print(arc.element())
    print('>> Adjacency vertexes to: ' + A.element())
    adj_vers = G.adjacent_vertices(A, outgoing=True)
    for node in adj_vers:
        print(node.element())
    print('>> Deleting vertex "A"')
    G.delete_vertex(A)
    print(G.get_vertex(A))
    print('>> Vertexes count of G: ' + str(G.vertex_count()))
    for node in G.vertices():
        print(node.element())
    print('>> Edges count of G: ' + str(G.edge_count()))
    for arc in G.edges():
        print(arc.element())
    print('>> vertex count:')
    print(G.vertex_count())
    print([arc.element() for arc in G.edges()])
    