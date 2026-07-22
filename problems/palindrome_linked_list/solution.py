# Definition for singly-linked list.
# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first = head
        second = prev

        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next        
        return True


        