# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# This part is given.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# You have to write your own function.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        checker1 = l1
        checker2 = l2
        while checker1 != None:
            l1_list.append(checker1.val)
            checker1 = checker1.next
        while checker2 != None:
            l2_list.append(checker2.val)
            checker2 = checker2.next
        first_num = ''.join([str(num) for num in l1_list])
        second_num = ''.join([str(num) for num in l2_list])
        final_num = int(first_num[::-1]) + int(second_num[::-1])
        final_str = str(final_num)[::-1]
        linked_node = ListNode(int(final_str[0]))
        pointer = linked_node
        for num in final_str[1:]:
            pointer.next = ListNode(int(num))
            pointer = pointer.next
        return linked_node
