# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        llen = 0

        while temp:
            llen +=1
            temp = temp.next

        count = 1

        if n == llen:
            return head.next

        ls = head

        prev = head
        head = head.next

        while head:
            if count == llen-n:
                temp = head.next
                head = prev
                head.next = temp
                return ls
            prev= head
            head = head.next
            count += 1




