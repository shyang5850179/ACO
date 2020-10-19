# -*- coding: utf-8 -*-
import heapq
Graph=open('graph2.txt','r')
result=[]
Gp={}
Gpr={}
#read file
for line in Graph:
    result.append(list(map(int,line.split('	')))) 
start=result[0][0] # start vertex
vex_n=len(result)-1
del(result[0])
for i in range(vex_n):
    num=i+1
    row=result[i]
    Gpr={}
    for j in range(vex_n):
        if row[j] !=0 :
            Gpr.setdefault(j+1,row[j])
    Gp.setdefault(num,Gpr)
Graph.close()
#
pqueue=[]
heapq.heappush(pqueue, (0,start))
seen=set() 
parent=[]
distance=0
while(len(pqueue) > 0):
    dis,vertex=heapq.heappop(pqueue)
    node=Gp[vertex].keys()
    if  vertex not in seen:         
        distance=distance+dis
        parent.append(vertex)
    seen.add(vertex)         
    for w in node:       
        if w not in seen:            
               heapq.heappush(pqueue,(Gp[vertex][w],w))
     
    
print('the final path is',parent)
print('Weight is', distance)


