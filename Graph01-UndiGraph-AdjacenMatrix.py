# 采用邻接矩阵实现图（AdjacencyMatrix）

# 图是有n个顶点，在实现邻接矩阵时，需要构建n*n的二维矩阵
#    v1  v2  v3  v4  ...vn
# v1 0   1   1   1      0
# v2 1   0
# v3 1      0
# ...
# vn 0                 0

# 邻接矩阵的基本性质：
# 1. 使用AdjMatrix[i][j] 来存储图数据中顶点之间的邻接关系；
# 2. 当顶点之间存在邻接关系，则AdjMatrix[i][j]=1，否则为0；
# 3. 邻接矩阵的主对角线上的数据均为0，表示顶点的邻接点是其自身，所以为0；
# 4. 当存储的数据是带权的图，则邻接矩阵中元素的值是邻接点之间的权值，AdjMatrix[i][j]=w(i,j)；
# 5. 对于无向图而言，邻接矩阵是关于主对角线对称的二维矩阵，
#    而对有向图而言，则不一定是对称矩阵，当且仅当有向图是完全有向图时，才是对称矩阵；
# 6. 对于无向图而言，顶点的度是邻接矩阵对应行或者对应列的和，
#    而对有向图而言，顶点的度是顶点的入度和顶点的出度之和，顶点的入度是顶点所在列的元素值之和，顶点的出度是顶点所在行的元素值之和。

# 前提假设：
#   图数据中的边是由顶点偶对构成(u,v)或(u,v,w)，即图是按照边来划分的，
#   给出的形式是列表形式，其中列表元素是顶点偶对[(u,v),(v,x),]或者[(u,v,w0),(v,x,w1),]

# 图的方法设计有：
# 1.图的邻接矩阵
# 2.图的邻接关系
# 3.图的顶点度
# 4.图的邻接顶点
# 5.图的广度优先遍历
# 6.图的深度优先遍历
# 7.图的单源最短路径
# 8.图的任意点对之间最短路径

# 创建邻接矩阵的步骤：
# 1. 构建顶点列表
# 创建邻接矩阵的程序设计
# 顶点偶对 vertexpair
# 顶点偶对列表 vertexpairlist
# 2. 创建顶点编号与顶点名称的字典
# 3. 创建邻接矩阵


# 设计图的遍历说明：
# 在设计图的广度优先遍历和深度优先遍历时，都是采用的非递归方法来实现的，
# 这两种图遍历的方式仅仅是在顶点进入容器（栈/队列）与退出容器的优先顺序不一样：
#    深度优先遍历：邻接点进入的容器是栈，保证了后进入栈的顶点优先退出栈（LIFO）；
#    广度优先遍历：邻接点进入的容器是队列，保证了先进入队列的顶点优先退出对列（FIFO）。

class Graph:
    vertexlist = []  # 存放顶点的列表(全局列表)
    vertexdict = {}  # 存放顶点编码与顶点名称（全局字典）
    adjmatrix = []  # 存放顶点与边关系的邻接矩阵（全局列表）
    
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
            Graph.adjmatrix[i][j] = item[2]  # 无权图的邻接关系为1，有权图的邻接关系为w(i,j)
            Graph.adjmatrix[j][i] = item[2]  # 无权图的邻接关系的对称关系为1，有权图的邻接关系的对称关系为w(i,j)
    
    # 求图顶点的度
    @staticmethod
    def vertexdegree():
        degreedict = {}
        # 顶点的个数
        vertexnum = len(Graph.adjmatrix)
        # 遍历邻接矩阵
        for row in range(vertexnum):
            degree = 0
            for col in range(vertexnum):
                if Graph.adjmatrix[row][col] > 0:
                    degree += 1
            vertexname = Graph.vertexdict[row]
            degreedict[vertexname] = degree
        
        return degreedict
    
    # 判定邻接关系
    @staticmethod
    def adjrelation(vertex_u, vertex_w):
        
        # 判定顶点u与顶点w是否邻接
        row = 0
        col = 0
        for key, value in Graph.vertexdict.items():
            if Graph.vertexdict[key] == vertex_u:
                row = key
            if Graph.vertexdict[key] == vertex_w:
                col = key
        if Graph.adjmatrix[row][col] > 0:
            return True
        else:
            return False
    
    # 输出指定顶点的邻接顶点
    @staticmethod
    def adjvertex(somevertex):
        # 记录邻接顶点的列表
        adjvers = []
        # 判定指定顶点是否有邻接顶点
        row = 0
        col = 0
        for key, value in Graph.vertexdict.items():
            if Graph.vertexdict[key] == somevertex:
                row = key
        while col < len(Graph.adjmatrix[row]):
            if Graph.adjmatrix[row][col] > 0:
                adjvers.append(col)
            col += 1
        for i in range(len(adjvers)):
            vertexcode = adjvers[i]
            if vertexcode in Graph.vertexdict.keys():
                vertexname = Graph.vertexdict[vertexcode]
                adjvers[i] = vertexname
        
        return adjvers
    
    # 图的深度优先遍历（非递归方法）
    @staticmethod
    def gdfs():
        # 存放深度优先遍历结果的列表
        dfsres = []
        # 1-图遍历
        # 赋初始值-栈存放顶点的邻接点（后入栈的顶点优先出栈）
        stack = [0]
        # 顶点已经访问的标志数组
        visited = [0 for _ in range(len(Graph.adjmatrix))]
        while stack:
            row = stack.pop()
            dfsres.append(row)
            for col in range(len(Graph.adjmatrix[row])):
                # 将满足条件的邻接点加入到栈中：存在邻接关系且未被访问且未入栈的顶点
                if Graph.adjmatrix[row][col] > 0 and visited[col] == 0 and (col not in stack):
                    stack.append(col)
            visited[row] = 1
        
        for i in range(len(dfsres)):
            dfsres[i] = Graph.vertexdict[dfsres[i]]
        return dfsres
    
    # 图的广度优先遍历（非递归方法）
    @staticmethod
    def gbfs():
        # 存放广度优先遍历结果的列表
        bfsres = []
        # 1-图遍历
        # 赋初始值-队列存放顶点的邻接点（先入队列的顶点优先出队列）
        queue = [0]
        # 顶点已经访问的标志数组
        visited = [0 for _ in range(len(Graph.adjmatrix))]
        while queue:
            row = queue.pop(0)
            bfsres.append(row)
            for col in range(len(Graph.adjmatrix[row])):
                # 将满足条件的邻接点加入到栈中：存在邻接关系且未被访问且未入栈的顶点
                if Graph.adjmatrix[row][col] > 0 and visited[col] == 0 and (col not in queue):
                    queue.append(col)
            visited[row] = 1
        
        for i in range(len(bfsres)):
            bfsres[i] = Graph.vertexdict[bfsres[i]]
        return bfsres
    
    # 单源最短路径
    
    # 任意点对之间最短路径
    
    
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
                ('V8', 'V9', 1)]

    print('>> 无向图的存储结构为邻接矩阵<<')
    g.adjacencymatrix(verpairs)
    print('>> 无向图顶点的度')
    print(g.vertexdegree())
    print('>> 无向图判定是否为邻接点:')
    print(g.adjrelation('V1', 'V5'))
    print('>> 无向图指定顶点的邻接顶点:')
    print(g.adjvertex('V1'))
    print('>> 无向图的深度优先遍历:')
    print(g.gdfs())
    print('>> 无向图的广度优先遍历:')
    print(g.gbfs())
