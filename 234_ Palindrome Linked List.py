'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        for i in range(len(res)//2):
            if res[i]!=res[-i-1]:
                return False
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        mid = tail = head
        while tail and tail.next:
            tail = tail.next.next
            mid = mid.next

        node = None

        while mid:
            precedding = mid.next
            mid.next = node
            node = mid
            mid = precedding

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True