class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        def find_middle(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        if not head or not head.next:
            return True
        middle = find_middle(head)
        second_half = reverse_list(middle)
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True
