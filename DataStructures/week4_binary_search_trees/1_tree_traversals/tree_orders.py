# python3

import sys, threading
sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:

  def read(self):
    self.n = int(input())
    self.key = [0] * (self.n)
    self.left = [0] * (self.n)
    self.right = [0] * (self.n)
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def choosen_tree(self, keys, left, right):
    self.n = len(keys)
    self.key = keys
    self.left = left
    self.right = right
    

  def test(self, case=1):
    """
    Test tree case
    """
    if case == 1:
      self.n = 5
      self.key = [4, 2, 5, 1, 3]
      self.left = [1, 3, -1, -1, -1]
      self.right = [2, 4, -1, -1, -1]
    if case == 2:
      self.n = 10
      self.key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
      self.left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
      self.right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]


  def preOrder(self):
    self.result = self.treeTraversal(traversal_strategy=0)              
    return self.result

  def inOrder(self):
    self.result = self.treeTraversal(traversal_strategy=1)      
    return self.result

  def postOrder(self):
    self.result = self.treeTraversal(traversal_strategy=2)             
    return self.result


  def inOrderIter(self):
    if len(self.key) == 0:
      return []

    stack = []
    result = []
    parent_index = 0

    while len(result) != self.n:

      if parent_index != -1:
        stack.append(parent_index)
        parent_index = self.left[parent_index]
      elif stack:
        parent_index = stack.pop()
        result.append(self.key[parent_index])
        parent_index = self.right[parent_index]
    else:
      return result
    
  def preOrderIter(self):
    if len(self.key) == 0:
      return []

    stack = [0]
    result = []
    parent_index = 0

    while len(result) != self.n:
      parent_index = stack.pop()
      result.append(self.key[parent_index])
      if self.right[parent_index] != -1:
        stack.append(self.right[parent_index])
      if self.left[parent_index] != -1:
        stack.append(self.left[parent_index])

    else:
      return result      

  def postOrderIter(self):
    if len(self.key) == 0:
      return []

    stack = []
    result = []
    parent_index = 0

    while True:

      while parent_index != -1:
        if self.right[parent_index] != -1:
          stack.append(self.right[parent_index])
        stack.append(parent_index)

        parent_index = self.left[parent_index]

      parent_index = stack.pop()

      if stack and self.right[parent_index] != -1 and stack[-1] == self.right[parent_index]:
        stack.pop()
        stack.append(parent_index)
        parent_index = self.right[parent_index]
      else:
        result.append(self.key[parent_index])
        parent_index = -1

      if len(stack) <= 0:
        break

    return result  


  def treeTraversal(self, parent_index=0, traversal_strategy:int=1):
    result = []

    # Pre order Traversal
    if traversal_strategy == 0:
      result.append(self.key[parent_index])

    if self.left[parent_index] != -1:
      result += self.treeTraversal(self.left[parent_index], traversal_strategy)

    # In order Traversal
    if traversal_strategy == 1:
      result.append(self.key[parent_index])

    if self.right[parent_index] != -1:
      result += self.treeTraversal(self.right[parent_index], traversal_strategy)
    
    # Post order traversal
    if traversal_strategy == 2:
      result.append(self.key[parent_index])

    return result


def create_tree(keys, left, right):
  tree = TreeOrders()
  tree.choosen_tree(keys, left, right)
  return tree

def do_traversal(tree, main_sol=False, recurse=False, iterative=False):
  if main_sol:
    inOrderMain = tree.inOrder()
    preOrderMain = tree.preOrder()
    postOrderMain = tree.postOrder()
    return inOrderMain, preOrderMain, postOrderMain
  if recurse:
    pass
  if iterative:
    inOrderIter = tree.inOrderIter()
    preOrderIter = tree.preOrderIter()
    postOrderIter = tree.postOrderIter()
    return inOrderIter, preOrderIter, postOrderIter

def run_test(tree):
  inMain, preMain, postMain = do_traversal(tree, main_sol=True)
  inIter, preIter, postIter = do_traversal(tree, iterative=True)
  return ((inMain, preMain, postMain), (inIter, preIter, postIter))
  
def time_test(tree, solution, traversal):
  if solution == "main":
    if traversal == "in":
      tree.inOrder()
    elif traversal == "pre":
      tree.preOrder()
    elif traversal == "post":
      tree.postOrder()
  elif solution == "iter":
    if traversal == "in":
      tree.inOrderIter()
    elif traversal == "pre":
      tree.preOrderIter()
    elif traversal == "post":
      tree.postOrderIter()
  


def main():
	tree = TreeOrders()
	#tree.test(case=2)
	tree.read()
	#print(tree.inOrderImprooved() == tree.inOrder())
	#print(tree.preOrderImprooved() == tree.preOrder())
	#print(tree.postOrderImprooved() == tree.postOrder())
	#print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.inOrderIter()))
	#print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.preOrderIter()))
	#print(" ".join(str(x) for x in tree.postOrder()))
	print(" ".join(str(x) for x in tree.postOrderIter()))

threading.Thread(target=main).start()
