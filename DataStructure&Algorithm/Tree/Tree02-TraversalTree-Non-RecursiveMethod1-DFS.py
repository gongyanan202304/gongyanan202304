# 树的遍历的简介
# 树的遍历的实现方法有2大类：递归遍历与非递归遍历
# 树的遍历方式有深度遍历和层次遍历
# 深度遍历：前序遍历、中序遍历、后序遍历
# 层次遍历：广度遍历

# 脚本说明：
# 1：在使用树的遍历的时候, 先需要进行树的创建，在本脚本中使用嵌套列表的形式来存储树的结构
# 2：设计树的遍历的时候，需要设计前序遍历、中序遍历、后序遍历三种深度优先的遍历DFS
# 3：本脚本设计的是非递归方法的深度优先遍历DFS

# 在遍历树的节点时，采用非递归的方法。如何实现非递归的方法？
# 以对前序遍历为例：
#   根据前序遍历的访问顺序，先访问根节点，然后访问根节点的左右孩子节点。即对每一个节点，其可看作是根节点，因此可以直接访问，
#   访问完成以后，如果该节点的左节点不为空，就按照相同的方法访问它的左子树，最后访问它的右子树。
#   对于任一节点，访问规则：
#   s1：访问节点P，并将节点P入栈
#   s2：判断节点P的左孩子是否为空，
#       若为空，则取栈顶节点并进行出栈操作，并将栈顶节点的右孩子节点置为当前节点P，循环至s1;
#       若不空，则将节点P入栈，并且把P的左孩子节点置为当前节点P,循环至s1;
#   s3：直到P为NUll并且栈为空，则遍历结束。

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
        self.leafnodes = []  # 存放叶子节点
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
                rootnode.left = node  # 将节点值赋给当前根节点的左子树
                self.ls.append(rootnode.left)  # 将节点值存放在列表中作为双亲节点下次被取出来
            elif rootnode.right is None:  # 当前根节点的右子树是空树
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)  # 将列表中的第一个元素弹出，表示已经完成了左右子树的添加

    # 前序遍历-递归方法
    def preordertraverse(self, root):
        """前序遍历"""
        if root is None:
            return
        print(root.data, end=" ")
        self.preordertraverse(root.left)
        self.preordertraverse(root.right)

    # 前序遍历-非递归方法
    @staticmethod
    def preordertraversestack(root):
        if root is None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                result.append(node.data)  # 当前根节点的数值
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result

    # 中序遍历-非递归方法
    @staticmethod
    def inordertraversestack(root):
        if root is None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                # 树的左子树一直遍历到叶子节点，栈中全部是左子树
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right

        return result

    # 后序遍历-非递归方法
    @staticmethod
    def postordertraversestack(root):
        if root is None:
            return
        seq = []
        result = []
        stack = []
        node = root
        while node or stack:
            while node:
                seq.append(node.data)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        while seq:
            result.append(seq.pop())
        return result


# 主函数


if __name__ == '__main__':
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    btree = BinaryTree()
    for i in range(0, 10):
        btree.insertnode(i)

    # 2：调用遍历方法
    print('>> 前序遍历-递归方法:')
    print(btree.preordertraverse(btree.root))
    print('>> 前序遍历-非递归方法:')
    print(btree.preordertraversestack(btree.root))
    print('>> 中序遍历-非递归方法:')
    print(btree.inordertraversestack(btree.root))
    print('>> 后序遍历-非递归方法:')
    print(btree.postordertraversestack(btree.root))
