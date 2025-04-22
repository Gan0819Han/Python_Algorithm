# 删除列表的倒数第n个元素
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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        slow = fast = dummy_head
        step = n + 1
        while(step != 0):
            fast = fast.next
            step -= 1
            
        while(fast != None):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        while(slow != None):
            slow = slow.next
            
        return dummy_head.next
    
head = [1,2,3,4,5]
n = 2

head_linked = list_to_linkedlist(head)
print_linkedlist(head_linked)
solution = Solution()
head_linked_processed = solution.removeNthFromEnd(head_linked,n)
print_linkedlist(head_linked_processed)
            