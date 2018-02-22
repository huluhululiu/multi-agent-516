import sys
import re
import numpy as np
def othermax(v,i,j,price):
    maxvalue=0
    H,W=v.shape
    for k in range(0,H):
        if k!=j:
            maxvalue=max(v[i][k]-price[k],maxvalue)
    return maxvalue
def unassigned(agent):
    allproduct=1
    for i in agent:
        allproduct*=i
    return allproduct

def performauction(v):
	assigned=np.full_like(v,0)
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
	    if agent[i]==0:
	        maxvalue=0
	        j=0
	        #Find an object j ∈ X that offers i maximal value at current prices:
	        for k in range(0,H):
	            diff=v[i][k]-price[k]

	            if diff>maxvalue:
	                maxvalue=diff
	                j=k
	        # Compute i’s bid increment for j:
	        b=maxvalue-othermax(v,i,j,price)+1
	        # remove current(i',j)
	        for m in range(0,H):
	            if assigned[m][j]==1:
	                assigned[m][j]=0
	                agent[m]=0
	                totalvalue[m]=0
	        #increase price p[j]& assignment step
	        price[j]=price[j]+b
	        agent[i]=1
	        assigned[i][j]=1
	        totalvalue[i]=v[i][j]
	    count += 1
	return sum(totalvalue)*1.0/H

M=100
sumofrun=[]
for n in range(2,257):
	summ=0
	if n%10==0:
		print(n/256)
	for i in range(1000):
		v= np.random.randint(0, M, size=(n, n))
		summ+=performauction(v)
	sumofrun.append(summ)
thefile = open('result.txt', 'w')
for item in ss:
    thefile.write("%s\n" % item)