# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy_head.next

# 辅助函数：将列表转换为链表
def list_to_linkedlist(lst):
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# 辅助函数：打印链表
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# 测试代码
solution = Solution()
head = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
val = 3

# 将列表转换为链表
linked_list_head = list_to_linkedlist(head)

# 调用函数删除指定值的节点
result_head = solution.removeElements(linked_list_head, val)

# 打印结果链表
print("结果链表：")
print_linkedlist(result_head)
print(f"{result_head}")