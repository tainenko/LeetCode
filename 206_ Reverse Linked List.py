'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head=None
        while head:
            p=head
            head=head.next
            p.next=new_head
            new_head=p
        return new_head
class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst=[]
        p=head
        while p:
            lst.insert(0,p.val)
            p=p.next
        p=head
        for v in lst:
            p.val=v
            p=p.next
        return head


class Solution3:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_list