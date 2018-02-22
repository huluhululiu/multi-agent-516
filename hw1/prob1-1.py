import re
import numpy as np
def othermax(v,i,j,price):

    maxvalue=0
    for k in range(0,H):
        if k!=j:
            maxvalue=max(v[i][k]-price[k],maxvalue)
    return maxvalue
def unassigned(agent):
    allproduct=1
    for i in agent:
        allproduct*=i
    return allproduct

arr = []
inp = open ("dat.txt","r")
for line in inp.readlines():
    arr.append([])
    for i in line.split():
        arr[-1].append(int(i))
v=np.asarray(arr)
assigned=np.full_like(arr,0)
H,W=v.shape
price=[]
agent=[]
ss=[]

totalvalue=[]
for i in range(H):
    agent.append(0)
    price.append(0)
    ss.append(0)
    totalvalue.append(0)
count=0
total=0
while unassigned(agent)==0:
    i=count%H
    print(count)
    print(i)
    if agent[i]==0:
        print (i)
        maxvalue=0
        j=0
        #Find an object j ∈ X that offers i maximal value at current prices:
        for k in range(0,H):
            diff=v[i][k]-price[k]

            if diff>maxvalue:
                maxvalue=diff
                j=k
        # Compute i’s bid increment for j:
        b=maxvalue-othermax(v,i,j,price)
        # remove current(i',j)
        for m in range(0,H):
            if assigned[m][j]==1:
                assigned[m][j]=0
                agent[m]=0
                ss[m]=0
                totalvalue[m]=0
        #increase price p[j]& assignment step
        price[j]=price[j]+b
        agent[i]=1
        assigned[i][j]=1
        ss[i]=j
        totalvalue[i]=v[i][j]
        print("price for bid ",price[j])
    count += 1
    #print(price)
    # temp=sum(totalvalue)
    # if total==temp:
    #     break
    # if total<temp:
    #     total=temp
    


print(sum(totalvalue)*1.0/H)
print(ss)
thefile = open('test.txt', 'w')
for item in ss:
  thefile.write("%s\n" % item)

