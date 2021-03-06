#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = []
        st.append((root, 0))
        rs = []
        while st:
            (r, d) = st.pop()
            if not r: continue             
            if d == 0:
                rs.append(r.val)
                st.append((r, 1))
                st.append((r.left, 0))
            elif d == 1:
                st.append((r.right, 0))
        return rs
