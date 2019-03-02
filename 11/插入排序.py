#1.书上那种
'''
def inertsort(l):  #参数的传入，当想传入的是一个list时，直接传入一个变量就行了
    N=len(l)
    for x in range(1,N):
        a,b=x,x
        n=l[x]
        while n<l[a-1] and a-1>=0:
            a=a-1
            if a-1<0:
                a=0
        while b>a:
            l[b]=l[b-1]
            b=b-1
        l[a]=n

l=[8,3,7,4,5,6,3,0,2,9,3,5,8,5,6,7,2,1]
inertsort(l)
print (l)
'''

#自己瞎写,将待插入元素与其前一个元素进行比较，若小于，则将前一个元素后移一位，在将带插入元素与前前一位进行比较，若小于，则将前前一位往后移，如此操作直到遇到小于待插入元素的位置，插入到该位后一位（此位已经在上一步后移了）
# def InsertSort(l):
#     n = len(l)
#     for i in range(1,n):
#         key = l[i]
#         a = i
#         while key < l[a-1] and a-1>0:
#             l[a] = l[a-1]
#             a = a-1
#             l[a] = key
# l = [1,23,4,5,3,2,32,323,24,6235,34,234,3]
# InsertSort(l)
# print(l)


# def insert(l):
#     n = len(l)
#     for i in range(1,n):
#         key = l[i]
#         a = i-1
#         while key < l[a] and a>0:
#             l[a+1] = l[a]
#             a = a-1
#             l[a+1] = key

def Insort(A):
    for i in range (1,len(A)):
        key = A[i]
        j = i
        while j > 0 and A[j-1]>key:
            A[j] = A[j-1]
            j = j-1
            A[j] = key


l = [1,2,46,7,43,723,5,24,536,346]
Insort(l)
print(l)