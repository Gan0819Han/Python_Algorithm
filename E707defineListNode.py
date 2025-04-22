# 对链表的一系列操作
class ListNode():
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
        
class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head.next
        # 遍历到第index的元素
        for i in range (index):
            current = current.next
            
        return current.val
            

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val,self.dummy_head.next)
        self.size += 1
        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummy_head
        while (current.next):
            current = current.next
        current.next = ListNode(val)
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head
        for i in range (index):
            current = current.next
        current.next = ListNode(val,current.next)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head
        for i in range (index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# 打印链表的辅助函数
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# 实例化链表对象
my_linked_list = MyLinkedList()

# 在链表头部添加节点
my_linked_list.addAtHead(1)
print("链表状态：", end=" ")
print_linkedlist(my_linked_list.dummy_head.next)

# 在链表尾部添加节点
my_linked_list.addAtTail(3)
print("链表状态：", end=" ")
print_linkedlist(my_linked_list.dummy_head.next)

# 在指定索引处添加节点
my_linked_list.addAtIndex(1, 2)
print("链表状态：", end=" ")
print_linkedlist(my_linked_list.dummy_head.next)

# 获取指定索引处的节点值
value = my_linked_list.get(1)
print(f"索引 1 处的节点值：{value}")

# 删除指定索引处的节点
my_linked_list.deleteAtIndex(1)
print("链表状态：", end=" ")
print_linkedlist(my_linked_list.dummy_head.next)

# 再次获取指定索引处的节点值
value = my_linked_list.get(1)
print(f"索引 1 处的节点值：{value}")