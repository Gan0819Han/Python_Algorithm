# 反转链表 ： 双指针法
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        pre = None
        while(cur):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre # 反转
            # 更新pre、cur指针
            pre = cur
            cur = temp
        return pre
    
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
    
# 实例化并使用
# 创建链表
lst = [1, 2, 3, 4, 5]
head = list_to_linkedlist(lst)

# 打印原始链表
print("原始链表：")
print_linkedlist(head)

# 实例化 Solution 类
solution = Solution()

# 反转链表
reversed_head = solution.reverseList(head)

# 打印反转后的链表
print("反转后的链表：")
print_linkedlist(reversed_head)
# 打印.next (?)
