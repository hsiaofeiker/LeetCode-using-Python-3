# google interview 2
# There's a Matrix N x M. Each cell is a number.
# Write two functions setValue and sum.
# setValue will be pass in x, y and Value.
# sum function will be pass in x1,x2,y1,y2 and sum the items between those two point.
# setValue(x1,y1,value) 在指定的 x,y位置上,填入數值
# sum(x1,x2,y1,y2) 把 x1,y1 到x2,y2的長方形內的數字加起來

def setValue(x:int,y:int,value:int)->bool:
    if x >= len(matrixV) or y>= len(matrixV[0]) or x<0 or y<0 :
        return False
    else:
        matrixV[x][y] = value
        for i in range(len(matrixV)):
            print(matrixV[i])
        return True
    return False

def sumAll(x1,y1,x2,y2)->int:
    if x1 >= len(matrixV) or y1 >= len(matrixV[0]) or x1 < 0 or y1 < 0: return False
    if x2 >= len(matrixV) or y2 >= len(matrixV[0]) or x2 < 0 or y2 < 0: return False
    minX= min(x1,x2)
    maxX= max(x1,x2)+1
    minY= min(y1,y2)
    maxY= max(y1,y2)+1
    result=0
    for i in range(minX,maxX):
        for j in range(minY,maxY):
            result+=matrixV[i][j]
    return result


matrixV =  [[1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,1,1,1,1]]

x,y = 3,3
value = 1
if setValue( x,y,value ) == False:
    print(' fail to input the Value:',value,' at',x,',',y)

x1,y1=0,0
x2,y2=7,7
ans=sumAll(x1,y1,x2,y2)
if ans!=False:
    print('from (',x1,',',y1,')to(',x2,',',y2,'), the sum of those cells:',ans)
else:
    print(' input out of range!')