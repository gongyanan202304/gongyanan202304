# > 二叉排序树简介
# 二叉排序树是在完全二叉树的基础上进行节点数值大小比较进行的构建的。
# 二叉排序树是一个动态构建的树。
# 该脚本设计了二叉排序树的增删改查的代码，尤其是增删查
# > 程序设计思路：
# 1-动态插入节点：
#   （1）判定当前的树是否为空，为空则把node设置为树的根节点；不为空，则判定当前树的根节点的数据与node的数据大小；
#   （2）当node的数据大于当前树的根节点的数据，则将node插入到当前树的右子树中的空节点；
#   （3）当node的数据小于当前树的根节点的数据，则将node插入到当前树的左子树中的空节点。
#   （4）while True 循环步骤中的（1）（2）（3）三个步骤，直到左右的节点数据插入完成。
# 2-动态查找节点：
#   （1）判定当前树是否为空，为空则输出空；不为空，则比较当前树的根节点的data与key的大小；
#   （2）当当前树的根节点的data等于key，则输出True、parent与key；
#   （3）当当前树的根节点的data大于key，则在当前树的左子树中查找节点。若存在则输出True、parent与key；若不存在则输出False、None与key。
#   （4）当当前树的根节点的data小于key，则在当前树的右子树中查找节点。若存在则输出True、parent与key；若不存在则输出False、None与key。
#   （5）while root 循环步骤中的 （2）（3）（4）三个步骤，直到找到节点或者遍历完整个树。

class SortedBinaryTree:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return '<node:%d>' % self.data
        
    def dynamicinsertnodes(self, data):
        """动态增加二叉排序树的节点"""
       
        if data is None:
            return
        
        node = SortedBinaryTree(data)
        
        if self.data is None:
            self.data = node
            
        # 初始化一棵树
        tree = self
        # 循环向树中插入节点
        while True:
            root = tree.data
            if data < root:
                if tree.left is None:
                    tree.left = node
                tree = tree.left
                
            elif data > root:
                if tree.right is None:
                    tree.right = node
                tree = tree.right
                
            else:
                return
    
    @staticmethod
    def dynamicsearchnode(tree, key):
        """动态查找排序二叉树的节点"""
        if tree is None:
            return
        if key is None:
            return
        parent = -1  # 双亲节点初始值为-1（tree的根节点的双亲节点为-1）
        while tree:
            # 当当前树的根节点的数据=key
            if tree.data == key:
                return True, parent, tree
            
            # 当当前树的根节点的数据<key
            elif tree.data < key:
                if tree.right is not None:
                    parent = tree
                    tree = tree.right
                else:
                    return False, None, key
            
            # 当当前树的根节点的数据>key
            else:
                if tree.left is not None:
                    parent = tree
                    tree = tree.left
                else:
                    return False, None, key
    
    def dynamicdeletenode(self, tree, key):
        """动态删除二叉排序树中指定节点"""
        
        # 判定二叉排序树是否为空
        if tree is None:
            print('排序二叉树是空树')
            return
        # 判定节点key是否存在
        isintree, parent, curnode = self.dynamicsearchnode(tree, key)
        
        # 删除节点不存在于二叉排序树中
        if not isintree:  # 当isintree==False时执行下列语句
            print('需要删除的姐弟{key}不存在')
            return
        
        # 当处理节点是树的根节点，则不执行删除操作
        if tree.data == key:
            print('不能删除树的根节点')
            return
        
        # 1-删除节点key是叶子节点
        if curnode.left is None and curnode.right is None:
            if parent.left == curnode:
                parent.left = None
            if parent.right == curnode:
                parent.right = None
        
        # 2-删除节点key 仅仅含有左子树或者右子树
        # (1) 当前节点为其双亲节点的左孩子：
        if curnode == parent.left:
            if curnode.left is not None and curnode.right is None:
                # 当前节点仅有左子树
                parent.left = curnode.left
            if curnode.left is None and curnode.right is not None:
                # 当前节点仅有右子树
                parent.left = curnode.right
        # (2) 当前节点为其双亲节点的右孩子：
        if curnode == parent.right:
            if curnode.left is not None and curnode.right is None:
                # 当前节点仅有左子树
                parent.right = curnode.left
            if curnode.left is None and curnode.right is not None:
                # 当前节点仅有右子树
                parent.right = curnode.right
            
        # 3-删除节点key 既含有左子树又含有右子树
        if curnode.left is not None and curnode.right is not None:
            # (1) 当前节点为其双亲节点的左孩子：
            if curnode == parent.left:
                curleft = curnode.left  # 当前节点的左子树
                curright = curnode.right  # 当前节点的右子树
                parent.left = curleft  # 当前节点的双亲节点的左子树指向当前节点的左子树
                travertree = curleft  # 将当前节点的左子树赋值给遍历树
                while travertree.right:
                    # 一直遍历原来左子树中的右子树的右子树
                    travertree = travertree.right
                # 将遍历到最后的遍历树的右子树指向当前节点的右子树
                travertree.right = curright

            # (2) 当前节点为其双亲节点的右孩子：
            if curnode == parent.right:
                curleft = curnode.left  # 当前节点的左子树
                curright = curnode.right  # 当前节点的右子树
                parent.right = curright  # 当前节点的双亲节点的右子树指向当前节点的右子树
                travertree = curright  # 将当前节点的右子树赋值给遍历树
                while travertree.left:
                    # 一直遍历原来you子树中的zuo子树的zuo子树
                    travertree = travertree.left
                # 将遍历到最后的遍历树的zuo子树指向当前节点的zuo子树
                travertree.left = curleft
    
    @staticmethod
    def breadthtraver(tree):
        """广度优先遍历"""
        if tree is None:
            return
        result = []  # 存放遍历节点的结果表
        subtreequeue = [tree]  # 存放子树的队列
        while subtreequeue:
            subtree = subtreequeue.pop(0)
            result.append(subtree.data)
            if subtree.left is not None:
                subtreequeue.append(subtree.left)
            if subtree.right is not None:
                subtreequeue.append(subtree.right)
        
        return result
        
# 主函数


if __name__ == "__main__":
    # nodelst = [0, 1, 2, 3, 4, 5, 8, 6, 7]
    nodelst = [5, 3, 2, 4, 7, 6, 8]
    sbtree = SortedBinaryTree(5)
    for i in nodelst:
        sbtree.dynamicinsertnodes(i)
    
    print('>> 输出二叉排序树')
    print(sbtree)
    
    print('>> 广度优先遍历二叉排序树：')
    print(sbtree.breadthtraver(sbtree))
    
    print('>> 查找二叉排序中的指定的节点：')
    boolres, parentnode, keynode = sbtree.dynamicsearchnode(sbtree, 4)
    print('节点是否存在：', boolres)
    print('双亲节点:', parentnode)
    print('指定节点:', keynode)
    
    print('>> 删除二叉排序树中的指定的节点：')
    sbtree.dynamicdeletenode(sbtree, 3)

    print('>> 广度优先遍历二叉排序树：')
    print(sbtree.breadthtraver(sbtree))
