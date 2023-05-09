# 二叉树的构造方法-节点链表表示法
"""
    在这个脚本中主要使用的是队列来插入数据节点，
    并且还对当前根节点的左右子树的存在，进行了判定。
    该脚本还是和脚本<Tree01-BuildingTree-NodeLinkedTable-1.py>的解题思路大体上是一致的，稍微有点区别。
"""

# 节点链表表示法
print('>>> 节点链表表示法')


class BinTree:
    """创建二叉树"""
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def insertnodes(self, data):
        node = BinTree(data)  # 二叉树节点化
        if self.root is None:
            self.root = node
            return

        queue = [self]  # 存储当前节点的对列
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

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
                result.append(node.root)  # 当前根节点的数值
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
            result.append(node.root)
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
                seq.append(node.root)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        while seq:
            result.append(seq.pop())
        return result

    # 层次遍历（广度优先遍历）
    @staticmethod
    def breadthfirsttraversal(root):
        if root is None:
            return
        sequence = []  # 声明一个先进先出的队列存放子树
        result = []  # 声明一个列表存放节点数值
        node = root
        sequence.append(node)  # 现将整个树假如队列中
        while sequence:  # 当前队列不为空，表示队列中还有需要遍历的子树
            node = sequence.pop(0)  # 当前队列中的子树出队列
            result.append(node.root)  # 将当前子树中的根节点的数值存放在reslut列表中
            if node.left is not None:  # 当前子树的左子树存在，则先加入到队列中
                sequence.append(node.left)
            if node.right is not None:  # 当前子树的右子树存在，则后加入到队列中
                sequence.append(node.right)
        return result


# 主函数

if __name__ == '__main__':
    tree = BinTree(0)
    for i in range(1, 4):
        tree.insertnodes(i)
    print('>> 非递归-前序遍历：')
    print(tree.preordertraversestack(tree))
    print('>> 非递归-中序遍历：')
    print(tree.inordertraversestack(tree))
    print('>> 非递归-后序遍历：')
    print(tree.postordertraversestack(tree))
    print('>> 广度优先遍历：')
    print(tree.breadthfirsttraversal(tree))
