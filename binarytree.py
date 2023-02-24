'''
================ MEMBERS =====================
นาย     ณัฐวัฒน์    พวงยี่สุ่น    INE 6506022620044
นางสาว  เนติญา     ภูริทัตสิริ    INE 6506022630015
นางสาว  พัชร์กวี     กีรติตระกูล  INE 6506022630031
นาย     ภาณุวัฒน์   กลิ่นสุคนธ์  INE 6506022630058
'''

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+ ' is found')

    def InorderTraversal(self,root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res
    
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
    
    def Delete(self,num):
        if num < self.data:
            if self.left != None:
                self.left = self.left.Delete(num)
            return self
        elif num > self.data:
            if self.right != None:
                self.right = self.right.Delete(num)
            return self
        else:
            if self.left == None:
                return self.right
            elif self.right == None:
                return self.left
            else:
                min_node = self.right.Find_min()
                self.data = min_node.data
                self.right = self.right.Delete(min_node.data)
                return self
            
    def Find_min(self):
        while self.left != None:
            self = self.left
        return self
    
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()
print(root.findval(7))
print(root.findval(35))
print('In  ',root.InorderTraversal(root))
print('Pre ',root.PreorderTraversal(root))
print('Post',root.PostorderTraversal(root))

root.Delete(int(input('Delete Num: ')))
print('In  ',root.InorderTraversal(root))
print('Pre ',root.PreorderTraversal(root))
print('Post',root.PostorderTraversal(root))