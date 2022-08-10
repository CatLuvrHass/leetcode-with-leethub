# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Converts a sorted array to a BST
        
        @parameters: nums (List[int])
        @returns: TreeNode
        '''
        def bst(left, right):
            if left < right:
                mid = left + (right - left) // 2
                
                return TreeNode(val = nums[mid],
                                left = bst(left, mid),
                                right = bst(mid+1, right))
        return bst(0, len(nums))
        
