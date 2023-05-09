# 树的遍历-深度优先遍历（非递归方法）
# 这个脚本可以是设计成遍历的大一统的形式
# 1-设计思路：
# 在设计脚本时，以中序遍历-非递归为例
# 当节点列表中的最后一个元素是一个叶子节点，则把该叶子节点从列表中取出来并且添加到结果列表中，然后取出
# 节点列表中的最后一个元素作为子树来进行判定，如果不是叶子节点，则将该子树取出来，再进行右子树-根节点-左子树的方式
# 分解以后，添加到节点列表中。


# 2-解决问题：
# 下面的代码是非递归的方式实现的，
# 在前期设计代码是遇见了一个很严重的问题，
# 即从列表中取出来的节点是一个叶子节点，对其进行判定是有难度的
# 这期间也尝试了几种解法，都需要对上述的问题进行了特殊化处理，这显然是不具有普遍性的，应该摒弃，而找新的方法。
# 对于每一次遍历而言，加入节点队列中的元素是右子树、左子树、根节点。
# 在这里的根节点（当前根节点）是一个数值，将其转化为一个树节点的形式，即单个元素生成了一棵单节点的树，
# 如此一来，在节点列表中的元素均是树或者树节点的形式。
# 至此，非递归遍历的3种形式统一为一种形式的遍历结构。

# 3-算法思想：
# (1)使用栈来存放节点
# (2)节点入栈顺序：
#       前序遍历：右子树->左子树->根节点
#       中序遍历：右子树->根节点->左子树
#       后序遍历：根节点->右子树->左子树
# (3)节点出栈顺序：
#    A：若当前栈顶元素是单节点，则将该节点弹出栈
#    B：若当前栈顶元素是子树，则将该子树弹出栈，分解子树，并按照入栈顺序
#    C：重复A、B步骤，直到节点栈为空栈


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

    def insertnode(self, data):

        node = TreeNode(data)  # 实例化树节点
        if self.root is None:
            # 判定树的根节点为空，添加根节点，并将根节点的地址添加到列表中
            self.root = node
            self.ls.append(self.root)
        else:
            rootnode = self.ls[0]  # 取出第一个节点作为当前的根节点（不一定是整个树的根节点，而是双亲节点）
            if rootnode.left is None:  # 当前根节点的左子树是空树
                rootnode.left = node  # 将节点值赋给当前根节点的左子树（此处的node已经是实例化的节点）
                self.ls.append(rootnode.left)  # 将节点值存放在列表中作为双亲节点下次被取出来
            elif rootnode.right is None:  # 当前根节点的右子树是空树
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)  # 将列表中的第一个元素弹出，表示已经完成了左右子树的添加
    
    # 非递归遍历-前序遍历
    def preordertraversalnon(self):
        result = []  # 存放中序遍历结果
        treenodes = [self.root]  # 存放顺序-右子树-根节点-左子树

        if self.root is None:
            return

        while treenodes:
            subtree = treenodes.pop()  # 引用类生成的树
            if subtree.right is None and subtree.left is None:
                result.append(subtree.data)
            else:
                if subtree is not None:
                    if subtree.right is not None:
                        treenodes.append(subtree.right)  # 添加当前树的右节点
                    if subtree.left is not None:
                        treenodes.append(subtree.left)  # 添加当前树的左节点
                    if subtree.data is not None:
                        rootnode = TreeNode(subtree.data)  # keypoint: 将当前根节点单独生成一棵单节点树
                        treenodes.append(rootnode)  # 添加当前树的根节点

        return result

    # 非递归遍历-中序遍历
    def inordertraversalnon(self):
        result = []  # 存放中序遍历结果
        treenodes = [self.root]  # 存放顺序-右子树-根节点-左子树

        if self.root is None:
            return
        
        while treenodes:
            subtree = treenodes.pop()  # 引用类生成的树
            if subtree.right is None and subtree.left is None:
                result.append(subtree.data)
            else:
                if subtree is not None:
                    if subtree.right is not None:
                        treenodes.append(subtree.right)  # 添加当前树的右节点
                    if subtree.data is not None:
                        rootnode = TreeNode(subtree.data)  # keypoint: 将当前根节点单独生成一棵单节点树
                        treenodes.append(rootnode)  # 添加当前树的根节点
                    if subtree.left is not None:
                        treenodes.append(subtree.left)  # 添加当前树的左节点
                
        return result

    # 非递归遍历-中序遍历
    def postordertraversalnon(self):
        result = []  # 存放中序遍历结果
        treenodes = [self.root]  # 存放顺序-右子树-根节点-左子树
    
        if self.root is None:
            return
    
        while treenodes:
            subtree = treenodes.pop()  # 引用类生成的树
            if subtree.right is None and subtree.left is None:
                result.append(subtree.data)
            else:
                if subtree is not None:
                    if subtree.data is not None:
                        rootnode = TreeNode(subtree.data)  # keypoint: 将当前根节点单独生成一棵单节点树
                        treenodes.append(rootnode)  # 添加当前树的根节点
                    if subtree.right is not None:
                        treenodes.append(subtree.right)  # 添加当前树的右节点
                    if subtree.left is not None:
                        treenodes.append(subtree.left)  # 添加当前树的左节点
    
        return result


if __name__ == '__main__':
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    btree = BinaryTree()
    for i in range(0, 10):
        btree.insertnode(i)

    # 2：调用遍历方法

    print('>> 前序遍历-非递归方法:')
    print(btree.preordertraversalnon())
    print('>> 中序遍历-非递归方法:')
    print(btree.inordertraversalnon())
    print('>> 后序遍历-非递归方法:')
    print(btree.postordertraversalnon())
