# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:35:21 2018

@author: Tain
"""

class Node(object):
    val = 0
    nxt = None
class DoubleNode(object):
    val = 0
    nxt = None
    prev = None
    
n1 = Node()
n2 = Node()
n3 = Node()

n1.nxt = n2
n2.nxt = n3
n3.nxt = n1

n1.val = 1
n2.val = 2
n3.val = 3

print(n1.val, n1.nxt.val, n1.nxt.nxt.val)

dn1 = DoubleNode()
dn2 = DoubleNode()
dn3 = DoubleNode()

dn1.nxt = dn2
dn2.nxt = dn3
dn3.nxt = dn1

dn1.prev = dn3
dn2.prev = dn1
dn3.prev = dn2

dn1.val = 1
dn2.val = 2
dn3.val = 3

print(dn1.val, dn1.prev.val, dn1.prev.prev.val)
