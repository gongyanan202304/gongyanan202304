# 平衡二叉树
# 判定一棵树是平衡二叉树

# 设计代码
# 不需要对二叉树进行节点的插入操作，数据是一个线性存储结构


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def getheightoftree(self, tree):
        if tree is None:
            return 0
        if tree.left is None and tree.right is None:
            return 1
        else:
            return 1 + max(self.getheightoftree(tree.left), self.getheightoftree(tree.right))
    
    def isbanlancedtree(self, tree):
        
        if tree is None:
            return True
        
        return 0 if abs(self.getheightoftree(tree.left) - self.getheightoftree(tree.right)) <= 1 \
                    and self.isbanlancedtree(tree.left) and self.isbanlancedtree(tree.right) else 1
        

# 主函数

if __name__ == "__main__":
    node = TreeNode(0)  # 根节点实例化
    node.left = TreeNode(1)  # 左子树节点
    node.right = TreeNode(2)  # 右子树节点
    treeL1 = node.left
    treeL1.left = TreeNode(3)
    treeL1.right = TreeNode(4)
    treeR1 = node.right
    treeR1.left = TreeNode(5)
    
    print('>> 树的高度：')
    print(node.getheightoftree(treeL1))
    
    print('>> 树是否是平衡二叉树：')
    print(node.isbanlancedtree(node.left))
    
        