# 图的应用-1
# 拓扑排序(TopologicalSort)
# 1. 逆拓扑序列
# 2. 拓扑序列

# 拓扑排序的典型应用是在AOV网中
# 活动的先后顺序排成一个序列，任何一个活动都不会依赖它后面的活动
# 在AOV网中，如果活动i优先于活动j，则在线性序列中顶点i排在顶点j的前面。
# 一个AOV网必须是一个无环有向图DAG


# 拓扑排序的基本思想：
# 1. 对生成拓扑序列来说，入度为0的顶点优先加入到栈中，而其后继结点的入度减1
# 2. 对生成逆拓扑排序来说，出度为0的顶点优先加入到对列中，而其前驱节点的出度减1

# 拓扑排序的基本步骤：
# 1-求正向拓扑序列：
# 1） 求取每个结点的入度，将入度为0的顶点v加入到队列中，
# 2） 将顶点v的后继顶点的入度减1
# 3） 将顶点v出队列，
# 4） 将顶点v标记为已经访问（0-表示未被访问，1-表示已被访问）
# 5） 遍历顶点v的后继顶点，
# 6） 重复步骤1）～5），直到队列中的顶点元素个数为0
# 7） 判定图中的所有顶点是否已经被全部访问，若没有未被全部访问，则表示有向图中存在环，否则，输出拓扑序列。

# 2-求逆向拓扑序列：
# 1） 求取每个结点的出度，将出度为0的顶点v加入到队列中，
# 2） 将顶点v的前驱顶点的出度减1
# 3） 将顶点v出队列，
# 4） 将顶点v标记为已经访问（0-表示未被访问，1-表示已被访问）
# 5） 遍历顶点v的前驱顶点，
# 6） 重复步骤1）～5），直到队列中的顶点元素个数为0
# 7） 判定图中的所有顶点是否已经被全部访问，若没有未被全部访问，则表示有向图中存在环，否则，输出拓扑序列。


# 拓扑排序的程序设计：
# 假设传入的数据是邻接矩阵（DAG的邻接矩阵形式）


class Graph:
    vertexlist = []  # 存放顶点的列表(全局列表)
    vertexdict = {}  # 存放顶点编码与顶点名称（全局字典）
    adjmatrix = []  # 存放顶点与边关系的邻接矩阵（全局列表）
    indegreedict = {}  # 存放顶点的入度的字典（全局字典）
    outdegreedict = {}  # 存放顶点的出度的字典（全局字典）
    
    @staticmethod
    def adjacencymatrix(vertexpairlist):
        
        # 1-创建顶顶点列表：列表元素是顶点名称
        for verp in vertexpairlist:
            if verp[0] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[0])
            if verp[1] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[1])
        
        # 2-创建顶点字典（顶点编号:顶点名称）
        key = 0
        for item in Graph.vertexlist:
            value = item
            Graph.vertexdict[key] = value
            key += 1
        
        # 3-创建邻接矩阵（二维数组）
        
        # 邻接矩阵初始化
        Graph.adjmatrix = [[0 for _ in range(len(Graph.vertexlist))] for _ in range(len(Graph.vertexlist))]
        # 邻接矩阵赋值
        for item in vertexpairlist:
            i = Graph.vertexlist.index(item[0])
            j = Graph.vertexlist.index(item[1])
            Graph.adjmatrix[i][j] = 1  # 无环有向无权图的邻接关系为1
    
    # 顶点的入度indegree与顶点的出度outdegree
    @staticmethod
    def vertexdegree():
        
        # 顶点的个数
        vertexnum = len(Graph.adjmatrix)
        # 遍历邻接矩阵
        for col in range(vertexnum):
            indegree = 0  # 入度
            outdegree = 0  # 出度
            for row in range(vertexnum):
                if Graph.adjmatrix[row][col] > 0:
                    indegree += 1
                if Graph.adjmatrix[col][row] > 0:
                    outdegree += 1
                
            vertexname = Graph.vertexdict[col]
            Graph.outdegreedict[vertexname] = outdegree
            Graph.indegreedict[vertexname] = indegree
            
    # 拓扑排序
    @staticmethod
    def topologicalsort():
        # 求邻接矩阵的大小
        matrixsize = len(Graph.adjmatrix)
        # 拓扑序列（存放输出的拓扑结点）
        toporder = []
        # 访问标志数组（存放已经访问的结点）
        visited = [0 for _ in range(matrixsize)]
        # 顶点队列（存放入度为0的结点）
        queue = []
        
        # 判断每个顶点的入度与其邻接点
        # 初始化顶点的入度
        for vertex in Graph.indegreedict:
            if Graph.indegreedict[vertex] == 0:
                queue.append(vertex)
                
        while queue:
            # 入度为0的结点出队列
            vertex = queue.pop(0)
            # 入度为0的结点出队列后进入拓扑序列中
            toporder.append(vertex)
            row = Graph.vertexlist.index(vertex)  # 顶点编号
            visited[row] = 1  # 标记数组对应顶点已被访问
            for col in range(len(Graph.adjmatrix[row])):
                if Graph.adjmatrix[row][col] == 1 and visited[col] == 0 and (Graph.vertexlist[col] not in queue):
                    vertex = Graph.vertexlist[col]
                    Graph.indegreedict[vertex] -= 1
                    
                    if Graph.indegreedict[vertex] == 0:
                        queue.append(vertex)
            visited[row] = 1  # 标记数组对应的最后一个顶点（AOV中任务结束的顶点）已被访问

        # 当存在环时，则终止程序
        cyclevertex = [1 for flag in visited if flag == 0]
        if not queue and cyclevertex:
            return '有向图中存在环，退出程序'
        else:
            return toporder
    
    # 逆拓扑序列
    @staticmethod
    def reversedtopologicalsort():
        # 求邻接矩阵的大小
        matrixsize = len(Graph.adjmatrix)
        # 逆拓扑序列（存放输出的拓扑结点）
        reversedtoporder = []
        # 访问标志数组（存放已经访问的结点）
        visited = [0 for _ in range(matrixsize)]
        # 顶点队列（存放入度为0的结点）
        queue = []

        # 判断每个顶点的出度与其邻接点
        # 初始化顶点的出度
        for vertex in Graph.outdegreedict:
            if Graph.outdegreedict[vertex] == 0:
                queue.append(vertex)

        while queue:
            # 出度为0的结点出队列
            vertex = queue.pop(0)
            # 出度为0的结点出队列后进入逆拓扑序列中
            reversedtoporder.append(vertex)
            col = Graph.vertexlist.index(vertex)  # 顶点编号
            visited[col] = 1  # 标记数组对应顶点已被访问
            for row in range(len(Graph.adjmatrix)):
                if Graph.adjmatrix[row][col] == 1 and visited[row] == 0 and (Graph.vertexlist[row] not in queue):
                    vertex = Graph.vertexlist[row]
                    Graph.outdegreedict[vertex] -= 1
                    
                    if Graph.outdegreedict[vertex] == 0:
                        queue.append(vertex)
                    
            visited[col] = 1  # 标记数组对应的最后一个顶点（AOV中任务结束的顶点）已被访问

        # 当存在环时，则终止程序
        cyclevertex = [1 for flag in visited if flag == 0]
        if cyclevertex:
            return '有向图中存在环，退出程序'
        else:
            return reversedtoporder
    

# 主函数
if __name__ == "__main__":
    g = Graph()
    verpairs = [('V1', 'V2', 1),
                ('V1', 'V3', 2),
                ('V1', 'V4', 3),
                ('V2', 'V3', 1),
                ('V2', 'V5', 4),
                ('V3', 'V6', 6),
                ('V4', 'V6', 8),
                ('V5', 'V7', 4),
                ('V6', 'V8', 3),
                ('V7', 'V9', 2),
                ('V8', 'V9', 1),
                ]
    
    print('>> 有向图的存储结构为邻接矩阵<<')
    g.adjacencymatrix(verpairs)
    print(g.adjmatrix)
    print('>> 有向图顶点的入度')
    g.vertexdegree()
    print(g.indegreedict)
    print('>> 有向图顶点的出度')
    print(g.outdegreedict)
    print('>> 输出拓扑序列：')
    print(g.topologicalsort())
    print('>> 输出逆拓扑序列：')
    print(g.reversedtopologicalsort())
    