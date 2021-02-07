#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  return inOrderTraversal(tree)

# keys list = tree[0]
# left list = tree[1]
# right list = tree[2]
def inOrderTraversal(tree):
  if len(tree) == 0:
    return True

  stack = []
  result = []
  parent_index = 0

  while len(result) != len(tree):
    if parent_index != -1:
      stack.append(parent_index)
      parent_index = tree[parent_index][1]
    elif stack:
      parent_index = stack.pop()
      if not len(result) or result[-1] <= tree[parent_index][0]:
        result.append(tree[parent_index][0])
        parent_index = tree[parent_index][2]
      else:
        return False

  return True


  
def treeTraversal(tree, parent_index=0, traversal_strategy:int=1):
  if not len(tree):
    return True
  left = tree[parent_index][1]
  if left != -1:
    penultimate = treeTraversal(tree, left, traversal_strategy)
    if penultimate is False:
      return False

  # In order Traversal
  if traversal_strategy == 1:
    penult = tree[parent_index][0]
    if left != -1:
      if penult <= penultimate:
        return False
    penultimate = penult
  
  right = tree[parent_index][2]
  if right != -1:
    penult = treeTraversal(tree, right, traversal_strategy)
    if penult <= penultimate:
      return False

  return penult
  

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

"""
def main():
  tree = [[100, 7, 2], [110, -1, -1], [120, -1, 6], [30, 8, 9], [75, 3, -1], [10, -1, -1], [160, 1, -1], [15, 5, 4], [20, -1, -1], [35, -1, -1]]
  #tree = [[4, 1, 2], [2, 3, 4], [5, -1, -1], [1, -1, -1], [3, -1, -1]]
  #tree = [[0, 7, 2],[10, -1, -1], [20, -1, 6], [30, 8, 9], [40, 3, -1], [50, -1, -1], [60, 5, 4], [70, -1, -1], [80, -1, -1], [90, -1, -1]]
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")
"""

threading.Thread(target=main).start()
