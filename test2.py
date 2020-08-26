# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        the_map = {}
        length = len(preorder)
        for i in range(length):
            the_map[inorder[i]] = i

        def build_helper(pre_start, pre_end, in_start):
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            root_index = the_map[preorder[pre_start]]
            left_tree_length = root_index - in_start
            root.left = build_helper(pre_start + 1, pre_start + left_tree_length, in_start)
            root.right = build_helper(pre_start + left_tree_length + 1, pre_end, root_index + 1)
            return root

        res = build_helper(0, length - 1, 0)
        return res


ls1 = [1,2,4,5,3,6,7]
ls2 = [4,2,5,1,6,3,7]
Solution().buildTree(ls1, ls2)
