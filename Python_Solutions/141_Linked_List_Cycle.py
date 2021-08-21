class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        My Solution: O(n) Solution

        IDEA: There is a slow pointer that travels no more than n steps, and a
        fast pointer that must travel less than n steps (moves 2 steps). There
        is a cycle if the slow and faster pointer equal each other at some
        point. If fast reaches the end, there is no cycle.

        # Time Complexity: O(n), where n = number of nodes
        # Space Complexity: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False
