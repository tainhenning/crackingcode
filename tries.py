# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:00:55 2018

@author: Tain
"""

class Node(object):
    left = None
    right = None
    letter = "A"

t1 = Node()
t2 = Node()
t3 = Node()
t4 = Node()
t5 = Node()

t1.letter = "A"
t2.letter = "P"
t3.letter = "P"
t4.letter = "R"
t5.letter = "T"

t1.left = t2
t2.left = t3

t1.right = t4
t4.right = t5

print(t1.letter, t1.left.letter, t1.left.left.letter)
print(t1.letter, t1.right.letter, t1.right.right.letter)
