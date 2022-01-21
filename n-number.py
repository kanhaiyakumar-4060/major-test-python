lst = []
n = int(input())
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
maxi = max(lst)


for i in range(1,maxi+1):
    if i in lst:
        continue
    else:
        print(i)
        break
if i == maxi:
    print(i+1)