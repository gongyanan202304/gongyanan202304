# 图的应用-3
# 最短路径(shortestpath)

# 最短路径的算法主要有4种：
# 最短路径算法-1：Dijkstra (迪杰斯特拉算法)
# 最短路径算法-2: Folyd (佛洛依德算法)
# 最短路径算法-3：Bellman-Ford (贝尔曼-福德算法)
# 最短路径算法-4：SPFA (Shortest Path Fast Algorithm)


# 最短路径算法设计：
# 在最短路径算法中，使用多种算法计算最短路径
import copy


class Graph:
    
    # 存放最短路径长度的数组dis
    dis = []
    # 存放最短路径顶点的数组path
    path = []
    # 存放顶点列表
    vertexlist = []
    # 存放顶点字典（顶点编号与顶点名称）
    vertexdict = {}
    # 存放邻接矩阵
    adjmatrix = []
    # 存放Floyd算法之后的邻接矩阵
    floydadjmatrix = []

    @staticmethod
    def adjacencymatrix(vertexpairlist):
        
        # 1-创建顶顶点列表：列表元素是顶点名称
        for verp in vertexpairlist:
            if verp[0] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[0])
            if verp[1] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[1])
        Graph.vertexlist.sort()
        
        # 2-创建顶点字典（顶点编号:顶点名称）
        key = 0
        for item in Graph.vertexlist:
            value = item
            Graph.vertexdict[key] = value
            key += 1
        
        # 3-创建邻接矩阵（二维数组）
        
        # 邻接矩阵初始化
        Graph.adjmatrix = [[float('inf') for _ in range(len(Graph.vertexlist))]for _ in range(len(Graph.vertexlist))]
    
        # 邻接矩阵赋值
        for item in vertexpairlist:
            i = Graph.vertexlist.index(item[0])
            j = Graph.vertexlist.index(item[1])
            Graph.adjmatrix[i][j] = item[2]  # 无环有向you权图的邻接关系为1
            Graph.adjmatrix[j][i] = item[2]  # 无环有向you权图的邻接关系为1
    
    # 构建最短路径算法-Dijkstra
    @staticmethod
    def dijkstrashortestpath(ver):
        """ver: 单源顶点"""
        # 单源顶点的最短路径
        n = len(Graph.vertexlist)
        visited = [ver]  # 存放已经访问过的顶点（作为最短路径的起点）
        # 1-最短路径长度初始化
        Graph.dis = [float('inf') for _ in range(len(Graph.vertexlist))]
        # 2-最短路径顶点初始化
        Graph.path = [[ver] for _ in range(len(Graph.vertexlist))]
        # 3-计算最短路径长度与最短路径顶点
        startindex = Graph.vertexlist.index(visited[-1])
        Graph.dis[startindex] = 0  # 最初源点的最短路径长度值为0（最初源点到自身的距离）
        
        while len(visited) < n:  # 循环入口
            row = Graph.vertexlist.index(visited[-1])
            for col in range(len(Graph.adjmatrix[row])):
                # 当前源点到其距离最近的邻接顶点小于邻接顶点的最短路径长度值
                if Graph.dis[row] + Graph.adjmatrix[row][col] < Graph.dis[col]:
                    print(Graph.adjmatrix[row][col], Graph.dis[col])
                    # 更新邻接点的最短路径长度
                    Graph.dis[col] = Graph.dis[row] + Graph.adjmatrix[row][col]
                    # 更新邻接点的最短路径顶点
                    Graph.path[col] = Graph.path[row] + [Graph.vertexlist[col]]
            
            # 找到下一个源点(上一次循环完成以后的生成路径长度最小值的邻接顶点)
            nextvalue = float('inf')
            nextkey = ''
            for i in range(len(Graph.dis)):
                if Graph.vertexlist[i] not in visited and Graph.dis[i] < nextvalue:
                    nextvalue = Graph.dis[i]
                    nextkey = Graph.vertexlist[i]
            # 将下一个源点加入到访问的列表中
            if nextkey == '':  # 说明已经到了出度为0的顶点
                break
            else:
                visited.append(nextkey)
    
    # 构建最短路径算法-Floyd算法
    @staticmethod
    def floydshortestpath():
        # 复制原邻接矩阵数据
        # adjmat = Graph.adjmatrix  # 怎样实现深度拷贝？
        Graph.floydadjmatrix = copy.deepcopy(Graph.adjmatrix)
        for i in range(len(Graph.floydadjmatrix)):
            for j in range(len(Graph.floydadjmatrix[i])):
                if i == j:
                    Graph.floydadjmatrix[i][j] = 0
                
        # 遍历顶点，以之为中间点mid
        for mid in range(len(Graph.floydadjmatrix)):
            # midver = Graph.vertexlist[mid]  # 中间点的名称
            for row in range(len(Graph.floydadjmatrix)):
                
                for col in range(len(Graph.floydadjmatrix[row])):
                
                    if Graph.floydadjmatrix[row][col] > Graph.floydadjmatrix[row][mid] + Graph.floydadjmatrix[mid][col]:
                        newvalue = Graph.floydadjmatrix[row][mid] + Graph.floydadjmatrix[mid][col]
                        Graph.floydadjmatrix[row][col] = newvalue
                
        return Graph.floydadjmatrix
    
    # 遍历最短路径长度数组，求每个顶点到其它顶点的距离之和sum
    @staticmethod
    def minshortestpath():
        minsum = float('inf')  # 最小和初始值
        resrow = 0
        for m in range(len(Graph.floydadjmatrix)):
            
            cursum = sum(Graph.floydadjmatrix[m])
            if cursum < minsum:
                minsum = cursum
                resrow = m
        vername = Graph.vertexlist[resrow]
        
        # 返回最短路径长度中的最小值与对应的顶点名称
        return vername, minsum
        

# 主函数
if __name__ == "__main__":
    
    vers = [('V0', 'V1', 20),
            ('V0', 'V2', 10),
            ('V0', 'V4', 10),
            ('V0', 'V5', 55),
            ('V1', 'V2', 25),
            ('V1', 'V3', 60),
            ('V3', 'V2', 30),
            ('V4', 'V2', 80),
            ('V3', 'V4', 25),
            ('V4', 'V5', 15),
            ('V5', 'V2', 10),
            ('V5', 'V3', 70)
            ]
    
    print('>> 有向图的存储结构为邻接矩阵<<')
    Graph.adjacencymatrix(vers)
    print('>> 输出顶点列表：')
    print(Graph.vertexlist)
    print('>> 输出邻接矩阵')
    print(Graph.adjmatrix)
    print('>> 最短路径-Dijkstra：')
    Graph.dijkstrashortestpath('V0')  # 以'V0'为源点
    print('>> 输出路径长度：')
    print(Graph.dis)
    print('>> 输出路径顶点：')
    print(Graph.path)
    print('>> 最短路径-Floyd：')
    print(Graph.floydshortestpath())
    print(Graph.floydadjmatrix)
    print('>> 最短路径之最小值：')
    print(Graph.minshortestpath())
