# 满二叉树
# 满二叉树是在完全二叉树的基础上形成的
# 满二叉树的特点是每一层的节点数目达到最大值power(2,k-1)
# 判定二叉树是否是满二叉树：二叉子树的高度一样，二叉左子树和右子树的节点存在情况一样（存在或者不存在）

# 设计满二叉树

class TreeNode:
    """创建树节点"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class FullBinaryTree:
    """创建满二叉树"""
    def __init__(self):
        self.root = None
        self.nodepos = []  # 存放节点的位置
        
    # 创建树-插入节点
    def insertnodes(self, node):
        if node is None:
            return
        node = TreeNode(node)  # 节点的树实例化
        if self.root is None:
            self.root = node
            self.nodepos.append(self.root)
        else:
            rootnode = self.nodepos[0]  # 取出列表中的第一个元素
            if rootnode.left is None:
                rootnode.left = node
                self.nodepos.append(rootnode.left)
            elif rootnode.right is None:
                rootnode.right = node
                self.nodepos.append(rootnode.right)
                self.nodepos.pop(0)  # 删除列表中的第一位元素，表明已经完成了左右树的插入
    
    # 递归法-返回树的高度
    def getheightoftree(self, tree):
        if tree is None:
            return 0
        elif tree.left is None and tree.right is None:
            return 1
        elif tree.left is None and tree.right is not None:
            return 1 + self.getheightoftree(tree.right)
        elif tree.left is not None and tree.right is None:
            return 1 + self.getheightoftree(tree.left)
        else:
            return max(self.getheightoftree(tree.left), self.getheightoftree(tree.right)) + 1
         
    # 判定子树高度是否一致
    def isheightequal(self, tree):
        if tree is None:
            return 0
        elif tree.left is None and tree.right is None:
            return 1
        elif tree.left is None and tree.right is not None:
            return 1 + self.getheightoftree(tree.right)
        elif tree.left is not None and tree.right is None:
            return 1 + self.getheightoftree(tree.left)
        else:
            if self.getheightoftree(tree.left) == self.getheightoftree(tree.right):
                return True
            else:
                return False
        
    # 判定二叉树是否满二叉树
    def isfullbinarytree(self, tree):
        """ param: tree 是被遍历的树
            二叉树是否是满二叉树的要求：
            （1）左右子树的高度一样
            （2）左右子树的节点均存在或均不存在
        """
        
        if self.root is None:
            return
        treequeue = [tree]  # 存储子树的队列
        
        while True:
            subtree = treequeue.pop(0)
            if self.isheightequal(subtree):
                if subtree.left is None and subtree.right is None:
                    # 左子树空，右子树空，返回True
                    return True
                elif subtree.left is not None and subtree.right is not None:
                    # 左子树bu空，右子树bu空，子树的左子树和右子树入队列
                    treequeue.append(subtree.left)
                    treequeue.append(subtree.right)
                elif subtree.left is None and subtree.right is not None:
                    return "False: 左空-右不空"
                elif subtree.left is not None and subtree.right is None:
                    return "False: 左不空-右空"
            else:
                return 'False: 左右子树的高度不一样'
  
# 主函数


if __name__ == '__main__':
    
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    btree = FullBinaryTree()
    # 节点总数power(2,k)-1
    for i in range(1, 32):
        btree.insertnodes(i)
        
    # 2：调用树的方法
    print('>> 树的高度：')
    print(btree.getheightoftree(btree.root))
    
    print('>> 子树的高度是否一样：')
    print(btree.isheightequal(btree.root))
    
    print('>> 判定二叉树是否为满二叉树：')
    print(btree.isfullbinarytree(btree.root))
    