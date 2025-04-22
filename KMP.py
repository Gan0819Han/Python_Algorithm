# 尝试写一写KMP算法的实现
# KMP算法原理

# KMP算法的代码实现
# ★next[]数组的实现

def calculateNext(lst):
    """
    lst(->str): 传入"模式串"用于求其Next数组
    """
    n = len(lst)
    next = [0] * n
    j = 0
    # 遍历模式串
    for i in range(1,n):
        # 定义next数组的起始数是0

        # 求解剩下部分的最小相等前缀
        while(lst[j]!=lst[i] and j > 0):
            j = next[j-1]
        if(lst[j]==lst[i]):
            j += 1
        next[i] = j

    return next

# 测试
pattern = "abcdcdab"
next_array = calculateNext(pattern)
print("模式串:", pattern)
print("Next数组:", next_array)

# 如何调用可以看  E28.py

# 在类中的定义如下
def calculateNext(self,next,lst):
    """
    next(->(List[int])): 传入用于记录NEXT数组
    lst(->str): 传入"模式串"用于求其Next数组
    """
    n = len(lst)
    j = 0
    # 遍历模式串
    for i in range(1,n):
        # 定义next数组的起始数是0

        # 求解剩下部分的最小相等前缀
        while(lst[j]!=lst[i] and j > 0):
            j = next[j-1]
        if(lst[j]==lst[i]):
            j += 1
        next[i] = j
