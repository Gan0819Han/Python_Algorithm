# 面试题目：链表相交
# 辅助函数 0 ：定义链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 辅助函数 1 ：将列表转换为链表
def list_to_linkedlist(lst):
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# 辅助函数 2 ： 打印链表
def print_linkedlist(lst):
    current = lst
    while(current):
        print(current.val,end=" -> ")
        current = current.next
    print("None")
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA 
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next 
            
        while(curA):
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next   
                     
        return None

headA = [1,2,3,4,5,6,7]
headB = [0,9,8,9,3,4,5,6,7]

headA = list_to_linkedlist(headA)
headB = list_to_linkedlist(headB)
solution = Solution()
print_linkedlist(solution.getIntersectionNode(headA,headB))