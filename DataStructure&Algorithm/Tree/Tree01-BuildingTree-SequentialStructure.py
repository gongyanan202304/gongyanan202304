# 使用顺序结构来构建完全二叉树
# CompleteBinaryTree
# 采用节点链表的方式来构建完全二叉树
# 完全二叉树的特点:
# 1.除了最后一层节点以外，其它的层的节点数目达到最大值
# 2.在使用顺序结构来存储数据时，树的节点位置与顺序结构中的元素的位置是一一对应的
# 3.对于一般树而言，需要转化为完全二叉树以后，才可以使用顺序结构来存储节点数据，
#   具体的方法是将空节点用虚拟节点来表示。


# 采用节点链表设计方法-构建完全二叉树


class TreeNode:
    def __init__(self, data):
        self.data = data  # 存储节点的数据域
        self.left = None  # 当前节点的左子树
        self.right = None  # 当前节点的右子树
        self.treenodes = []  # 存储树的结构形式

    def completebinarytree(self, nodelist):
        """
            构建完全二叉树
            参数：nodelist 是存放给定节点的列表
            列表中位置为k的元素是表示根节点，2k + 1 表示左节点， 2k + 2 表示右节点，即形式是[k,2k+1,2k+2]的递归形式
        """
        if len(nodelist) == 0:
            return

        for k in range(0, len(nodelist)):
            """使用python的三目运算"""
            # 当前根节点的数据
            self.data = nodelist[k]

            # 当前根节点的左子节点
            self.left = nodelist[2 * k + 1] if 2 * k + 1 <= len(nodelist) - 1 else ''

            # 当前根节点的右子节点
            self.right = nodelist[2 * k + 2] if 2 * k + 2 <= len(nodelist)-1 else ''

            # 将节点形式存储为树的节点链表的形式
            self.treenodes.append([self.data, self.left, self.right])

        return self.treenodes


if __name__ == "__main__":
    treenode = TreeNode('-1')  # 节点实例化
    nodelst = [0, 1, 2, 3, 4, 5, 6, 7]
    # 采用实例调用实例方法输出树的形式
    print(treenode.completebinarytree(nodelst))


# 思考1：
# 怎么使用递归方法来实现完全二叉树的构建

# 设计1-采用递归方法实现完全二叉树


class TreeNodeItem:
    def __init__(self, item):
        self.item = item  # 树节点的数据域
        self.left = None  # 树节点的左子树
        self.right = None  # 树节点的右子树


def completebinarytree(nodeslist, curindex, curnode=None):
    """采用递归方法来设计完全二叉树的创建"""
    if len(nodeslist) == 0:
        return
    if curindex < len(nodeslist):
        if nodeslist[curindex] == 'None':
            return None

        curnode = TreeNodeItem(nodeslist[curindex])
        curnode.left = completebinarytree(nodeslist, 2*curindex + 1, curnode.left)
        curnode.right = completebinarytree(nodeslist, 2 * curindex + 2, curnode.right)
        return curnode


def preordertraver(tree):
    # 设计一个前序遍历的函数来实现树的遍历
    if tree is None:
        return
    print(tree.item, end=' ')
    preordertraver(tree.left)
    preordertraver(tree.right)


if __name__ == "__main__":
    rootnode = TreeNodeItem('-1')
    treenodeslst = [0, 1, 2, 3, 4, 5, 6, 7]
    currootnode = completebinarytree(treenodeslst, 0, rootnode)
    preordertraver(currootnode)
    print('')


# 思考2：
# 怎么使用静态方法来实现完全二叉树的构建
# 设计2-采用静态类方法实现完全二叉树


def compbintree(nodelist):
    """
       采用静态方法实现完全二叉树
       参数：nodelist 输入的节点列表

    """
    treenodes = []  # 存放树的节点 [当前根节点，当前根节点的左节点，当前根节点的右节点]
    nodenumb = len(nodelist)  # 计算节点列表元素的个数

    if nodenumb == 0:
        return
    for i in range(0, nodenumb):
        # 当前根节点
        curroot = nodelist[i]
        # 当前根节点的左节点-用python的三目运算方式计算
        curleft = nodelist[2 * i + 1] if 2*i + 1 <= nodenumb - 1 else ''
        # 当前根节点的右节点-用python的三目运算方式计算
        curright = nodelist[2 * i + 2] if 2*i + 2 <= nodenumb - 1 else ''

        treenodes.append([curroot, curleft, curright])

    # 返回结果
    return treenodes


# 数据测试
if __name__ == "__main__":
    nodeslst = [0, 1, 2, 3, 4, 5, 6, 7]
    print(compbintree(nodeslst))
