# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            kth = groupPrev
            for i in range(k):
                if kth.next is None:
                    return dummy.next
                kth = kth.next
            groupNext = kth.next
            prev = groupNext
            current = groupPrev.next
            while current != groupNext:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp


           


        