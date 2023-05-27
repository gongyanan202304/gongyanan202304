# 二叉树的构造方法-节点链表表示法

# 1.树的表示方法主要有2种：嵌套列表表示法、节点链表方法
# 2.树的性质有：节点总数=度0节点数+度1节点数+度2节点数+度3节点数；节点总数=度1节点数+2*度2节点数+1
# 3.树的嵌套列表表示法：主要是列表中有3个元素[根，左孩子，右孩子]


# 方法2-节点与引用类方法
print('>>> 方法2-节点与引用类方法')


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

    def get_right_child(self):
        """返回右子树"""
        return self.right

    def get_left_child(self):
        """返回左子树"""
        return self.left


    def get_root_val(self):
        """返回根节点的数值"""
        return self.data

    def set_root_val(self, new_val):
        """修改根节点的数值"""
        self.data = new_val


class BinaryTree:
    """创建二叉树"""
    def __init__(self):
        self.root = None  # 初始化根节点
        self.ls = []  # 存储根节点(双亲节点)的位置值的队列

    def insertnode(self, data):
        """
            插入左子树： data 为左子树的根节点
            如果原来的树不存在左子树，那么 data 为左子树的根节点
            如果原来的树存在左子树，那么原来的左子树变为以 data 为根节点的左子树

            插入右子树：data 为右子树的根节点
            如果原来的树不存在左子树，那么 data 为左子树的根节点
            如果原来的树存在左子树，那么原来的右子树变为以 data 为根节点的右子树
        """

        node = TreeNode(data)
        if self.root is None:  # 判定树的根节点为空
            self.root = node  # 将当前
            self.ls.append(node)
        else:
            rootnode = self.ls[0]  # 取出第一个节点作为当前的根节点（不一定是整个树的根节点，而是双亲节点）
            if rootnode.left is None:  # 当前根节点的左子树是空树
                rootnode.left = node  # 将节点值赋给当前根节点的左子树
                self.ls.append(node)  # 将节点值存放在列表中作为双亲节点下次被取出来
            elif rootnode.right is None:  # 当前根节点的右子树是空树
                rootnode.right = node
                self.ls.append(node)
                self.ls.pop(0)  # 将列表中的第一个元素弹出，表示已经完成了左右子树的添加


# 主函数

if __name__ == '__main__':
    t = TreeNode('x')
    t.right = TreeNode('A')
    t.left = TreeNode('B')
    # tree = BinaryTree()
    # for i in range(1, 12):
    #     tree.insertnode(i)
    print('获取根节点:', t.get_root_val())
    print('返回左子树:', t.get_left_child())
    print('返回右子树:', t.get_right_child())
    print('重新设置根节点:', t.set_root_val('w'))
    print('返回新的根节点:', t.get_root_val())
    print('返回树结构:', t)

# 思考如何返回一个树的左子树、右子树？
