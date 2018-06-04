# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:42:59 2018

@author: Tain
"""
class Node(object):
    val = 0
    left = None
    right = None

n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()

n1.val = 1
n2.val = 2
n3.val = 3
n4.val = 4
n5.val = 5

n1.left = n2
n1.right = n3
n2.left = n4
n3.right = n5

tree = [n1,n2,n3,n4,n5]
   
for x in range(0, len(tree)):
    print(tree[x].val, ": ")
    if(tree[x].left == None and tree[x].right != None):
        print(tree[x].right.val)
    elif(tree[x].left != None and tree[x].right == None):
        print(tree[x].left.val)
    elif(tree[x].right != None and tree[x].right != None):
        print(tree[x].left.val,tree[x].right.val)
