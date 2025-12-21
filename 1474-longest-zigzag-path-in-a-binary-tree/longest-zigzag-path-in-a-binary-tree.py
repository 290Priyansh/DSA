# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

 #wrong ans
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.length = 0
#         self.leftT = True
#         self.rightT = True
#         self.maxLength = 0
#         def dfs(node):
            
#             if not node:
#                 return
#             if node.left and self.leftT:
#                 self.leftT = False
#                 dfs(node.left)
#                 self.length+=1
#                 self.maxLength = max(self.length,self.maxLength)
                
#                 self.rightT = True
#             if node.right and self.rightT:
#                 self.rightT = False
#                 dfs(node.right)
#                 self.length+=1
#                 self.maxLength = max(self.length,self.maxLength)
#                 self.leftT = True
#         dfs(root)
#         return self.maxLength

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def dfs(node, direction, length):
            if not node:
                return

            self.maxLength = max(self.maxLength, length)

            # if last move was left, next must be right
            if direction != "left":
                dfs(node.left, "left", length + 1)
            else:
                dfs(node.left, "left", 1)

            # if last move was right, next must be left
            if direction != "right":
                dfs(node.right, "right", length + 1)
            else:
                dfs(node.right, "right", 1)

        dfs(root, None, 0)
        return self.maxLength


            