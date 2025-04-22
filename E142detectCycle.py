# 环形链表
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(next=head)
        slow = fast = dummy_head.next
        slow_step = 0
        fast_step = 0
        
        # 先走一步
        # fast = fast.next.next
        # slow = slow.next
        # fast_step += 1
        # slow_step += 1
        
        # 先让fast一直跑
        while(fast and fast.next):
            fast = fast.next.next
            fast_step += 1
            slow = slow.next
            slow_step += 1
            
            #  是否追上了
            if fast==slow:
                # 让slow回到起点
                slow = dummy_head.next
                while(fast!=slow):
                    fast = fast.next
                    slow = slow.next
                return slow

        return None
 
    
# 创建链表
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
head = list_to_linkedlist(lst)

# 找到节点 3 和节点 15
current = head
node_3 = None
node_15 = None

while current:
    if current.val == 3:
        node_3 = current
    if current.val == 15:
        node_15 = current
        break
    current = current.next

# 创建环：让节点 15 的 next 指向节点 3
if node_3 and node_15:
    node_15.next = node_3

solution = Solution()
print(print_linkedlist(solution.detectCycle(head)))