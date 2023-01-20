class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: List[ListNode], n: int) -> List[ListNode]:
        # create a node point to head, starts at pos -1
        result = ListNode(0, head) 
        left = result
        right = head

        # move the right ptr by n pos, reach the end ahead the left ptr
        while n > 0:
            right = right.next
            n -= 1

        # traverse along the list, stop when right ptr reaches the end
        while right:
            left = left.next
            right = right.next
        
        # deletion by update the prev ele pointer
        left.next = left.next.next
        return result.next
