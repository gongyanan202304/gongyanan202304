# 递归方法+链表实现树的构造

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftchild = None
        self.rightchild = None
    
    def insertleft(self, newnode):
        if self.leftchild is None:
            self.leftchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t
    
    def insertright(self, newnode):
        if self.rightchild is None:
            self.rightchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getleftchild(self):
        if self.key is None:
            return
        else:
            if self.leftchild is None:
                return
            else:
                return self.leftchild.key
    
    def getrightchild(self):
        if self.key is None:
            return
        else:
            if self.rightchild is None:
                return
            else:
                return self.rightchild.key
            

if __name__ == "__main__":
    
    tree = BinaryTree(0)
    tree.insertleft(1)
    tree.insertright(2)
    print(tree.getleftchild())
    print(tree.getrightchild())
