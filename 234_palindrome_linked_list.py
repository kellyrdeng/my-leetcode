# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #use floyd's to find middle of the list
        beginning, slow, fast = head, head, head
        while fast and fast.next: #checking fast.next handles list of length 1
            slow = slow.next
            fast = fast.next.next
        middle = slow

        #reverse the last half of the list
        prev = None
        cur = middle
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        end = prev

        #we have beginning, middle, and end
        #advance beginning and end towards middle, return False if beginning != end
        while end:
            if beginning.val != end.val:
                return False
            beginning = beginning.next
            end = end.next
        return True
