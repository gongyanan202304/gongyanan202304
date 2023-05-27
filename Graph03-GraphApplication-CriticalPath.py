# 图的应用-2
# 关键路径与关键活动
# AOE的说明：
# 1-顶点表示事件
# 2-边表示活动
# 3-边上的权值表示活动的持续时间

# 关键路径(CriticalPath)是指顶点（事件）的最早发生时间与最晚发生时间相等的顶点所构成的路径
# 关键活动(CriticalActivity)是指边（活动）的最早发生时间与最晚发生时间相等的边组成的序列

# 关键路径的程序设计
# 假设：图数据中顶点
class Graph:
    vertexlist = []  # 存放顶点的列表(全局列表)
    vertexdict = {}  # 存放顶点编码与顶点名称（全局字典）
    adjmatrix = []  # 存放顶点与边关系的邻接矩阵（全局列表）
    vertexearliest = []  # 存放顶点的最早发生时间
    vertexlatest = []  # 存放顶点的最晚发生时间
    arcearliest = []  # 存放边的最早发生时间
    arclatest = []  # 存放边的最晚发生时间
    
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
            Graph.adjmatrix[i][j] = item[2]  # 无权图的邻接关系为1，有权有向图的邻接关系为w(i,j)
   
    # 顶点的最早发生时间与最晚发生时间
    @staticmethod
    def vertextime():
        # 求入度为0与出度为0的顶点
        invertexzero = 0
        outvertexzero = 0
        outdegree = 0
        for i in range(len(Graph.vertexlist)):
            
            for j in range(len(Graph.vertexlist)):
                if sum(Graph.adjmatrix[i]) == 0:
                    outvertexzero = i
                outdegree += Graph.adjmatrix[j][i]
            if outdegree == 0:
                invertexzero = i
        print(invertexzero)
        print(outvertexzero)
        
        # 顶点最早发生时间
        # 1-初始化顶点最早时间
        Graph.vertexearliest = [0 for _ in range(len(Graph.vertexlist))]
        vertexmaxtime = 0  # 顶点最大发生时间
        pass
        
  
# 主函数
if __name__ == "__main__":
    g = Graph()
    verpairs = [('V1', 'V2', 4),
                ('V1', 'V3', 7),
                ('V2', 'V4', 3),
                ('V2', 'V5', 10),
                ('V3', 'V5', 8),
                ('V3', 'V6', 9),
                ('V4', 'V7', 7),
                ('V5', 'V7', 5),
                ('V5', 'V8', 6),
                ('V5', 'V6', 11),
                ('V6', 'V8', 8),
                ('V7', 'V8', 2)]
    
    print('>> 无向图的存储结构为邻接矩阵<<')
    g.adjacencymatrix(verpairs)
    print(Graph.adjmatrix)
    print(Graph.vertexlist)
    print(Graph.vertexdict)
    print('>> 最早与最晚发生时间：')
    print(g.vertextime())
 