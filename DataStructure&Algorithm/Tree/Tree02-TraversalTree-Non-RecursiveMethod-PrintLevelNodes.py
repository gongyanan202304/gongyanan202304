# 树的遍历-输出每一层的节点
# 这脚本是设计怎么输出二叉树的每一层的节点，并统计每一层的节点个数
# 解题思路：
# （1）采用满完全二叉树的特点来设计代码
# （2）当一个节点的左子树或者右子树为空时，则在子树队列中田间一个空节点
# （3）当子树队列中的节点个数为该层的满层节点数目，则将节点层次、节点数目与节点添加到字典中
# （4）脚本中采用递归方法求取原树的高度，作为树的层次最大值


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right
        
    def getheightoftree(self, bintree):
        if bintree is None:
            return 0
        if bintree.left is None and bintree.right is None:
            return 1
        else:
            return 1 + max(self.getheightoftree(bintree.left), self.getheightoftree(bintree.right))
    
    def getnodesoflevel(self, bintree):
        if bintree.key is None:
            return
        lvlnoderes = {}  # 存储所有层的节点层次、节点数目与节点
        lvlnodes = []  # 存储每一层的节点
        nodescnt = 0  # 统计每一次层的节点数目
        queue = [bintree]  # 子树队列-先进先出
        lvl = 1
        height = self.getheightoftree(bintree)
        
        while height-lvl >= 0:
            subtree = queue.pop(0)
            if lvl == 1:
                lvlnoderes['Level='+str(lvl)] = ['NodesCnt='+str(1), [subtree.key]]
                lvl += 1
                
            if subtree.left is not None and subtree.right is not None:
                queue.append(subtree.left)
                queue.append(subtree.right)
            elif subtree.left is None and subtree.right is not None:
                nonenode = BinaryTree(None)
                queue.append(nonenode)
                queue.append(subtree.right)
                
            elif subtree.left is not None and subtree.right is None:
                queue.append(subtree.left)
                nonenode = BinaryTree(None)
                queue.append(nonenode)
                
            else:
                nonenode = BinaryTree(None)
                queue.append(nonenode)
                queue.append(nonenode)
                
            if len(queue) == pow(2, lvl-1):
        
                for nodes in queue:
                    if nodes.key is not None:
                        lvlnodes.append(nodes.key)
                        nodescnt += 1
                lvlnoderes['Level=' + str(lvl)] = ['NodesCnt=' + str(nodescnt), lvlnodes]
                lvl += 1
                lvlnodes = []  # 存储每一层的节点,下一层节点遍历的初始化
                nodescnt = 0  # 统计每一层的节点数目,下一层节点遍历的初始化
        
        return lvlnoderes


# 主函数

if __name__ == "__main__":
    
    treeL1 = BinaryTree(1)
    treeL1.left = BinaryTree(3)
    treeL1.right = BinaryTree(4)
    
    treeR1 = BinaryTree(2)
    treeR1.left = BinaryTree(5)
    treeR1.right = BinaryTree(6)

    tree = BinaryTree(0)
    tree.left = treeL1
    tree.right = treeR1
    
    # 循环遍历每一层的节点
    for key, value in tree.getnodesoflevel(tree).items():
        print(key, value[0], value[1])
