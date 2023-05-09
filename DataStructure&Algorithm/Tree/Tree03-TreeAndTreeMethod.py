# 树的结构与方法设计脚本（综合脚本）
# 脚本说明：
#     1：树的结构是采用节点链表方法来实现
#     2：树的属性方法有：叶子节点的个数统计、叶子节点、树的高度、返回左兄弟、返回右兄弟、补齐空左右节点
#     3：树的遍历方法有：深度优先遍历（前序遍历、中序遍历、后序遍历）、层次遍历（广度优先遍历）
# 设计方法：
#     1：在使用树的遍历的时候, 先需要进行树的创建，在本脚本中使用节点链表的形式来存储树的结构
#     2：树的遍历1：前序遍历、中序遍历、后序遍历三种深度优先的遍历DFS(使用了递归方法与非递归方法)
#     3：树的遍历2：广度优先遍历（层次遍历）


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
        self.preres = []  # 存放前序遍历-递归方法结果
        self.inres = []  # 存放中序遍历-递归方法结果
        self.postres = []  # 存放后序遍历-递归方法结果

        self.preresnon = []  # 存放非递归-前序遍历结果的列表
        self.inresnon = []  # 存放非递归-中序遍历结果的列表
        self.postresnon = []  # 存放非递归-后序遍历结果的列表
        self.breadthresult = []  # 存放广度遍历结果的列表

        self.depthfirsttraversalpath = []  # 存放采用深度优先方法遍历节点的路径
        self.breadthfirsttraversalpath = []  # 存放采用广度优先方法遍历节点的路径

        self.ls = []  # 存储根节点(双亲节点)的位置值的队列

        self.parentnode = None  # 指定节点的双亲节点
        self.rightbronode = None  # 右兄弟节点
        self.leftbronode = None  # 左兄弟节点
        self.insertedres = ''  # 插入节点后的结果列表

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
                
    # 返回树的根节点
    def getrootval(self, tree):
        if tree is None:
            return
        # 两种输出方式是等效的
        # return tree.data
        return self.root.data
    
    # 修改树的根节点的数值
    def setrootnewval(self, newval):
        # 不论树的根节点是存在数据还是空数据,直接修改根节点数据即可
        self.root.data = newval
        return self.root.data
        
    # 返回树的左子树节点
    def getleftchildnode(self, tree):
        if tree is None:
            return
        if tree.left is None:
            return
        else:
            # 两种输出方式是等效的
            return self.root.left.data
            # return tree.left.data
    
    # 返回树的右子树节点
    def getrightchildnode(self, tree):
        if tree is None:
            return
        if tree.right is None:
            return
        else:
            # return tree.right.data
            return self.root.right.data

    # 返回指定节点的双亲节点
    def getparentnode(self, tree, node):
        """返回一个给定node双亲节点"""
        if tree is None:
            return
        if node is None:
            return
        # 声明队列存储当前子树
        subtreequeue = [tree]
        # 将左子/树右子树循环加入到队列中
        while subtreequeue:
            subtree = subtreequeue.pop(0)  # 从队列中取出第一位元素即为一棵子树
    
            if subtree.data == node:  # 当前子树的根节点的数据等于指定节点的数据
                self.parentnode = subtree.data
                return self.parentnode
    
            if subtree.left is not None:  # 当前子树中的左子树不为空
                if subtree.left.data == node:  # 左子树的数据等于指定的节点
                    self.parentnode = subtree.data  # 子树的数据（子树的根节点的数据）
                    return self.parentnode
                else:
                    subtreequeue.append(subtree.left)  # 将子树的左子树加入到队列中
    
            if subtree.right is not None:  # 当前子树中的右子树不为空
                if subtree.right.data == node:  # 右子树的数据等于指定的节点
                    self.parentnode = subtree.data  # 子树的数据（子树的根节点的数据）
                    return self.parentnode
                else:
                    subtreequeue.append(subtree.right)  # 将子树的右子树加入到队列中

        if self.parentnode is None:  # 没有找到指定节点的双亲节点
            return

    # 返回指定节点的右兄弟
    def getrightbrother(self, tree, node):
        if tree is None:
            return
        if node is None:
            return

        # 存放子树的队列
        subtreequeue = [tree]
        while subtreequeue:
            subtree = subtreequeue.pop(0)  # 取出队列中的第一个元素
    
            if subtree.data == node:
                return
    
            if subtree.left is not None:
                if subtree.left.data == node:
                    if subtree.right is not None:
                        self.rightbronode = subtree.right.data
                        return self.rightbronode
                    else:
                        return  # 当前子树存在左子树节点，而不存在右子树节点
                else:
                    subtreequeue.append(subtree.left)  # 将子树的左子树加入队列中
    
            if subtree.right is not None:
                if subtree.right.data == node:
                    return  # 当前子树的右节点没有已经是指定的节点
                else:
                    subtreequeue.append(subtree.right)

        if self.rightbronode is None:
            return

    # 返回指定节点的左兄弟
    def getleftbrother(self, tree, node):
        if tree is None:
            return
        if node is None:
            return
        # 子树队列
        subtreequeue = [tree]

        while subtreequeue:
            subtree = subtreequeue.pop(0)
    
            if subtree.data == node:
                return
    
            if subtree.left is not None:
                if subtree.left.data == node:
                    return
                else:
                    subtreequeue.append(subtree.left)
    
            if subtree.right is not None:
                if subtree.right.data == node:
                    if subtree.left is not None:
                        self.leftbronode = subtree.left.data
                        return self.leftbronode
                    else:
                        return
                else:
                    subtreequeue.append(subtree.right)

        if self.leftbronode is None:
            return

    # 叶子节点个数的统计
    def getleafnodesamount(self, nodes):
        """在main函数中调用方法leafnodescount时需要加上.root,这是BinaryTree的属性参数"""
        if nodes is None:
            return 0
        elif (nodes.left is None) and (nodes.right is None):
            return 1
        else:
            return self.getleafnodesamount(nodes.left) + self.getleafnodesamount(nodes.right)

    # 判定当前节点是否是叶子节点,并输出叶子节点
    def getleafnodes(self, node):
        # 使用递归方法来判定当前节点是否是叶子节点
        if node is None:
            return None
        elif (node.right is None) and (node.left is None):
            self.leafnodes.append(node.data)  # 节点的数值写入列表
        elif node.left is None and node.right is not None:
            self.getleafnodes(node.right)
        elif node.left is not None and node.right is None:
            self.getleafnodes(node.left)
        else:
            self.getleafnodes(node.left)
            self.getleafnodes(node.right)

        return self.leafnodes

    # 树的高度
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

    # 给指定节点补上左节点或者右节点
    def insertmissingnode(self, tree, parent, child):
        """
        :param tree: 树结构
        :param parent: 给定的节点作为双亲节点
        :param child: 插入的节点
        :return:
        """
        if tree is None:
            return
        if parent is None:
            return
        # 声明存储子树的队列
        subtreequeue = [tree]
        while subtreequeue:
            subtree = subtreequeue.pop(0)
        
            if subtree.data == parent:
                # 补齐空的左节点
                if subtree.left is None and subtree.right is not None:
                    if subtree.right.data != child:
                        subtree.left = TreeNode(child)  # 注意此处应该赋值一个树节点，而不是一个数值
                        self.insertedres = [subtree.data, child, subtree.right.data]
                        return self.insertedres
                        # return tree
                    else:
                        self.insertedres = [subtree.data, None, subtree.right.data]
                        return self.insertedres
            
                elif subtree.left is not None and subtree.right is None:
                    if subtree.left.data != child:
                        subtree.right = TreeNode(child)  # 注意此处应该赋值一个树节点，而不是一个数值
                        self.insertedres = [subtree.data, subtree.left.data, child]
                        return self.insertedres
                        # return tree
                    else:
                        self.insertedres = [subtree.data, subtree.left.data, None]
                        return self.insertedres
            
                elif subtree.left is None and subtree.right is None:
                    subtree.left = TreeNode(child)  # 注意此处应该赋值一个树节点，而不是一个数值
                    self.insertedres = [subtree.data, child, None]
                    return self.insertedres
                    # return tree
                else:
                    self.insertedres = [subtree.data]
                    return self.insertedres
                    # return tree
            else:
                if subtree.left is not None:
                    subtreequeue.append(subtree.left)
                if subtree.right is not None:
                    subtreequeue.append(subtree.right)

    # 前序遍历-递归方法
    def preorder(self, tree):
        """前序遍历"""
        if tree is None:
            return
        self.preres.append(tree.data)
        self.preorder(tree.left)
        self.preorder(tree.right)

    def preordertraverse(self, tree):
        self.preorder(tree)
        return self.preres

    # 中序遍历遍历-递归方法
    def inorder(self, tree):
        """中序遍历"""
        if tree is None:
            return
        self.inorder(tree.left)
        self.inres.append(tree.data)
        self.inorder(tree.right)

    def inordertraverse(self, tree):
        self.inorder(tree)
        return self.inres

    # 后序遍历遍历-递归方法
    def postorder(self, tree):
        """后序遍历"""
        if tree is None:
            return
        self.postorder(tree.left)
        self.postorder(tree.right)
        self.postres.append(tree.data)

    def postordertraverse(self, tree):
        self.postorder(tree)
        return self.postres

    # 前序遍历-非递归方法

    def preordertraversestack(self, root):
        if root is None:
            return
        stack = []
        # result = []
        node = root
        while node or stack:
            while node:
                # result.append(node.data)  # 当前根节点的数值
                self.preresnon.append(node.data)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        # return result
        return self.preresnon

    # 中序遍历-非递归方法
    def inordertraversestack(self, root):
        if root is None:
            return
        stack = []
        # result = []
        node = root
        while node or stack:
            while node:
                # 树的左子树一直遍历到叶子节点，栈中全部是左子树
                stack.append(node)
                node = node.left
            node = stack.pop()
            # result.append(node.data)
            self.inresnon.append(node.data)
            node = node.right
        # return result
        return self.inresnon
    
    # 后序遍历-非递归方法
    def postordertraversestack(self, root):
        if root is None:
            return
        seq = []
        # result = []
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
            # result.append(seq.pop())
            self.postresnon.append(seq.pop())
        # return result
        return self.postresnon

# 层次遍历（广度优先遍历）
    def breadthfirsttraversal(self, tree):
        if tree is None:
            return
        sequence = []  # 声明一个先进先出的队列存放子树
        # result = []  # 声明一个列表存放节点数值
        node = tree
        sequence.append(node)  # 现将整个树假如队列中
        while sequence:  # 当前队列不为空，表示队列中还有需要遍历的子树
            node = sequence.pop(0)  # 当前队列中的子树出队列
            # result.append(node.data)  # 将当前子树中的根节点的数值存放在reslut列表中
            self.breadthresult.append(node.data)
            if node.left is not None:  # 当前子树的左子树存在，则先加入到队列中
                sequence.append(node.left)
            if node.right is not None:  # 当前子树的右子树存在，则后加入到队列中
                sequence.append(node.right)
        # return result
        return self.breadthresult
    
    # 获取遍历的所有路径-采用深度优先遍历的方式实现
    def generatingpaths(self, tree, path):
        if tree is None:
            return
        path += str(tree.data)  # 添加节点的数据，即参数path的初始化数值是一个空值
        if tree.left is None and tree.right is None:
            self.depthfirsttraversalpath.append(path)  # 列表用于存放遍历到叶子节点以后所形成的节点路径
        else:
            path += '->'
            self.generatingpaths(tree.left, path)
            self.generatingpaths(tree.right, path)
    
    def getallpathsbydepthfirst(self, tree):
        self.generatingpaths(tree, path='')  # 参数path的数值是一个空值
        return self.depthfirsttraversalpath

    # 获取遍历的所有路径-采用广度优先遍历的方式实现
    def getallpathsbybreadthfirst(self, tree):
        if tree is None:
            return
        # 使用collections模块需要在在脚本的最开始的地方使用import命令
        # nodequence = collections.deque([tree])
        # pathquence = collections.deque([str(tree.data)])
        
        nodequence = [tree]
        pathquence = [str(tree.data)]
        while nodequence:
            # path = pathquence.popleft()  # 取出路径队列中的第一个元素
            # node = nodequence.popleft()  # 取出节点队列中的第一个元素

            path = pathquence.pop(0)  # 取出路径队列中的第一个元素
            node = nodequence.pop(0)  # 取出节点队列中的第一个元素
            
            if node.left is None and node.right is None:
                self.breadthfirsttraversalpath.append(path)
            else:
                if node.left is not None:
                    nodequence.append(node.left)
                    pathquence.append(path + '->' + str(node.left.data))
                
                if node.right is not None:
                    nodequence.append(node.right)
                    pathquence.append(path + '->' + str(node.right.data))
        
        return self.breadthfirsttraversalpath


# 主函数


if __name__ == '__main__':
    
    # 1: 构建树的节点（节点的数据域，节点的左子树，节点的右子树）
    btree = BinaryTree()
    for i in range(0, 10):
        btree.insertnode(i)

    # 2：调用树的方法
    print('# 2：调用树的方法')
    print('>> 统计叶子节点的个数：')
    print(btree.getleafnodesamount(btree.root))
    print('>> 输出树的叶子节点：')
    print(' '.join(map(str, btree.getleafnodes(btree.root))))
    print('>> 输出树的高度：')
    print(btree.getheightoftree(btree.root))
    print('>> 树的根节点：')
    print(btree.getrootval(btree.root))
    print('>> 修改树的根节点：')
    print(btree.setrootnewval('x'))
    
    print('>> 返回树的左子树节点：')
    print(btree.getleftchildnode(btree.root))
    print('>> 返回树的右子树节点：')
    print(btree.getrightchildnode(btree.root))
    print('>> 前序遍历-递归方法:')
    print(btree.preordertraverse(btree.root))
    print('>> 中序遍历-递归方法:')
    print(btree.inordertraverse(btree.root))
    print('>> 后序遍历-递归方法:')
    print(btree.postordertraverse(btree.root))
    print('>> 前序遍历-非递归方法:')
    print(btree.preordertraversestack(btree.root))
    print('>> 中序遍历-非递归方法:')
    print(btree.inordertraversestack(btree.root))
    print('>> 后序遍历-非递归方法:')
    print(btree.postordertraversestack(btree.root))
    print('>> 层次遍历（广度优先遍历：）')
    print(btree.breadthfirsttraversal(btree.root))
    
    print('>> 深度优先遍历的所有节点路径：')
    print(btree.getallpathsbydepthfirst(btree.root))
    
    print('>> 广度优先遍历的所有节点路径：')
    print(btree.getallpathsbybreadthfirst(btree.root))

    print('>> 返回树中指定节点的双亲节点：')
    print(btree.getparentnode(btree.root, 6))

    print('>> 返回树中指定节点的右兄弟：')
    print(btree.getrightbrother(btree.root, 5))

    print('>> 返回树中指定节点的左兄弟：')
    print(btree.getleftbrother(btree.root, 6))

    print('>> 插入新的节点:')
    print(btree.insertmissingnode(btree.root, 2, 5))
        