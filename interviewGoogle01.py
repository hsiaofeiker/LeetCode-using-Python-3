# Google interview Q1
# find the no use items in A and B.
# A=[1,6,5,10,3,10]
# B=[3,5,4,6]
# Return will be [1,4,10]
# set 不會記錄重複的, 要利用 Set的特性.
def findtheDifference(A:list,B:list) -> list:
    setA=set()
    setB=set()
    result=set()    #記錄A不在B裡,也記錄B不在A裡的,使用set 就不會重覆紀錄

    for i in range(len(A)):     # 將list A 轉到 setA, 就能除去重複的
        setA.add(A[i])
    for i in range(len(B)):     # 將list B 轉到 setB, 就能除去重複的
        setB.add(B[i])
    for i in range(len(A)):     # 若 listA 中的資料, 既不在setB, 也沒有在 reuslt. 就可記錄到 result.
        if A[i] not in setB and A[i] not in result:
            result.add(A[i])
    for i in range(len(B)):     # 若 listB 中的資料, 既不在setA, 也沒有在 reuslt. 就可記錄到 result.
        if B[i] not in setA and B[i] not in result:
            result.add(B[i])
    return result

listA=[1,6,5,10,3,6,10]
listB=[3,5,4,6,3]
# sorted( string, tuple, list) 可排序 string, tuple, list
print(sorted(findtheDifference(listA,listB)))
