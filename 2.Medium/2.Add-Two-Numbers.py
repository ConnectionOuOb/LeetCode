"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Initial
        add1 = 0
        RETs = ListNode()
        Swap = RETs

        # Ietrate all elements
        while l1 != None or l2 != None or add1 != 0:
            # Get now value
            n1 = l1.val if l1 != None else 0
            n2 = l2.val if l2 != None else 0

            # Sum
            ll = n1 + n2 + add1

            # Set next value
            Swap.next = ListNode(ll % 10)
            add1 = ll // 10

            # Go next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            Swap = Swap.next

        return RETs.next


if __name__ == "__main__":
    s = Solution()
    s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))),
                    ListNode(5, ListNode(6, ListNode(4))))
    s.addTwoNumbers(ListNode(0), ListNode(0))
    s.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(
        9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
