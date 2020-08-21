
# ----------------------------------------------------------------
#
# 原題
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807
#
# Constraints: 約束條件
# ----------------------------------------------------------------
#
# 解釋題目:
# 2數相加, 但數字已顛倒的方式,用 link方式表示
# 如 342 + 465 = 807 / 342 => (2->4->3), 465 => (5->6->4) = 807 (7->0->8)
# ----------------------------------------------------------------
#
# 思維:
#
# ----------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pt1, pt2 = l1, l2
        newList = currpt = ListNode(0)
        carryOn = 0

        while pt1 or pt2 or carryOn:
            temp1 = pt1.val if pt1 else 0
            temp2 = pt2.val if pt2 else 0
            tempSum = temp1 + temp2 + carryOn

            carryOn = tempSum // 10
            currpt.next = ListNode(tempSum % 10)
            currpt = currpt.next

            if pt1:
                pt1 = pt1.next
            if pt2:
                pt2 = pt2.next
        return newList.next


num1 = ListNode(2)
num1.next = ListNode(4)
num1.next.next = ListNode(3)

num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)

a = Solution()
result = a.addTwoNumbers(num1,num2)
while result:
    print(result.val,end=" ->")
    result = result.next

