# 树的遍历-深度优先遍历（递归方法）
# 树的遍历的实现方法有2大类：递归遍历与非递归遍历
# 树的遍历方式有深度遍历和层次遍历
# 深度遍历有：前序遍历、中序遍历、后序遍历
# 而层次遍历仅有层次遍历

# 脚本说明：
# 1：在使用树的遍历的时候, 先需要进行树的创建，在本脚本中使用嵌套列表的形式来存储树的结构
# 2：设计树的遍历的时候，需要设计前序遍历、中序遍历、后序遍历三种深度优先的遍历DFS
# 3：本脚本设计的是采用递归方法的深度优先遍历DFS


# 嵌套列表表示方法-采用静态方法的形式
print('>>> 嵌套列表表示方法-采用静态方法的形式')


def binarytree(root):
    return [root, [], []]


def insertleft(tree, newnode):
    """向树中当前的根节点插入左节点"""
    left_node = tree.pop(1)  # 当前根节点的左孩子节点
    if len(left_node) > 1:  # 当前根节点存在左孩子节点
        tree.insert(1, [left_node, newnode, []])
    else:
        tree.insert(1, [newnode, [], []])
    return tree


def insertright(tree, newnode):
    """向树中当前的根节点插入右节点"""
    right_node = tree.pop(2)
    if len(right_node) > 1:  # 当前根节点存在右孩子节点
        tree.insert(2, [right_node, [], newnode])
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


# 递归方法-树的前序遍历-根-左子树-右子树
def preordertraver(tree):
    if tree:
        print(getrootval(tree), end=' ')
        preordertraver(getleftchild(tree))
        preordertraver(getrightchild(tree))


# 递归方法-树的中序遍历左子树-根-右子树
def inordertraver(tree):
    if tree:
        inordertraver(getleftchild(tree))
        print(getrootval(tree), end=' ')
        inordertraver(getrightchild(tree))


# 递归方法-树的后序遍历左子树-根-右子树
def posordertraver(tree):
    if tree:
        posordertraver(getleftchild(tree))
        posordertraver(getrightchild(tree))
        print(getrootval(tree), end=' ')


if __name__ == "__main__":
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

    print('>>> 树的前序遍历:')
    preordertraver(btree)
    print('')
    print('>>> 树的中序遍历:')
    inordertraver(btree)
    print('')
    print('>>> 树的后序遍历:')
    posordertraver(btree)

# 构建树的方法-节点链表表示法
print('')
print('>>> 构建树的方法-节点链表表示法')


class TreeNode:
    """定义树的节点结构"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """创建二叉树以及二叉树的遍历"""

    """定义树的节点"""
    def __init__(self, root):
        self.root = root  # 初始化根节点
        self.leftchild = None
        self.rightchild = None
        self.pretraverlst = []  # 在树的前序遍历preordertraversal中使用
        self.intraverlst = []  # 在树的中序遍历中使用
        self.postraverlst = []  # 在树的后序遍历中使用
        self.pretraverlst1 = []  # 在树的前序遍历preordertraversal1中使用

    """树的前序遍历"""
    def preordertraversal1(self, tree):
        """
        在大多数的关于树的博客中，代码中实现遍历的形式是用print函数来输出当前的根节点
        而在本程序设计中，是将每一次遍历的根节点放在了一个列表中。并且这个列表是在类的初始化阶段已提前设计完成。
        在后续的遍历中，仅仅是往这个列表中添加根节点，以作为列表元素。
        """
        if tree.root is None:
            return
        # if tree.root:
        #     print(tree.root, end=' ')
        # if tree.leftchild:
        #     self.preordertraversal1(tree.leftchild)
        # if tree.rightchild:
        #     self.preordertraversal1(tree.rightchild)

        if tree.root:
            self.pretraverlst1.append(tree.root)
        if tree.leftchild:
            self.preordertraversal1(tree.leftchild)
        if tree.rightchild:
            self.preordertraversal1(tree.rightchild)
        return self.pretraverlst1

# 树的前序遍历2：
# 树的前序遍历是使用了双方法的形式，pretraver负责递归处理树的遍历，preordertraversal负责返回处理的结果
# 在方法调用的时候直接调用preordertraversal这个方法就可以了。
# 树的前序遍历、中序遍历以及后序遍历采用双方法的形式来实现。
    
    def pretraver(self, tree):
        if tree is None:
            return
        self.pretraverlst.append(tree.root)
        self.pretraver(tree.leftchild)
        self.pretraver(tree.rightchild)

    def preordertraversal(self, tree):
        self.pretraver(tree)
        return self.pretraverlst

    # 中序遍历
    def intraver(self, tree):
        if tree is None:
            return
        self.intraver(tree.leftchild)
        self.intraverlst.append(tree.root)
        self.intraver(tree.rightchild)

    def inordertraversal(self, tree):
        self.intraver(tree)
        return self.intraverlst

    # 后序遍历
    def postraver(self, tree):
        if tree is None:
            return
        self.postraver(tree.leftchild)
        self.postraver(tree.rightchild)
        self.postraverlst.append(tree.root)

    def posordertraversal(self, tree):
        self.postraver(tree)
        return self.postraverlst


# 树的遍历测试过程
if __name__ == "__main__":
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    leftnode = BinaryTree('1')
    leftnode.leftchild = BinaryTree('3')
    leftnode.rightchild = BinaryTree('4')

    rightnode = BinaryTree('2')
    rightnode.leftchild = BinaryTree('5')
    rightnode.rightchild = BinaryTree('6')

    bintree = BinaryTree('0')
    bintree.leftchild = leftnode
    bintree.rightchild = rightnode

    # 2：输出遍历节点的顺序
    # 前序遍历输出
    print('>> 前序遍历输出1:')
    print(bintree.preordertraversal1(bintree))
    # 前序遍历输出2
    print('前序遍历输出:', ' '.join(bintree.preordertraversal(bintree)))  # 采用字符串的形式输出列表中的元素
    # 中序遍历输出
    print('中序遍历输出:', ' '.join(bintree.inordertraversal(bintree)))  # 采用字符串的形式输出列表中的元素
    # 后序遍历输出
    print('后序遍历输出:', ' '.join(bintree.posordertraversal(bintree)))  # 采用字符串的形式输出列表中的元素
