# 1,1,0
# 1,0,1
# 0,0,0
# 給一個2D 的長方形,1代表陸地,0代表水
# 告訴我有幾個陸地

#思考
# 1. 迴圈起始位置半段是否為陸地
# 2. 從陸地開始右下左上的延伸是否為同一塊
# 3. 跑完迴圈 告知有多少陸地

landmap = [[1,1,1,1,1],
           [1,0,0,0,1],
           [1,0,1,0,1],
           [1,0,0,0,1],
           [1,1,1,1,1]]

landStartNum,landEndNum = 10000,10000

def chkNear(landmap,x,y,landEndNum):
    if x>=0 and y>=0 and x<len(landmap) and y<len(landmap[0]) and landmap[x][y] == 1:
        landmap[x][y] = landEndNum
        chkNear(landmap, x + 1, y, landEndNum)
        chkNear(landmap, x, y + 1, landEndNum)
        chkNear(landmap, x - 1, y, landEndNum)
        chkNear(landmap, x, y - 1, landEndNum)

for i in range( len(landmap)):
    for j in range( len(landmap[0])):
        if landmap[i][j] == 1:
            landEndNum = landEndNum+1
            chkNear(landmap,i,j,landEndNum)
        if landmap[i][j] != 0:
            print(landmap[i][j]-landStartNum,end='\t')
        else:
            print(0,end='\t')
    print()

print("\t\t\t Land nums :",landEndNum-landStartNum)