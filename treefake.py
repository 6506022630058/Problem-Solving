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
    def Findnoi(self,num):
        global noi
        if num < self.data:
            if self.left != None:
                self.left.Findnoi(num)
        elif num > self.data:
            if self.right != None:
                self.right.Findnoi(num)
        elif num == self.data:
            if self.right != None:
                self.right.Checkleft()
            elif self.right == None:
                noi = None
    def Checkleft(self):
        global noi
        if self.left != None:
            self.left.Checkleft()
        elif self.left == None:
            noi = self.data
        else:
            noi = self.left.Int()
    def Realdel(self,num):
        root.Findnoi(num)
        print(noi)
        if num < self.data:
            if num == self.left.Int():
                self.left = Node(noi)
            elif self.left == None:
                print('Error left')
            else:
                self.left.Realdel(num)
        elif num > self.data:
            if num == self.right.Int():
                self.right = Node(noi)
            elif self.right == None:
                print('Error right')
            else:
                self.right.Realdel(num)
    def Int(self):return self.data
    def Delnode(self,num):
        root.Findnoi(num)
        print(noi)
        if num < self.data:
            if self.left != None:
                if self.left.Int() != num:
                    self.left.Delnode(num)
                elif self.left.Int() == num:
                    self.left == Node(noi)
        elif num > self.data:
            if self.right != None:
                if self.right.Int() != num:
                    self.right.Delnode(num)
                elif self.right.Int() == num:
                    self.right == Node(noi)
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            return self
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
            return self
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                min_node = self.right.find_min()
                self.data = min_node.data
                self.right = self.right.delete(min_node.data)
                return self
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(19)
root.insert(21)
root.insert(5)
root.PrintTree()
print(root.findval(7))
print(root.findval(35))
print(root.InorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
root.delete(47)
print(root.InorderTraversal(root))
