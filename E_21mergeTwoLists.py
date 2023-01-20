class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def mergeTwoLists(self, list1: List[ListNode], list2: List[ListNode]) -> List[ListNode]:
        # create a node point to result
        head = ListNode()
        result = head
        
        # compare the first ele in two lists, append smaller one
        while list1 and list2:
            # list 1 < list 2
            if list1.val < list2.val:
                # add the smaller node to result
                result.next = list1
                # remove the added node
                list1 = list1.next 
            # list 2 <= list 1
            else:
                # add the smaller node to result
                result.next = list2
                # remove the added node
                list2 = list2.next
            result = result.next
        # if len(list1) > len(list2)
        if list1:
            result.next = list1
        # if len(list2) > len(list1)
        elif list2:
            result.next = list2

        return head.next
