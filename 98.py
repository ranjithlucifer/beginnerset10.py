name=int(input())
w=input().split()
b=sorted(w)
a=[]
for i in range(0,name):
    if w[i]!=b[i]:
        a.append(i)
        break
    else:
        continue
print(*a)
