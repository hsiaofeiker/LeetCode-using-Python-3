# Google
# ----------------------------------------------------------------
# 快速檢索特性:
#
# ----------------------------------------------------------------
#
# 原題
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# Return the minimum number of rotations so that all the values in A are the same,
# or all the values in B are the same.
# If it cannot be done, return -1.
# Example 1:
# Input: A = [2,1,2,4,2,2]
#        B = [5,2,6,2,3,2]
# Output: 2
# Explanation: The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
# as indicated by the second figure.
# AB Array, 位置 1 跟 位置 3, 上下旋轉2次, 就能造成一排的2
#
# Example 2:
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
# 不管再怎轉, 都不能造成某一排有相同數,所以回傳-1
#
# Constraints: 約束條件
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# ----------------------------------------------------------------
#
# 解釋題目:
# Array A 跟 B 代表 domino多米諾骨牌的上下半的 2數字, 數字介於 1~6,  Array 的長度介於 2 ~20000
# A 跟 B 可以對調, 表示上下翻轉, 目標使 上一排,或下一排 的數字相同
# 回傳最小的 選轉次數, 若怎轉都不能湊成一排, 則回傳-1
# ----------------------------------------------------------------
#
# 思維:
# 我的解法 應該不是正統,但卻能快速解開此題
# 正常來說, dominoes 牌有1~6數字,要掃6個數字
# 但是若以第一張牌來看,若上2下5, 表示能排成一條線的數字非2即5, 就不用去掃6個數字,快速省下時間.
# 若搜尋的過程中, 某牌的上下數字 不等於 A[0]也不等於 B[0], 表示數字沒有無法湊成連續的一排,表示不用Rotate.後面就不用做
# 以底下數值 來看, 假設正確值是2, 最後判斷到底要轉幾回...
# A = [2, 1, 2, 4, 2, 2]
# B = [5, 2, 6, 2, 3, 2]
# 若計算上方有幾個2, 上方是4個, 若計算下方有幾個2, 下方是3個,會有困擾
# 但若直接計算有幾個不是 2, 上方是2, 下方是3, 表示轉2次即可
# 這想法來自 莊家玩3張蓋牌,一開始是 2K 1A, 但一蓋牌時,裡面全是3K, 若問,哪一張是A,翻任一張都是猜錯
# 但,若你選,哪兩張是 K , 隨便開都是K, 剩下的那張,雖是K,但沒翻,都必當作A.否則就抓到莊家出老千
# 邏輯 就是借用 不是2 (不是A) 就可知 要轉幾次, 不會被現有有幾個2 混淆
# ----------------------------------------------------------------

class Solution:
    # 直接暴力解..就行了
    # 先抓 A[0],B[0] Ex:(2,5)
    # 再抓 A[1],B[1] Ex:(1,2)
    # A = [2, 1, 2, 4, 2, 2]
    # B = [5, 2, 6, 2, 3, 2]
    # 可能的數字,不是2就是5, 所以就預設兩個possibleNumA,possibleNumB表示A[0],B[0]
    # 若搜尋的過程中, 有數字 不屬於 A[0]且 B[0], 表示數字沒有連續,不用Rotate.
    # 若搜尋的過程中, 有數字 不屬於 A[0]或 B[0], 表示數字一定是在A[0]或B[0],在不是時,把possibleNum設為-1.
    # 最後計算找幾次,從A頭跑到A尾,B頭跑到B尾, 看不是possible Num 的有幾個就是表示Rotate 幾次
    # 解釋:
    # A = [2, 1, 2, 2] --> 若看2 有幾次, A是3次,B欄是2次, 若看不是2的有幾次,A欄是1次,B欄是2次,表示只要轉1次
    # B = [5, 2, 3, 2]
    def minDominoRotations(self, A: list, B: list) -> int:

        if len(A) != len(B):    #dominoes牌,AB列應該同長, 若不同長度,就是錯
            return -1
        if len(A) <= 1:         #若只有一張dominoes牌, 那,連 旋轉都不用旋轉,直接回傳 0次
            return 0

        aLive = True  # aLive 是用來表示 A[0] Domino牌 上方的數字是否是正確可排成一列的數字
        bLive = True  # bLive 是用來表示 B[0] Domino牌 下方的數字是否是正確可排成一列的數字
        #只要上下方其中一個數字 跟後面的值不同,有不同,表示就不是上面或下面的數
        #若上下都不是,表示斷掉,無法成為一排.表示不用旋轉,回傳-1

        possibleNumA = 7    #牌上方可能的數字是1~6,預設值只要不是1~6即可
        possibleNumB = 7    #牌下方可能的數字是1~6,預設值只要不是1~6即可
        for i in range(0, len(A)):
            if aLive or bLive:
                if i == 0:
                    possibleNumA = A[0]
                    possibleNumB = B[0]
                else:
                    if possibleNumA != -1:
                    # 如果A[0]上方數,不等於後面的 上方也不等於下方數,表示A[0]絕對不是正確可成一排的數字
                    # 換句話說,若等於i位的上方或下方,就繼續保持 這可能是正確值
                        if A[0] != A[i] and A[0] != B[i]:
                            possibleNumA = -1   #-1表示
                            aLive = False

                    if possibleNumB != -1:
                    # 如果B[0]下方數,不等於後面的 上方也不等於下方數,表示B[0]絕對不是正確可成一排的數字
                    # 換句話說,若等於i位的上方或下方,就繼續保持 這可能是正確值
                        if B[0] != A[i] and B[0] != B[i]:
                            possibleNumB = -1
                            bLive = False

            if aLive == False and bLive == False:  # 如果同時 上下可能值都是False, 表示不連續,直接回傳-1
                return -1
        #print('A', possibleNumA, 'B', possibleNumB) #印出可能可以排成一列的數字, -1表示不對的數
        # 能執行到這,表示上值或下值 其一 一定是對的值,要不就其二. 1~6跟-1比, 大的值就是1~6內,也就是正確的數
        possibleNum = max(possibleNumA, possibleNumB)

        topCunt = 0 # 計算上方有幾個不是正確值
        btmCunt = 0 # 計算上方有幾個不是正確數
        # 以底下數列來看, possibleNum是 2.
        # A = [2, 1, 2, 4, 2, 2]
        # B = [5, 2, 6, 2, 3, 2]
        # 計算 上方A有多少個不是2, 或是下方B有多少個不是2.
        # 上面A有2個 不是2, 下方B 有3個不是2, 取最小.表示 只要把不是2次的那2位置旋轉,就可以湊成一列
        for i in range(len(A)):
            if A[i] != possibleNum:
                topCunt = topCunt + 1
            if B[i] != possibleNum:
                btmCunt = btmCunt + 1
        return min(topCunt, btmCunt)

A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]

a = Solution()
print( a.minDominoRotations(A,B) )