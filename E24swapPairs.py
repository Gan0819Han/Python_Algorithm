# 两两翻转链表

# 辅助函数 0 ： 定义链表
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
    # print("None")


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 检查head的格式
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(next=head)
        current = dummy_head

        while current.next and current.next.next:
            temp = current.next
            temp1 = current.next.next.next

            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next

        return dummy_head.next

solution = Solution()
head = [1,2,3,4]

head = list_to_linkedlist(head)
head_reverse = solution.swapPairs(head)

print(f"{print_linkedlist(head_reverse)}")