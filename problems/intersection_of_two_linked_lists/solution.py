# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        temp1 = headA
        A = headA
        B = headB
        while temp1:
            lengthA += 1
            temp1 = temp1.next
        lengthB = 0
        temp2 = headB
        while temp2:
            lengthB += 1
            temp2 = temp2.next
        diff = abs(lengthA - lengthB)
        if lengthA > lengthB:
            while diff:
                A = A.next
                diff -= 1
        else:
            while diff:
                B = B.next
                diff -= 1
        while A and B:
            if A == B:
                return A
            A = A.next
            B = B.next

