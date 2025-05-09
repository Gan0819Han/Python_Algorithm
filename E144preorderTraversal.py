# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        
        # 迭代进行前序排序（中左右）
        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            
            # 迭代
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return res