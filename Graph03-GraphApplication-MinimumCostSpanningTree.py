# 图的应用-4
# 无向图的最小生成树（Minimum Cost Spanning Tree）

# 最小生成树
# 一棵生成树的代价为该生成树中所有边的权值之和。对
# 于一个带权值的连通图，其不同生成树所对应的权值总和（即生成树的代价）也是不同的，
# 称代价最小的生成树为最小代价生成树，简称最小生成树。

# 求解最小生成树的算法：
# 算法1-Prime算法（扩点法）
#   通过扩展点的数目来生成最小生成树：
#   （1）将图中的顶点分为已经选择的顶点集合selected 与待选择的顶点集合waited；
#   （2）从selected集合中的选择所有的顶点v分别与waited 集合中所有顶点u进行组合<v,u>；
#   （3）每个组合的顶点对都存在一个边的权重w(v,u)，从其中选择权重最小的边<v,u>；
#   （4）将权重值最小的边对应的顶点u，加入到selected集合中；
#   （5）将权重值最小的边加入到最小生成树的边集合中；
#   （6）重复步骤（2）（3）（4）（5），直到waited集合中的顶点个数为0，结束程序。

# 算法2-Kruskal算法（扩边法）
#   通过扩展边的数目来生成最小生成树：
#   （1）将图中的边按照边的权重值进行非递减排序（可用排序方法：快速排序、插入排序、归并排序、冒泡排序等），生成有序边数组edges；
#   （2）将图中的所有顶点的进行连通分量数组vset并编号：v0:0,v1:1,...vi:i，使得每个顶点的连通分量的编号互异；
#   （3）从有序边数组edges中选择权重值最小的边<v,u,ewmin>，判定边的两个顶点v,u的连通分量编号是否相同:
#        如果不相同，则将最小权值边<v,u,ewmin> 加入到最小生成树的边集合treearc中，并将顶点u的连通编号修改为顶点v的连通编号；
#        如果相同，则将该最小权值边<v,u,ewmin> 舍弃；
#   （4）重复步骤（3）直到所有的边已经被合并完成。

# 最小生成树的算法

class Graph:
    vertexlist = []  # 存放顶点的列表(全局列表)
    adjmatrix = []  # 存放顶点与边关系的邻接矩阵（全局列表）
    edges = []  # 存放权重值有序的边

    @staticmethod
    def adjacencymatrix(vertexpairlist):
        
        # 1-创建顶顶点列表：列表元素是顶点名称
        for verp in vertexpairlist:
            if verp[0] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[0])
            if verp[1] not in Graph.vertexlist:
                Graph.vertexlist.append(verp[1])
        Graph.vertexlist.sort()
        
        # 2-创建邻接矩阵（二维数组）
        
        # 邻接矩阵初始化
        # 没有关系的顶点之间是0
        Graph.adjmatrix = [[0 for _ in range(len(Graph.vertexlist))] for _ in range(len(Graph.vertexlist))]
        # 邻接矩阵赋值
        for item in vertexpairlist:
            i = Graph.vertexlist.index(item[0])
            j = Graph.vertexlist.index(item[1])
            Graph.adjmatrix[i][j] = item[2]  # 无权图的邻接关系为w(i,j)
            Graph.adjmatrix[j][i] = item[2]  # 无权图的邻接关系为w(i,j)
            
    # 算法1-最小生成树-Prim算法
    @staticmethod
    def mst_prim(ver):
        
        # 存放已经选择的顶点集合selected
        selected = [ver]
        # 存放待选的顶点集合waited
        waited = [v for v in Graph.vertexlist if v != ver]
        # 存放最小生成树边的集合treearc
        treearc = []
        
        # 扩点法
        while waited:
            # 边权重的初始值
            ewmin = float('inf')
            # 存放当前权重最小值的边
            arcmin = ''
            # waited集合中将要被选择的顶点w的初始值
            w = ''
            # 获取selected数组中的顶点在邻接矩阵中的行列位置
            for i in range(len(selected)):
                row = Graph.vertexlist.index(selected[i])
                for col in range(len(Graph.adjmatrix[row])):
                    # 当前顶点的邻接顶点不在selected数组中，则需要判定与selected数组中的顶点是否存在边
                    if (Graph.vertexlist[col] not in selected) and (Graph.adjmatrix[row][col] > 0)\
                            and (Graph.adjmatrix[row][col] < ewmin):
                        ewmin = Graph.adjmatrix[row][col]
                        s = Graph.vertexlist[row]
                        w = Graph.vertexlist[col]
                        arcmin = (s, w, ewmin)
                        
            # 在selected集合中添加顶点w
            selected.append(w)
            # 从waited集合中删除顶点w
            waited.remove(w)
            # 将遍历以后的权重值最小边放入最小生成树边的集合中
            treearc.append(arcmin)
        
        return treearc

    # 算法2-最小生成树-Kruskal算法
    @staticmethod
    def edgequicksort(vertexpairlist):
        if len(vertexpairlist) <= 1:
            return vertexpairlist
        # 对边按照边的权重进行快速排序
        pivot = vertexpairlist[0]  # 以第一条边的权重为标杆数据
        left = [vertexpairlist[i] for i in range(1, len(vertexpairlist)) if vertexpairlist[i][2] < pivot[2]]
        right = [vertexpairlist[i] for i in range(1, len(vertexpairlist)) if vertexpairlist[i][2] >= pivot[2]]
        
        return Graph.edgequicksort(left) + [pivot] + Graph.edgequicksort(right)
        
    @staticmethod
    def mst_kruskal(vertexpairlist):
        # 将排序好的边集合存放到辅助数组中

        Graph.edges += Graph.edgequicksort(vertexpairlist)

        # 存放最小生成树的连通边
        treearc = []
        # 顶点连通分量编号
        vset = [Graph.vertexlist.index(ver) for ver in Graph.vertexlist]
        
        # 扩边法
        for i in range(len(Graph.edges)):
            minarc = Graph.edges[i]
            v = minarc[0]
            u = minarc[1]

            # 判定2个顶点是否在同一个连通分量
            v_code = Graph.vertexlist.index(v)
            u_code = Graph.vertexlist.index(u)

            # 连通分量编码的合并
            newcode = vset[v_code]
            oldcode = vset[u_code]
            if newcode != oldcode:
                # 修改与顶点u的连通分量编码相同的连通分量编码为顶点v的连通分量编码
                for j in range(len(vset)):
                    if vset[j] == oldcode:
                        vset[j] = newcode
                # 在两个顶点的连通分量不同的前提下，权值边写入最小生成树边集合中
                treearc.append(minarc)
        
        # 返回最小生成树的连通边的集合
        return treearc


# 主函数
if __name__ == "__main__":
    g = Graph()
    verpairs = [('V0', 'V1', 4),
                ('V0', 'V2', 3),
                ('V0', 'V4', 7),
                ('V1', 'V2', 1),
                ('V1', 'V3', 9),
                ('V1', 'V5', 10),
                ('V2', 'V4', 2),
                ('V3', 'V2', 8),
                ('V3', 'V4', 12),
                ('V3', 'V5', 5),
                ('V4', 'V5', 13)
                ]

    print('>> 无向图的存储结构为邻接矩阵<<')
    g.adjacencymatrix(verpairs)
    print(g.adjmatrix)
    print('>> 无向图-最小生成树-Prim算法:')
    print(g.mst_prim('V0'))
    print('>> 无向图-最小生成树-Kruskal算法:')
    print(g.mst_kruskal(verpairs))
