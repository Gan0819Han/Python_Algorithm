# Python 数据结构与算法练习

这是一个记录 Python 数据结构与算法练习的项目。每个文件对应一个算法问题的实现，涵盖了数组、链表、字符串、哈希表、双指针、滑动窗口等多种数据结构与算法的练习。持续更新。

## 目录

### 数组
- **E1twoSum.py**：解决两数之和问题，找到数组中和为目标值的两个数的索引。
- **E15threeSum.py**：解决三数之和问题，找到数组中所有和为零的三元组。
- **E18fourSum.py**：解决四数之和问题，找到数组中所有和为目标值的四元组。
- **E26removeDuplicates.py**：删除有序数组中的重复项，使每个元素只出现一次。
- **E27removeElement.py**：移除数组中的特定元素，返回移除后的数组长度。
- **E28strStr.py**：实现字符串的查找，返回子串在主串中的位置。
- **E34searchRange.py**：查找目标值在数组中的起始和结束位置。
- **E35insert.py**：在有序数组中插入一个元素，保持数组有序。
- **E344reverseString.py**：反转字符串。
- **E349intersection.py**：计算两个数组的交集。
- **E350intersection.py**：计算两个数组的交集（考虑重复元素）。
- **E367isPerfectSquare.py**：判断一个数是否为完全平方数。
- **E383canConstruct.py**：判断一个字符串是否可以由另一个字符串的字符拼接而成。
- **E438findAnagrams.py**：找到字符串中所有字母异位词的位置。
- **E454fourSumCount.py**：计算满足四数之和为零的组合数量。
- **E459repeatedSubstringPattern.py**：判断一个字符串是否可以通过另一个字符串重复拼接而成。
- **E541reverseStr.py**：反转字符串的奇数位置。
- **E704search.py**：在有序数组中查找目标值。
- **E707defineListNode.py**：定义链表节点类（虽文件名有“ListNode”，但实际是数组相关）。
- **E844backspaceCompare.py**：比较两个字符串是否相等，考虑退格操作。
- **E904totalFruit.py**：计算最多可以收集的水果数量。
- **E977sortedSquares.py**：对有序数组的平方进行排序。
- **E1047removeDuplicates.py**：删除字符串中的重复字符。

### 链表
- **E19removeNthFromEnd.py**：删除链表中倒数第 n 个节点。
- **E20isVaild.py**：判断链表是否为有效的括号序列（可能是文件名错误，实际应为字符串相关）。
- **E24swapPairs.py**：交换链表中每两个相邻节点。
- **E142detectCycle.py**：检测链表中是否存在环。
- **E203removeElements.py**：移除链表中的特定元素。
- **E206reverselist.py**：反转链表。
- **E232myQueue.py**：使用链表实现队列。
- **E707defineListNode.py**：定义链表节点类。
- **ListNode_pre.py**：链表相关操作的前置代码或辅助函数。

### 字符串
- **E151reverseWord.py**：反转字符串中的单词。
- **E202isHappy.py**：判断一个数是否为快乐数（虽文件名有“isHappy”，但实际是字符串相关）。
- **E283moveZeroes.py**：将数组中的零移动到末尾（虽文件名有“moveZeroes”，但实际是字符串相关）。
- **E49groupAnagrams.py**：将字符串数组中的字母异位词分组。
- **E242isAnagram.py**：判断两个字符串是否为字母异位词。
- **E54_1spiralOrder.py**：按螺旋顺序打印矩阵（虽文件名有“spiralOrder”，但实际是字符串相关）。
- **E54_2generateMatrix.py**：生成螺旋矩阵（虽文件名有“generateMatrix”，但实际是字符串相关）。
- **E69mySqrt.py**：计算一个数的平方根（虽文件名有“mySqrt”，但实际是字符串相关）。
- **E76minWindow.py**：找到包含目标字符串的最小窗口。
- **E150evalRPN.py**：计算逆波兰表达式的值。
- **E209minSubArraylen.py**：找到最小子数组长度，使其和大于等于目标值。
- **E239maxSlidingWindow.py**：计算滑动窗口的最大值。
- **E349intersection.py**：计算两个字符串的交集。
- **E350intersection.py**：计算两个字符串的交集（考虑重复元素）。
- **E438findAnagrams.py**：找到字符串中所有字母异位词的位置。
- **E454fourSumCount.py**：计算满足四数之和为零的组合数量。
- **E459repeatedSubstringPattern.py**：判断一个字符串是否可以通过另一个字符串重复拼接而成。
- **E541reverseStr.py**：反转字符串的奇数位置。
- **E704search.py**：在字符串中查找目标值。
- **E844backspaceCompare.py**：比较两个字符串是否相等，考虑退格操作。
- **E904totalFruit.py**：计算最多可以收集的水果数量。
- **E977sortedSquares.py**：对字符串的平方进行排序。
- **E1047removeDuplicates.py**：删除字符串中的重复字符。
- **KMP.py**：实现 KMP 算法，用于字符串匹配。

## 使用方法
每个文件都包含一个独立的算法实现，可以直接运行并测试。部分文件可能依赖于其他文件中的类或函数，例如链表相关文件可能依赖于 `ListNode_pre.py` 中的定义。

## 项目结构
```
Algorithm_Exercise/
├── E1twoSum.py
├── E15threeSum.py
├── ...
├── KMP.py
└── ListNode_pre.py
```

## 贡献
欢迎提交新的算法实现或改进现有代码。请遵循以下步骤：
1. 叉这个仓库。
2. 创建一个新的分支。
3. 提交你的更改。
4. 提交一个 Pull Request。

## 致谢
感谢所有为这个项目做出贡献的人。
