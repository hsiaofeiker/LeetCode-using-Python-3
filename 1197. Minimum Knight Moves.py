# Google
# ----------------------------------------------------------------
# 快速檢索特性:
# DP Dynamic Programming (動態規劃) / BFS Breadth-First Search 廣度優先
# dictionary/Hash map (使用Dictionary 比 2D Array 快)
# 2D array in Dictionary -> 變數chessBoard 使用Dictionary, 是因為搜尋起來會比2D Array快很多.
# Queue -> 變數fifoQue 用來儲存(x,y) 衍伸出來的8方向點, 變數currentValueQue用來儲存(x,y) 衍伸出來的8方向點預設值
# ----------------------------------------------------------------
#
# 原題
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square[0, 0].
# A knight has 8 possible moves it can make, as illustrated below.Each move is two squares in a cardinal direction,
# then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square[x, y].It is guaranteed the answer exists.
# Example 1:
# Input: x = 2, y = 1 / Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:
# Input: x = 5, y = 5 / Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
# Constraints: 約束條件
# | x | + | y | <= 300
# ----------------------------------------------------------------
#
# 解釋題目:
# 西洋棋盤大小是|x|+|y|<= 300.西洋棋騎士日字走法,走的路徑方向有8種.
# 起始位置在 (0,0) ,走到預設位置 (x,y), 回傳最短步數.
# ----------------------------------------------------------------
#
# 思維: 這種題 解法應該是 BFS 跟 DP.
# 在速度上,跟記憶體上要把 範圍再縮小才能更快, 第41~53行 有解釋
# ----------------------------------------------------------------
import queue

def minKnightMoves(x: int, y: int) -> int:

    # 騎士日字走法的8方向
    directionX=[+2,+1,-1,-2,-2,-1,+1,+2]    # ( 4點) +2, +1  (5點) +1, +2 (7點)-1, +2  (8點)-2, +1
    directionY=[+1,+2,+2,+1,-1,-2,-2,-1]    # (10點)-2, -1   (11點)-1, -2 (1點)+1, -2  (2點)+2, -1

    # 題目 說 邊界範圍在 abs(x)+abs(y)<=300,
    # 原始做法最懶, 若把 -300 ~ +300 x -300~300 設下去, 則記憶體上會佔600x600的尺寸,速度上也慢
    # 若以x,y正負來分 4相限, 300x300,記憶體上會是以 原始做法的 1/4, 當然速度也會快些
    # 但是若仔細研究 日字走法.
    #       (4,5)
    #(0,0)
    #其實界線,只要設 比最大x值+2 ,最小x值 0-2,最大y值+2,最小y值-2 , 即 ( x:-2~6, y:-2~7 )
    #這樣一來, 記憶體用的少,速度也快,所以,寬度上ws~wb, 高度上hs~hb
    # 宣告
    ws = min(0, x)-2 # 橫向寬度 +300~-300
    wb = max(0, x)+2
    hs = min(0, y)-2 # 縱向寬度 +300~-300
    hb = max(0, y)+2
    # 變數chessBoard 使用dictionary儲存方式, 專記錄走幾步會到這點.
    # 將 -300~300 的矩形點(橫向jw, 縱向ih) 預設值都設為-1

    chessBoard = dict(((j, i), -1) for i in range(hs,hb) for j in range(ws,wb))
    fifoQue = queue.Queue()         # 用於儲存現在(x,y)衍伸出來的8個方向點(x,y)
    currentValueQue = queue.Queue() # 用於儲存現在(x,y)衍伸出來的8個方向點的預設值

    # 預設值
    chessBoard[(0, 0)] = 0  # 修改記憶艇中 騎士出發位置 (0,0) 的對映值 0步 / 沒走過的都是-1
    fifoQue.put((0, 0))             # 騎士出發位置 (0,0)
    currentValueQue.put(0)          # 騎士出發位置 (0,0) 所以到這位置是0步

    currentX = 0  # x 橫向軸
    currentY = 0  # y 縱向軸

    # 方式1:while迴圈中 若 qsize 大於0 , 表示 Que裡還有沒處理完的點,有可能棋盤沒全走完,
    # 方式2:另一種while寫法是 沒找到傳進來要搜尋點的(x,y)就繼續找. 找到就停止
    # 方式3:另一種while寫法是 dictionary 有 -1 就繼續
    #while fifoQue.qsize()>0:   #方式1:
    while -1 in chessBoard.values():

        (currentX,currentY)=fifoQue.get()   # Queue裡取得這次要處理的(x,y)點
        currentValue=currentValueQue.get()  # (x,y)點的預設值

        #利用 for 迴圈, 走衍申的8方向
        #從 Queue裡 取得的(x,y)點衍伸出來的8方向跟值, (x,y)放入fifoQue, 值放入currentValueQue
        for i in range(8):
            tmpX = currentX + directionX[i] # 8方向的暫存X軸
            tmpY = currentY + directionY[i] # 8方向的暫存Y軸

            # chessBoard(x,y)若不等於-1,表示之前曾走過了(應有更小值),不須重複走過該點.
            if tmpX>=ws and tmpX<wb and tmpY>=hs and tmpY<hb and chessBoard[(tmpX,tmpY)]==-1:
                chessBoard[(tmpX, tmpY)] = currentValue + 1 # 修改dictionary裡的值,表示 告知未來的拜訪,現在這點走過.
                fifoQue.put((tmpX, tmpY))                   # 該點延伸出的8點(x,y),放入 Queue 待處理區
                currentValueQue.put(currentValue + 1)       # 該點延伸出的8點(x,y)的值,放入 Queue 待處理區

            #if tmpX==x and tmpY ==y: break
        #print(chessBoard.values())  # 看每次Dictionary的chessBoard棋盤 值 被改變
    #print(chessBoard.values())     # 看最後一次Dictionary 的chessBoard棋盤的終值被改變
    return chessBoard[(x,y)]    # chessBoard 裡專記錄走幾步會到這點.

targetX=5
targetY=4
print(minKnightMoves(targetX,targetY))