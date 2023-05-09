# 本脚本设计完全二叉树有关的创建、遍历以及一些方法
# 1. 关于完全二叉树的说明：
# (1)完全二叉树的叶子节点在最大层和次大层上
# (2)除了最大层的节点以外，其它层的节点个数是power(2,i-1),其中i是表示树的节点所在的层次。

# 完全二叉树的创建
class TreeNode:
    """实现一个节点的类TreeNode类"""
    def __init__(self, data):
        self.data = data  # 数据域
        self.parent = None  # 双亲节点指针
        self.left = None  # 左孩子指针
        self.right = None  # 右孩子指针
     

class TreeQueue:
    def __init__(self):
        self.__members = list()
        
    def ismptyqueuee(self):
        return not len(self.__members)
    
    def enqueue(self, data):
        self.__members.insert(0, data)

    def dequeue(self):
        if self.ismptyqueuee():
            return
        return self.__members.pop()


class CompeleteBinaryTree:
    def __init__(self):
        self.root = None
        self.breadthtraverresult = []  # 存放广度优先遍历的结果
        self.preorderlst = []  # 前序遍历结果列表
        self.inorderlst = []  # 中序遍历结果列表
        self.postorderlst = []  # 后序遍历结果列表

        self.prefix_branch = '|-'
        self.prefix_trunk = '|'
        self.prefix_leaf = 'x'
        self.prefix_empty = ''
        self.prefix_left = '--L-'
        self.prefix_right = '-R-'
    
    def isemptycomtree(self):
        # 为空则返回True
        return not self.root
    
    # 为树添加节点
    def addnodes(self, data):
        node = TreeNode(data)  # 将数据data实例化为树节点
        if self.isemptycomtree():  # 当前树是一个空树
            self.root = node  # 将节点作为树的根节点
            return
        
        queue = TreeQueue()  # 声明一个树的队列
        queue.enqueue(self.root)  # 将整个树添加到树队列中
        while not queue.ismptyqueuee():  # 树队列不为空
            curtree = queue.dequeue()
            if curtree.left is None:
                curtree.left = node
                curtree.parent = curtree
                return
            queue.enqueue(curtree.left)
            if curtree.right is None:
                curtree.right = node
                curtree.parent = curtree
                return
            queue.enqueue(curtree.right)
            
    # 判定一个数据是否存在
    def getnodesexist(self, node):
        if self.isemptycomtree():
            return
        queue = TreeQueue()
        queue.enqueue(self.root)
        while not queue.ismptyqueuee():
            curtree = queue.dequeue()
            if curtree.data == node:
                return True
            if curtree.left is not None:
                queue.enqueue(curtree.left)
            if curtree.right is not None:
                queue.enqueue(curtree.right)
        return False
    
    # 树形结构展示树的节点
    @staticmethod
    def haschild(node):
        return node.left is not None or node.right is not None

    def showtree(self, node, prefix=None):
        if prefix is None:
            prefix = ''
            prefix_left_child = ''
        else:
            prefix = prefix.replace(self.prefix_branch, self.prefix_trunk)
            prefix = prefix.replace(self.prefix_leaf, self.prefix_empty)
            prefix_left_child = prefix.replace(self.prefix_leaf, self.prefix_empty)
            
        if self.haschild(node):
            if node.right is not None:
                print(prefix + self.prefix_branch + self.prefix_right + str(node.right.data))
                if self.haschild(node.right):
                    self.showtree(node.right, prefix + self.prefix_branch + ' ')
            else:
                print(prefix + self.prefix_branch + self.prefix_right)
            if node.left is not None:
                print(prefix + self.prefix_leaf + self.prefix_left + str(node.left.data))
                if self.haschild(node.left):
                    prefix_left_child += '  '
                    self.showtree(node.left, prefix + self.prefix_leaf + prefix_left_child)
            else:
                print(prefix + self.prefix_leaf + self.prefix_left)
    
    def gettreenodestyle(self, tree):
        if tree is None:
            return
        self.showtree(tree, prefix='')
        
    # 广度优先遍历
    def comtreebreadthtraver(self):
        if self.isemptycomtree():
            print('空二叉树')
            return
        
        queue = TreeQueue()
        queue.enqueue(self.root)  # 将整个树添加到树队列中
        while not queue.ismptyqueuee():
            curtree = queue.dequeue()  # 从树队列中取出队头的元素
            
            self.breadthtraverresult.append(curtree.data)  # 将树的根节点的数据域写入列表中
            
            if curtree.left is not None:  # 当前树的左子树不为空
                queue.enqueue(curtree.left)
                
            if curtree.right is not None:  # 当前树的右子树不为空
                queue.enqueue(curtree.right)
        
        return self.breadthtraverresult
    
    # 深度优先遍历-前序遍历-非递归方法
    def preordertraver(self, tree):
        if tree is None:
            return
        
        stack = [tree]
        tree = stack.pop()  # 第一个元素出栈
        while tree or stack:
            while tree:
                self.preorderlst.append(tree.data)
                stack.append(tree)
                tree = tree.left
            tree = stack.pop()
            tree = tree.right

        return self.preorderlst
    
    # 深度优先遍历-中序遍历-非递归方法
    def inordertraver(self, tree):
        if tree is None:
            return
        
        stack = [tree]
        tree = stack.pop()
        while stack or tree:
            while tree:
                stack.append(tree)
                tree = tree.left
            tree = stack.pop()
            self.inorderlst.append(tree.data)
            tree = tree.right
        
        return self.inorderlst
    
    # 深度优先遍历-后序遍历-非递归方法
    def postordertraver(self, tree):
        if tree is None:
            return
        seq = []
        stack = [tree]
        tree = stack.pop()
        
        while stack or tree:
            while tree:
                seq.append(tree.data)
                stack.append(tree)
                tree = tree.right
            tree = stack.pop()
            tree = tree.left
        
        while seq:
            self.postorderlst.append(seq.pop())
        
        return self.postorderlst
    
    
# 完全二叉树的测试

if __name__ == "__main__":
    ComTree = CompeleteBinaryTree()  # 实例化一棵树
    print(ComTree)
    print('isympy:', ComTree.isemptycomtree())
    print('>> 添加树的节点：')
    for item in range(0, 8):
        ComTree.addnodes(item)
        
    print('>> 广度优先遍历完全二叉树：')
    print(ComTree.comtreebreadthtraver())
    
    print('>> 深度优先-先序遍历完全二叉树：')
    print(ComTree.preordertraver(ComTree.root))
    
    print('>> 深度优先-中序遍历完全二叉树：')
    print(ComTree.inordertraver(ComTree.root))

    print('>> 深度优先-后序遍历完全二叉树：')
    print(ComTree.postordertraver(ComTree.root))
    
    print('>> 判定一个节点是否存在：')
    print(ComTree.getnodesexist(7))
    
    print('>> 展示树的节点形式：')
    print(ComTree.gettreenodestyle(ComTree.root))
