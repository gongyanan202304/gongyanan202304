# 图的遍历-广度优先遍历与深度优先遍历算法
# BreadthFirstSearch+DepthFirstSearch

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

    # ------------------------Nested Breadth First Search Class----------------------------------
    class BreadthFirstSearch:
        """图的广度优先遍历算法"""
    
        def __init__(self, graph):
            self.state = {vertex: 'unexplored' for vertex in graph.vertices()}
            self.has_cycle = False
            self.queue = []
            self.breadth_traversal = []
            self.visited_vertex = []  # 存放遍历顶点顺序的列表
    
        def call_bfs(self, graph, start):
            self.queue.append(start)
            self.state[start] = 'exploring'
            while self.queue:
                vertex = self.queue.pop(0)
                self.state[vertex] = 'explored'
                self.visited_vertex.append(vertex.element())
                for edge in graph.incident_edges(vertex):
                    neighbor = edge.opposite(vertex)
                    
                    if self.state[neighbor] == 'unexplored':
                        self.breadth_traversal.append(edge)
                        self.queue.append(neighbor)
                        self.state[neighbor] = 'exploring'
                    else:
                        if self.state[neighbor] == 'exploring':
                            self.has_cycle = True

    # -------------Nested Class Depth First Search---------------------------
    class DepthFirstSearch:
        """图的深度优先遍历算法"""
        def __init__(self, graph):
            self.time = 0
            self.state = {vertex: 'unexplored' for vertex in graph.vertices()}
            self.depth_traversal = []
            self.arrival = {vertex: None for vertex in graph.vertices()}
            self.departure = {vertex: None for vertex in graph.vertices()}
            self.edge_added = {edge: False for edge in graph.edges()}
            self.has_cycle = False
            if graph.is_directed:
                self.top_ordering = []
            else:
                self.top_ordering = None
        
        def dfs_compute(self, graph, start):
            self.state[start] = 'exploring'
            self.time = self.time + 1
            self.arrival[start] = self.time
            
            for edge in graph.incident_edges(start, outgoing=True):
                neighbor = edge.opposite(start)
                if self.state[neighbor] == 'unexplored':
                    self.depth_traversal.append(edge)
                    self.edge_added[edge] = True
                    self.dfs_compute(graph, neighbor)
            
                else:
                    if self.edge_added[edge]:
                        continue
                    if self.state[neighbor] == 'exploring':
                        self.has_cycle = True
                        
            self.time = self.time + 1
            self.departure[start] = self.time
            self.state[start] = 'explored'
            self.top_ordering.insert(0, start)
            
        def get_topological_order(self, graph, start):
            if not graph.is_directed:
                raise Exception("Graph is not directed!")
            self.dfs_compute(graph, start)
            if self.has_cycle:
                return None
            else:
                return self.top_ordering

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
        return total if self.is_directed() else total // 2
    
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
    E = [('a', 'b', 3), ('a', 'c', 4), ('b', 'd', 5), ('d', 'e', 6), ('d', 'f', 7), ('d', 'g', 9), ('e', 'h', 10),
         ('f', 'h', 10), ('g', 'h', 10)]
    G, weight = g.create_graph(E, is_directed=True)
    print('>> Breadth First Search: ')
    bfs = g.BreadthFirstSearch(G)
    print('>> 1-调用广度优先遍历算法：')
    bfs.call_bfs(G, G.get_vertex('a'))
    print('>> 2-打印图中结点的状态：')
    for key, value in bfs.state.items():
        print("Vertex:", key.element(), "State:", value)
    print('>> 3-打印图中访问的边：')
    for arc in bfs.breadth_traversal:
        print(arc.element())
    print('>> 4-打印图中访问的顶点：')
    print(bfs.visited_vertex)
    print('>> Depth First Search：')
    dfs = g.DepthFirstSearch(G)
    print('>> 1-调用深度优先遍历算法：')
    dfs.dfs_compute(G, G.get_vertex('a'))
    print('拓扑0：', dfs.top_ordering)
    print('>> 2-打印图中节点的状态：')
    for key, value in dfs.state.items():
        print("Vertex:", key.element(), "State:", value)
    print('>> 3-打印图中已经添加的边：')
    for key, value in dfs.edge_added.items():
        print("Edge:", key.element(), "Added:", value)
    print('>> 4-打印图中到达顶点的次数：')
    for key, value in dfs.arrival.items():
        print("arrival-vertex:", key.element(), "Times:", value)
    print('>> 5-打印图中出发顶点的次数：')
    for key, value in dfs.departure.items():
        print("departure-vertex:", key.element(), "Times:", value)
    print('>> 6-打印图中边的遍历顺序：')
    for arc in dfs.depth_traversal:
        print(arc.element(), end=' ')
    print('')
    print('>> 7-打印拓扑序列：')
    print('>>> 有向图：', G.is_directed())
    for top in dfs.top_ordering:
        print(top.element(), end=' ')
