# Huffman Binary Tree and Huffman Coding
# 赫夫曼二叉树（=最优二叉树）与赫夫曼编码
# 运行版本
# 叶子节点的输入形式由列表变为字典
# 字典中叶子节点的名称是key,叶子节点的权值是value,例如：{'A':20, 'B':11}

class HuffmanTree:
    def __init__(self, name, data):
        
        self.name = name  # 节点名称
        self.weight = data  # 节点数据
        self.left = None  # 左子树指针
        self.right = None  # 右子树指针
        self.parent = -1  # 双亲指针
        self.hcode = ''  # 节点的赫夫曼编码
    
    @staticmethod
    def creatinghuffmantree(endnodes):  # 传入的叶子节点是字典的形式
        """采用自底向上的方式构造赫夫曼树"""
        if len(endnodes) == 0:
            return
        if len(endnodes) == 1:
            return endnodes[0]
        
        # 赫夫曼子树列表升序排列
        hufftreenodes = sorted([HuffmanTree(item, value) for item, value in endnodes.items()],
                               key=lambda node: node.weight)
        
        while len(hufftreenodes) > 1:
            # 从赫夫曼子树列表中取出根节点最小的2 棵子树
            lefttree = hufftreenodes.pop(0)
            righttree = hufftreenodes.pop(0)
            
            # 计算2 棵子树权值之和作为子树的根节点的权值
            rootweight = lefttree.weight + righttree.weight  # 子树权值之和（子树根节点权值）
            roottree = HuffmanTree(str(rootweight), rootweight)  # 子树根节点的名称与权值
            
            # 依据根节点构造一个子树
            roottree.left = lefttree  # 子树根节点的左子树
            roottree.right = righttree  # 子树根节点的左子树
            roottree.weight = rootweight  # 子树根节点的权值
            roottree.name = str(rootweight)  # 子树根节点的名称
            lefttree.parent = roottree  # 子树左子树的双亲节点
            righttree.parent = roottree  # 子树右子树的双亲节点
            
            # 将子树加载到赫夫曼子树的列表
            hufftreenodes.append(roottree)
            
            # 对新的赫夫曼子树列表升序排列
            hufftreenodes = sorted(hufftreenodes, key=lambda newnode: newnode.weight)
        
        return hufftreenodes[0]
    
    # 赫夫曼编码
    @staticmethod
    def huffmantreecoding(tree):
        """采用自顶向下的方式构造赫夫曼编码"""
        if tree is None:
            return
        hcodedict = {}  # 存放节点与其赫夫曼编码
        hqueue = [tree]  # 存放htree的队列
        
        while hqueue:  # 赫夫曼树队列不空
            tree = hqueue.pop(0)
            # 子树的左子树不为空，对左子树节点的赫夫曼编码赋值
            if tree.left is not None:
                tree.left.hcode = tree.hcode + '0'
                hqueue.append(tree.left)
            
            # 子树的右子树不为空，对右子树节点的赫夫曼编码赋值
            if tree.right is not None:
                tree.right.hcode = tree.hcode + '1'
                hqueue.append(tree.right)
            
            # 存储叶子节点的赫夫曼编码
            if tree.left is None and tree.right is None:
                hcodedict[str(tree.name)] = str(tree.hcode)
        
        return hcodedict
    
    # 层次遍历（广度优先遍历）
    @staticmethod
    def breadthfirsttraversal(tree):
        if tree is None:
            return
        sequence = []  # 声明一个先进先出的队列存放子树
        result = []  # 声明一个列表存放节点数值
        node = tree
        sequence.append(node)  # 现将整个树假如队列中
        while sequence:  # 当前队列不为空，表示队列中还有需要遍历的子树
            node = sequence.pop(0)  # 当前队列中的子树出队列
            result.append(node.name)  # 将当前子树中的根节点的数值存放在reslut列表中
            
            if node.left is not None:  # 当前子树的左子树存在，则先加入到队列中
                sequence.append(node.left)
            if node.right is not None:  # 当前子树的右子树存在，则后加入到队列中
                sequence.append(node.right)
        return result


# 主函数

if __name__ == "__main__":
    endnodedict = {'A': 4, 'B': 2, 'C': 5, 'D': 3, 'E': 4}
    htree = HuffmanTree
    huffmantree = htree.creatinghuffmantree(endnodedict)
    print('>> 赫夫曼树的基本信息：')
    print(huffmantree)
    print(huffmantree.name, huffmantree.weight)
    
    print('>> 层次遍历赫夫曼树：')
    print(huffmantree.breadthfirsttraversal(huffmantree))
    
    print('>> 节点的赫夫曼编码：')
    huffmancode = huffmantree.huffmantreecoding(huffmantree)
    for hname, hcode in huffmancode.items():
        print(f'{hname} huffman code is: {hcode}')  # 格式化的输出

# 思考：
# 还有3个问题没有写代码：
# 1是构造出一个实实在在的可视化的赫夫曼树，需要花费比较长的时间（todo）
# 2是赫夫曼编码的代码没有实现（done）
# 3是当给你叶子节点不再是一个简单的列表，而是一个嵌套列表或者字典的形式，即叶子节点有权值也有名称（done）
#   其实在输入之前可以将其它形式的叶子节点的名称与权值转化为字典的形式，即需要左一次转化为字典的操作，再使用该脚本。

# 解决思路：
# 1-关于赫夫曼编码的解决办法
# （1）构建一个含有双亲节点的Huffman树
# （2）使用列表元素是整数的叶子节点，暂时不考虑叶子节点的名称
# （3）使用一个数据域来存储节点编码
# （4）采用自顶向下的方式构建赫夫曼编码：
#     左子树的节点会继承子树根节点的赫夫曼编码，并在结尾处添加'0'
#     右子树的节点会继承子树根节点的赫夫曼编码，并在结尾处添加'1'
