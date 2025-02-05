from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        new_node = ListNode(i)
        current.next = new_node
        current = new_node

    print("Original linked list:")
    print_linked_list(head)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("\nReversed linked list:")
    print_linked_list(reversed_head)
