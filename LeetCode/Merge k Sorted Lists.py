# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        temp = None

        x = []
        for i in lists:
            while i!=None:
                x.append(i.val)
                i = i.next
        
        x.sort()
        for i in x:
            if head == None:
                head = ListNode(i)
                temp = head
            else:
                temp.next = ListNode(i)
                temp = temp.next
        
        return head

        
        # while True:
        #     m = {'isComplete': 0}
        #     i = 0
        #     for item in lists:
        #         if 'min' not in m and item != None:
        #             m['min'] = item.val
        #             m['index'] = i
        #         elif item != None:
        #             if m['min'] > item.val:
        #                 m['min'] = item.val
        #                 m['index'] = i
        #         else:
        #             m['isComplete'] = m['isComplete'] + 1
        #         i += 1
            
        #     if m['isComplete'] == len(lists):
        #         break
            
        #     if head == None:
        #         head = ListNode(m['min'])
        #         temp = head
        #     else:
        #         temp.next = ListNode(m['min'])
        #         temp = temp.next
            
        #     lists[m['index']] = lists[m['index']].next

        # return head