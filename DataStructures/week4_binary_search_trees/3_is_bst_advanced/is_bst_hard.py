#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  return inOrderTraversal(tree)

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
      if parent_index != -1 and tree[stack[-1]][0] == tree[parent_index][0]:
        return False
    elif stack:
      parent_index = stack.pop()
      if len(result) and result[-1] <= tree[parent_index][0]:
        result.append(tree[parent_index][0])
        parent_index = tree[parent_index][2]
      elif not len(result):
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
    if penult < penultimate:
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
  tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
  # tree = [[100, 7, 2], [120, -1, -1], [100, -1, 6], [30, 8, 9], [75, 3, -1], [10, -1, -1], [120, -1, 1], [15, 5, 4], [20, -1, -1], [35, -1, -1]]
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")
"""

threading.Thread(target=main).start()
