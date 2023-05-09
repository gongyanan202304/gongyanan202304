# 树的遍历-广度优先遍历（非递归方法）

# 1：树的结构是采用节点链表方法来实现
# 2：树的属性方法有：叶子节点的个数统计、叶子节点、树的高度、返回左兄弟、返回右兄弟、补齐空左右节点
# 3：树的遍历方法有：深度优先遍历（前序遍历、中序遍历、后序遍历）、层次遍历（广度优先遍历）
#
# 1：在使用树的遍历的时候, 先需要进行树的创建，在本脚本中使用节点链表的形式来存储树的结构
# 2：树的遍历1：前序遍历、中序遍历、后序遍历三种深度优先的遍历DFS(使用了递归方法与非递归方法)
# 3：树的遍历2：广度优先遍历（层次遍历）BFS
# 4：本脚本是广度优先遍历代码

# 设计方法-节点链表法

class TreeNode:
    """
    定义树节点
    # 参数说明：
        data : 存储节点数据
        left : 节点左子树
        right: 节点右子树
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """创建二叉树"""
    def __init__(self):
        self.root = None  # 初始化根节点
        self.ls = []  # 存储根节点(双亲节点)的位置值的队列
        self.breadthresult = []  # 存放广度遍历结果的列表

    def insertnode(self, data):

        node = TreeNode(data)  # 实例化树节点
        if self.root is None:
            # 判定树的根节点为空，添加根节点，并将根节点的地址添加到列表中
            self.root = node
            self.ls.append(self.root)
        else:
            rootnode = self.ls[0]  # 取出第一个节点作为当前的根节点（不一定是整个树的根节点，而是双亲节点）
            if rootnode.left is None:  # 当前根节点的左子树是空树
                rootnode.left = node  # 将节点值赋给当前根节点的左子树
                self.ls.append(rootnode.left)  # 将节点值存放在列表中作为双亲节点下次被取出来
            elif rootnode.right is None:  # 当前根节点的右子树是空树
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)  # 将列表中的第一个元素弹出，表示已经完成了左右子树的添加

# 层次遍历（广度优先遍历）
    def breadthfirsttraversal(self, tree):
        if tree is None:
            return
        sequence = []  # 声明一个先进先出的队列存放子树
        # result = []  # 声明一个列表存放节点数值
        node = tree
        sequence.append(node)  # 现将整个树假如队列中
        while sequence:  # 当前队列不为空，表示队列中还有需要遍历的子树
            node = sequence.pop(0)  # 当前队列中的子树出队列
            # result.append(node.data)  # 将当前子树中的根节点的数值存放在reslut列表中
            self.breadthresult.append(node.data)
            if node.left is not None:  # 当前子树的左子树存在，则先加入到队列中
                sequence.append(node.left)
            if node.right is not None:  # 当前子树的右子树存在，则后加入到队列中
                sequence.append(node.right)
        # return result
        return self.breadthresult


# 主函数


if __name__ == '__main__':
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    btree = BinaryTree()
    for i in range(0, 10):
        btree.insertnode(i)
    
    # 2：调用遍历方法
    
    if __name__ == '__main__':
        # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
        btree = BinaryTree()
        for i in range(0, 10):
            btree.insertnode(i)
        
        # 2：调用树的方法
        print('# 2：调用树的方法')
        print('>> 层次遍历（广度优先遍历：）')
        print(btree.breadthfirsttraversal(btree.root))
        