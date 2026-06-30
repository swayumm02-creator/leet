class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Reach the node just before the sub-list to be reversed
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. Set pointers at the beginning of the sub-list
        curr = prev.next
        
        # 3. Reverse the sub-list nodes one by one
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next