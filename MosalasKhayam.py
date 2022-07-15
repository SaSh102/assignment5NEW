def MosalasKhayam(n):
    list=[]
    for i in range(n):
        list.append([1]*(i+1))

    for i in range(2,n):
        for j in range(1,i):
            list[i][j]=list[i-1][j-1]+list[i-1][j]
    return list

num = int(input('please enter a number: '))
x = MosalasKhayam(num)
for i in x:
    print(i)



