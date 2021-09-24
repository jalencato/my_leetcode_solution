from collections import Counter

c = Counter('abcasd')
print(sorted(c))
#prefix product suffix product

#bucket sort

#reverse linklist
def ReverseList(self, pHead):
    if not pHead or not pHead.next:
        return pHead
    last = None
    while pHead:
        tmp = pHead.next
        pHead.next = last
        last = pHead
        pHead = tmp
    return last

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            #find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None

            # reverse linked list head2
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next

            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2

# 单调栈

# 左右侧边界

# bst 中序是有序的

import heapq # 注意是 小顶堆 噢～

import copy
h = copy.copy(origin_list)
heapq.heapify(h)

h = []
for item in origin_list:
    heapq.heappush(h, item)

def partition(arr,low,high):
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]

    for j in range(low , high):

        # 当前元素小于或等于 pivot
        if   arr[j] <= pivot:

            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1], arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

answer[i] = answer[i >> 1] + (i & 1)

def findKthLargest(self, nums, k):
    pivot = random.choice(nums)
    nums1, nums2 = [], []
    for num in nums:
        if num > pivot:
            nums1.append(num)
        elif num < pivot:
            nums2.append(num)
    if k <= len(nums1):
        return self.findKthLargest(nums1, k)
    if k > len(nums) - len(nums2):
        return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
    return pivot

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []

    def get(self, key: int) -> int:
        for i, tup in enumerate(self.data):
            if tup[0] == key:
                values = tup
                self.data.pop(i)
                self.data.append(values)
                return values[1]

        return -1

    def put(self, key: int, value: int) -> None:
        did_put = False
        for i, tup in enumerate(self.data):
            if tup[0] == key:
                did_put = True
                self.data.pop(i)
                self.data.append((key, value))
        if not did_put:
            self.data.append((key, value))
        if len(self.data) > self.capacity:
            self.data.pop(0)

import random
def func(arr):
    n = len(arr)
    rem = n
    for i in range(n):
        p = random.randint(1, rem)  # randint的随机范围是[a,b]闭区间
        arr[p-1], arr[rem-1] = arr[rem-1], arr[p-1]
        rem -= 1
    return arr

import re
result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip)

def numDecodings(self, s: str) -> int:
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        if int(s[i-1]) != 0:
            dp[i] = dp[i-1]
        if i != 1 and '09' < s[i-2:i] < '27':
            dp[i] += dp[i-2]
    return dp[-1]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in xrange(rows / 2):
                for j in xrange(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in xrange(rows):
                for j in xrange(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

import bisect

a = [1,4,6,8,12,15,20]
position = bisect.bisect(a,13)

def chinesetoint(self,  strs):
    if strs == "":
        return None
    dicts = {"一":1, "二":2, "三": 3, "四": 4, "五": 5, "六":6, "七":7, "八":8, "九":9, "十": 10, "百":100, "千":1000, "万":10000}
    strs = strs.replace("零", "")
    lists = [0] * (len(strs) + 1)
    nums = 0
    for i in range(len(strs)):
        lists[i] = int(dicts.get(strs[i], -1))
        # 首先判定除了第0个元素外，其他元素的数值是否大于10
        if i !=0 and lists[i] >= 10:
            if lists[i-1] < 10:
                nums += lists[i] * lists[i-1] - lists[i-1]
            else:
                nums = nums * lists[i]
        else:
            nums += lists[i]

class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        resultList = []
        nums.sort()
        for i in range(0,length-2):
            j = i + 1
            k = length - 1
            while (j < k):
                sum0 = nums[i] + nums[j] + nums[k]
                if (sum0 == 0):
                    result = []
                    result.append(nums[i])
                    result.append(nums[j])
                    result.append(nums[k])
                    if result not in resultList:
                        resultList.append(result)
                    j +=1
                if (sum0 < 0):
                    j +=1
                if (sum0 > 0):
                    k -=1
        return resultList

    class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            print(s)
            print(wordDict)
            dp = [False] * (len(s) + 1)
            dp[0] = True
            print(dp)
            for i in xrange(1, len(s) + 1):
                for k in xrange(i):
                    if dp[k] and s[k:i] in wordDict:
                        dp[i] = True
                        print(dp)
            return dp.pop()

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        win = defaultdict(int)
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1

        # 定义指针
        left = 0
        right = 0
        # 初始化最小长度
        min_len = float('inf')

        # chr_count 用以表示滑动窗口包含字符数
        chr_count = 0
        # 最小子串起始位置
        begin = 0
        # s 长度
        s_len = len(s)
        # t 长度
        t_len = len(t)

        while right < s_len:
            # 移动窗口，
            if t_dict[s[right]] == 0:
                right += 1
                continue
            # 滑动窗口包含 T 字符数，当超过 T 其中字符个数时不在增加
            if win[s[right]] < t_dict[s[right]]:
                chr_count += 1

            win[s[right]]+=1
            right+=1

            # 当窗口包含 T 所有的字符时，缩小窗口
            while chr_count == t_len:
                # 这里更新子串的起始位置和长度
                if right-left < min_len:
                    begin = left
                    min_len = right - left
                # 缩小窗口
                if t_dict[s[left]] == 0:
                    left += 1
                    continue
                # 这里表示出窗时，窗口所包含 T 的字符刚好等于 T 中字符的个数
                # 这个时候再移动，窗口就不满足包含 T 所有字符的条件
                # 这里 chr_count - 1 ，循环结束
                if win[s[left]] == t_dict[s[left]]:
                    chr_count -= 1

                win[s[left]]-=1
                left += 1

        return "" if min_len == float('inf') else s[begin:begin+min_len]