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
    