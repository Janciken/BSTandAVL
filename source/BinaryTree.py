class Node:
    def __init__(self,data):
        self.data=int(data)
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data>data:
            if self.left==None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        elif self.data<data:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data)
        else:
            return

    def delete(self,target,parent):
        if target < self.data:
            if self.left!=None:
                return self.left.delete(target,self)
            else:
                print("Non-Existing")
                return None
        elif target > self.data:
            if self.right!=None:
                return self.right.delete(target,self)
            else:
                print("Non-Existing")
                return None
        else:
            replacement=self.findReplacement()
            if parent.data>self.data:
                parent.left=replacement
            else:
                parent.right=replacement
            if replacement!=None:
                replacement.left=self.left
                replacement.right=self.right

    def findReplacement(self):
        if self.left!=None:
            if self.left.right!=None:
                return self.left.right.findMax(self.left)
            else:
                forreturn=self.left
                self.left=self.left.left
                return forreturn
        elif self.right!=None:
            if self.right.left!=None:
                return self.right.left.findMin(self.right)
            else:
                forreturn=self.right
                self.right=self.right.right
                return forreturn
        else:
            return None

    def findMax(self,parent):
        if self.right==None:
            parent.right=self.left
            return self
        else:
            return self.right.findMax(self)

    def findMin(self,parent):
        if self.left==None:
            parent.left=self.right
            return self
        else:
            return self.left.findMin(self)

    def preorder(self):
        print(self.data,end=" ")
        if self.left!=None:
            self.left.preorder()
        if self.right!=None:
            self.right.preorder()

    def inorder(self):
        if self.left!=None:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right!=None:
            self.right.inorder()

    def postorder(self):
        if self.left!=None:
            self.left.postorder()
        if self.right!=None:
            self.right.postorder()
        print(self.data,end=" ")

    def draw(self,canvas,x,y,a,b):
        if b>10:
            b-=2
        canvas.create_line(x,y,x-a/2,y+40)
        canvas.create_line(x,y,x+a/2,y+40)
        canvas.create_oval(x-b,y-b,x+b,y+b,fill='white')
        canvas.create_text(x,y,text=self.data)
        if self.left!=None:
            self.left.draw(canvas,x-a/2,y+40,a/2,b)
        if self.right!=None:
            self.right.draw(canvas,x+a/2,y+40,a/2,b)

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(int(data))
        else:
            self.root.insert(int(data))

    def delete(self,target):
        if self.root==None:
            print("Nothing to delete")
            return None
        elif self.root.data==target:
            replacement=self.root.findReplacement()         #najdi nahradcu
            replacement.left=self.root.left                 #nahradcovi pridaj lavu stranu rootu
            replacement.right=self.root.right                #nahradcovi pridaj pravu stranu rootu
            forreturn=self.root
            self.root=replacement                           #root pointer nastav teraz na nahradcu
            return forreturn
        else:
            if self.root.data>target:
                if self.root.left!=None:
                    return self.root.left.delete(target,self.root)
                else:
                    print("Non-Existing")
                    return None
            else:
                if self.root.right!=None:
                    return self.root.right.delete(target,self.root)
                else:
                    print("Non-Existing")
                    return None

    def printTree(self):
        print("Preorder: ",end="")
        self.root.preorder()
        print()
        print("Inorder: ", end="")
        self.root.inorder()
        print()
        print("Postorder: ", end="")
        self.root.postorder()
        print()

    def kresli(self, canvas):
        if self.root != None:
            self.root.draw(canvas, 600, 40, 600, 22)



"""
stromcek=BinarySearchTree()
for i in 50,30,90,80,20,13,44,57,78,12:
    stromcek.insert(i)

stromcek.printTree()
"""

"""
    def remove(self,data):
        if self.data>int(data):
            if self.left.data==int(data):
                self.left=None
            else:
                self.left.remove(data)
        elif self.data<int(data):
            if self.right.data==int(data):
                self.right=None
            else:
                self.right.remove(data)
"""

"""
    def remove(self,data):
        if self.root.data==int(data):
            self.root=None
        else:
            self.root.remove(int(data))
"""