# 二叉树的构建方法-嵌套列表表示法

# 1.树的表示方法主要有2种：嵌套列表表示法、节点链表表示法
# 2.树的性质有：节点总数=度0节点数+度1节点数+度2节点数+度3节点数；节点总数=度1节点数+2*度2节点数+1
# 3.树的嵌套列表表示法：主要是列表中有3个元素[根，左孩子，右孩子]
# 4.仅有完全二叉树是使用顺序结构（数组/列表）存储数据，一般情况下是使用链表来存储数据结构。
# 5.增加嵌套列表里面的元素就可以实现多叉树的构建

# 方法1-嵌套列表表示方法-采用类方法的形式
print('>>> 嵌套列表表示方法-采用类方法的形式1')


class Solution:  # 此处的类没有添加object 参数,也没有()

    @staticmethod
    def binarytree(root):
        return [root, [], []]

    @staticmethod
    def insertleft(tree, newnode):
        """向树中当前的根节点插入左节点"""
        leftnode = tree.pop(1)  # 当前根节点的左孩子节点
        if len(leftnode) > 1:  # 当前根节点存在左孩子节点
            tree.insert(1, [leftnode, newnode, []])
        else:
            tree.insert(1, [newnode, [], []])
        return tree

    @staticmethod
    def insertright(tree, newnode):
        """向树中当前的根节点插入右节点"""
        rightnode = tree.pop(2)
        if len(rightnode) > 1:  # 当前根节点存在右孩子节点
            tree.insert(2, [rightnode, [], newnode])
        else:
            tree.insert(2, [newnode, [], []])
            return tree

    @staticmethod
    def getrootval(tree):
        return tree[0]

    @staticmethod
    def setrootval(tree, newval):
        tree[0] = newval

    @staticmethod
    def getleftchild(tree):
        return tree[1]

    @staticmethod
    def getrightchild(tree):
        return tree[2]


# 数据测试
if __name__ == '__main__':
    s = Solution()
    btree = s.binarytree('a')
    s.insertleft(btree, 'b')
    s.insertright(btree, 'c')
    print('tree-1:', btree)

    s.insertleft(s.getleftchild(btree), 'd')
    s.insertright(s.getleftchild(btree), 'e')
    print('tree-2:', btree)
 
    s.insertleft(s.getrightchild(btree), 'f')
    s.insertright(s.getrightchild(btree), 'g')
    print('tree-3:', btree)

# 注意问题
# Q1： Method 'binarytree' may be 'static'
# A1：这是因为这个方法本可以写成静态方法，但我们把它写成类方法了（就是没有必要写成类方法，因为在方法中并未使用这个类self）
# 具体的解决办法是删除类方法中的self, 并且在方法的上面添加"@staticmethod" 来表示声明了一个静态方法
# (简单的来说就是一个简单的函数 function ，不是放在类class中的方法)

# 思考1：
# 如果本题要修改为静态方法的形式的话，
# 需要把class Solution 以及静态方法声明删除，
# 并把def 的方法定格书写，即可以实现。
# 如下所示：


# 方法2-嵌套列表表示方法-采用静态方法的形式
print('>>> 嵌套列表表示方法-采用静态方法的形式')


def binarytree(root):
    return [root, [], []]


def insertleft(tree, newnode):
    """向树中当前的根节点插入左节点"""
    leftnode = tree.pop(1)  # 当前根节点的左孩子节点
    if len(leftnode) > 1:  # 当前根节点存在左孩子节点
        tree.insert(1, [leftnode, newnode, []])
    else:
        tree.insert(1, [newnode, [], []])
    return tree


def insertright(tree, newnode):
    """向树中当前的根节点插入右节点"""
    rightnode = tree.pop(2)
    if len(rightnode) > 1:  # 当前根节点存在右孩子节点
        tree.insert(2, [rightnode, [], newnode])
    else:
        tree.insert(2, [newnode, [], []])
        return tree


def getrootval(tree):
    return tree[0]


def setrootval(tree, newval):
    tree[0] = newval


def getleftchild(tree):
    return tree[1]


def getrightchild(tree):
    return tree[2]


# 数据测试
btree = binarytree('a')
insertleft(btree, 'b')
insertright(btree, 'c')
print('tree-1:', btree)

insertleft(getleftchild(btree), 'd')
insertright(getleftchild(btree), 'e')
print('tree-2:', btree)

insertleft(getrightchild(btree), 'f')
insertright(getrightchild(btree), 'g')
print('tree-3:', btree)

# 思考2：
# 再思考一个问题：如果我既想使用类方法，又想使用self，
# 代码如何设计，如下所示：
print('>>> 嵌套列表表示方法-采用类方法的形式2')


class CreatingBinaryTree:

    def __init__(self, root):  # 初始化变量
        self.root = root
        self.left = None
        self.right = None

    def binarytree(self):  # 此处没有参数输入
        return [self.root, [], []]

    def insertleft(self, tree, newnode):
        """向树中当前的根节点插入左节点"""
        self.left = tree.pop(1)  # 当前根节点的左孩子节点
        if len(self.left) > 1:  # 当前根节点存在左孩子节点
            tree.insert(1, [self.left, newnode, []])
        else:
            tree.insert(1, [newnode, [], []])
        return tree

    def insertright(self, tree, newnode):
        """向树中当前的根节点插入右节点"""
        self.right = tree.pop(2)
        if len(self.right) > 1:  # 当前根节点存在右孩子节点
            tree.insert(2, [self.right, [], newnode])
        else:
            tree.insert(2, [newnode, [], []])
            return tree

    def getrootval(self):
        return self.root[0]

    def setrootval(self, newval):
        self.root[0] = newval

    def getleftchild(self):
        return self.root[1]

    def getrightchild(self):
        return self.root[2]


# 数据测试
if __name__ == '__main__':

    t = CreatingBinaryTree('a')  # 实例化创建二叉树
    btree = t.binarytree()
    t.insertleft(btree, 'b')
    t.insertright(btree, 'c')
    print('tree-1:', btree)

    insertleft(getleftchild(btree), 'd')
    insertright(getleftchild(btree), 'e')
    print('tree-2:', btree)

    insertleft(getrightchild(btree), 'f')
    insertright(getrightchild(btree), 'g')
    print('tree-3:', btree)

    print('RootNodeOfBinTree:', getrootval(btree))  # 输出树的根节点的数值

# 思考3：
# 假如我们需要设计一个类，包含方法的功能：
# (1)取出某个指定节点的左子树、右子树，
# (2)修改某个指定节点的数值，
# (3)删除某个指定节点，
# (4)为某个指定的节点添加一个左节点或右节点
# 以上内容在《Tree03-TreeAndTreeMethod.py》中可以参考。
