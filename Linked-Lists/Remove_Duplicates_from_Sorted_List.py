class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head 
        while curr.next != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
        