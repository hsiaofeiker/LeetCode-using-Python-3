# Google
# ----------------------------------------------------------------
# 快速檢索特性:
#
# ----------------------------------------------------------------
# 原題
# Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing
# zero or more conversions.
# In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
# Return true if and only if you can transform str1 into str2.
#
# Example 1:
# Input: str1 = "aabcc", str2 = "ccdee"  /  Output: true
# Explanation: Convert 'c' to 'e'.
# then 'b' to 'd'
# then 'a' to 'c'. Note that the order of conversions matter.
#
# Example 2:
# Input: str1 = "leetcode", str2 = "codeleet" /  Output: false
# Explanation: There is no way to transform str1 to str2.
# Note:
# 1 <= str1.length == str2.length <= 10 ^ 4
# Both str1 and str2 contain only lowercase English letters.
# ----------------------------------------------------------------
#
# 解釋題目:
# 給定兩個長度相同的字符串str1和str2，通過執行轉換 操作確定是否可以將str1轉換為str2 零次或多次轉化。
# 在一次轉換中，您可以將出現在str1中的一個字符的所有出現轉換為其他任何小寫英文字符。
# 當且僅當您可以將str1轉換為str2時，才返回true。
# Str1:"aabcc"轉成Str2:"ccdee"? 若一開始把a轉成 c, Str1就會變成ccbcc 就會產生問題
# 但要是從 c->e 開始 aabee-> aadee-> ccdee 就能轉換成功
# 也就是說...英文字母小寫能換得首要,就是 26個中最多只能 25個字,不能全滿都在 Str2裡
# 若是全26字都有, 要是 Str1 等於 Str2 就轉換0次 也符合 程式所需.
# 這是在考 這一步是否會卡下一步的問題.
# ----------------------------------------------------------------
#
# 思維:

# ----------------------------------------------------------------
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(set(str2))
        if m == 26:
            return str1 == str2

        d = {}
        for i, c in enumerate(str1):
            if c in d:
                if d[c] != str2[i]:
                    return False
            else:
                d[c] = str2[i]
        return True

a = Solution()
str1='aabcc'
str2='ccdee'
print( a.canConvert(str1,str2) )