# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def createResult(self, res, ind):
        if len(res) == ind + 1:
            return ListNode(res[ind], None)
        return  ListNode(res[ind], self.createResult(res, ind+1))
        


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        carry = 0
        i = 0
        data1 = l1
        data2 = l2
        while data1 != None or data2 != None:
            sum_value =  (data1.val if data1 != None else 0)  + (data2.val if data2 != None else 0) + carry
            if sum_value >= 10:
                sum_value = sum_value % 10
                carry = 1
            else:
                carry = 0
            
            res.append(sum_value)
            i = i+1
            data1 = (data1.next if data1 != None else None)
            data2 = (data2.next if data2 != None else None)

        if carry != 0:
            res.append(carry)
        return self.createResult(res, 0)