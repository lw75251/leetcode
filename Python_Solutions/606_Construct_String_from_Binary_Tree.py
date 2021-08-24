# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        My Solution: O(n) Solution

        IDEA: Use recursive preorder traversal. There are a couple of cases
        to consider:
            1. For any node, if there exists a right node, then we need empty
            () for the left node regardless if left has a value
            2. If there exists only a left node, then we do not need the empty
            () for the right node
            3. If there is no left or right node, then we don't need the empty
            () for both nodes

        # Time Complexity: O(n), where n = num nodes in tree
        # Space Complexity: O(n) because of n recursive calls
        """
        s = ""
        if root:
            s = str(root.val)
            left = right = ""

            if root.left:
                left = str(self.tree2str(root.left))
            if root.right:
                right = str(self.tree2str(root.right))

            # Add left result and right result
            if right != "":
                s += "(" + left + ")"
                s += "(" + right + ")"
                return s

            # Add only left result
            if left != "":
                s += "(" + left + ")"
                return s
        return s

    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Cleaner Solution: O(n) Solution

        Solution IDEA: Use recursive preorder traversal. Cases to consider:
            1. Left and Right Child exists, meaning we need braces () around
            both left and right children
            2. No children exist, meaning we do not need any () around the
            left and right children
            3. Only left child exists, meaning we need braces () around only
            the left child
            4. Only right child exists, meaning we need an empty brace () for
            the left child, and a brace () for the right child.

        # Time Complexity: O(n), where n = num nodes in tree
        # Space Complexity: O(n) because of n recursive calls
        """

        # Empty Case
        if not root:
            return ""

        # Case: No Children
        if not root.left and not root.right:
            return f"{root.val}"

        # Case: Only Left Child
        if not root.right:
            return f"{root.val}({self.tree2str(root.left)})"

        # Case: Right Child
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
