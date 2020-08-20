# 1,1,0
# 1,0,1
# 0,0,0
# 給一個2D 的長方形,1代表陸地,0代表水
# 告訴我有幾個陸地

#思考
# 1. 迴圈起始位置半段是否為陸地
# 2. 從陸地開始右下左上的延伸是否為同一塊
# 3. 跑完迴圈 告知有多少陸地

# 非常像 Leetcode 200題
# 在ASML 裡的考題中2D Array 是 int
# leetcode 200 輸入的Array 是 String, 要轉成 int.

# print(result)

# landmap = [[1,1,1,1,1],
#            [1,0,0,0,1],
#            [1,0,1,0,1],
#            [1,0,0,0,1],
#            [1,1,1,1,1]]

# 這是寫法1 原理是 DFS , 已改內容的方式, 不另外宣告 Stack 跟 瀏覽過的Set
# 若是要求 不能改島號 或是 另外宣告 Array 就只能寫成 標準的 DFS(有Stack 跟Set) 或 BFS(有Queue 跟Set)
class Solution:

    def numIslands(self, grid):

        ############################################################################
        def chkNear(landmap, x, y, landEndNum): #  class中的 小helper. 用來 recurtion.
            if x >= 0 and y >= 0 and x < len(landmap) and y < len(landmap[0]) and landmap[x][y] == 1:
                landmap[x][y] = landEndNum
                chkNear(landmap, x + 1, y, landEndNum)
                chkNear(landmap, x, y + 1, landEndNum)
                chkNear(landmap, x - 1, y, landEndNum)
                chkNear(landmap, x, y - 1, landEndNum)
        ############################################################################

        landmap = [list(map(int, i)) for i in grid]  # <- 將 2D String 改成 2D int

        landStartNum, landEndNum = 10000, 10000  # <- 設10000原因是 Array 中是用1與0代表地跟水
        # 我要改Array內容的地成島號, 但若島號表成1, 會分不清是 我改過的島號 還是原始的地
        # 所以起始值設 10000, 第一個島是 10001, 第2島是 10002 , 最後在問有幾個島時, 10002-10000=2 就是2個島

        for i in range(len(landmap)):
            for j in range(len(landmap[0])):
                if landmap[i][j] == 1:
                    landEndNum = landEndNum + 1
                    chkNear(landmap, i, j, landEndNum)
                if landmap[i][j] != 0:
                    print(landmap[i][j]-landStartNum,end='\t')  # print裡有預設值 end = '\n' 只要改掉 end 就會連著印,不會換行
                else:
                    print(0,end='\t')
            print()

        return landEndNum - landStartNum  # 結束島號-起始島號 = 有幾個島

############################################################################
landstr = ["11111", "10001", "10101", "10001", "11111"]
a = Solution()  # <- 正規的叫 class的方式 配合 leetcode.
print("the number of Islands:", a.numIslands(landstr))
