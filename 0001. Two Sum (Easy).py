# Google
# ----------------------------------------------------------------
# 快速檢索特性:
# class Solution: 寫法 , 底下主程式部分要 a = Solution() , 然後再呼叫 a.twoSum(x,y)...
# 變數difference in nums(Array) 這樣沒有此數,並不會出現Error.
# nums.index(某數) -> 直接回傳 Array中的位置
# ----------------------------------------------------------------
#
# 原題
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example 1:
# Given nums = [2, 7, 11, 15], target = 9,
# Output [0, 1]
# Explanation: Because nums[0] + nums[1] = 2 + 7 = 9,
# Constraints: 約束條件
# ----------------------------------------------------------------
#
# 解釋題目:
# Array中的 2數在相加 等於 目標值, 回傳這2數在 Array中的位置,
# 一定有解,且不會用同一數2次
# ----------------------------------------------------------------
#
# 思維:
# 這種題 解法就直接使用 內建函數,跟暴力解
# 空間0, 時間 O(n)
# ----------------------------------------------------------------
class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        for i in range(len(nums)):

            differce = target - nums[i]
            # 變數 difference = 目標值 - 第i位數,
            # 然後直接搜尋是否有這個 difference差值, 且這個difference在Array的位置,不能等於i位
            # 成立的話,回傳, 不成立,i換下一位再試看看
            if differce in nums and nums.index(differce) != i:
                return [i, nums.index(differce)]

numbers=[2,2,7,11,15]
target = 4
a = Solution()
print( a.twoSum(numbers,target) )