# -*- coding: utf-8 -*-
import heapq
import matplotlib.pyplot as plt
spppp=['A','B','C','D','E','F','G','H','I','L','K','L']
filename='graph3.txt'
def POMSpT(s,t_nodes,graph,tr):
    hq=[]
    heapq.heappush(hq,(0,s,s))
    seen=set()    
    connect=[]
    dis=0
    while len(connect)<t_nodes:
        R_hq=[]
        a=heapq.heappop(hq)
        connect.append((a[1],a[2]))
        dis+=a[0]
        seen.add(a[2])
        seen.add(a[1])
        
        for i in range(t_nodes) :
            if (i not in seen) or(a[2] not in seen):
                heapq.heappush(hq,(abs(graph[a[2]][0]-graph[i][0])+abs(graph[a[2]][1]-graph[i][1]),a[2],i))   
               
        nnnn=0
        for i in range(len(hq)):
            K,L,M=heapq.heappop(hq)  
            
            if ((L not in seen) or (M not in seen)) :
                if tr == 1:
                    if nnnn==0 :
                        print('|{0}{1}|={2} is shortest'.format(spppp[L],spppp[M],K))
                        nnnn=1
                    else :
                        print('|{0}{1}|={2}'.format(spppp[L],spppp[M],K))
                heapq.heappush(R_hq,(K,L,M))
        
        print('-------------------------')
        hq=R_hq
    return connect,dis
def Heuristic (graph):
    n_graph=[]   
    graph_R1=[]
    for i in graph:
        graph_R1.append(i)
        for j in graph:  
            n_graph.append([i[0],j[1]])

    for i in X :
        A=i[0]
        B=i[1]
        Nhq=[]
        for j in n_graph:
        
            if (j[0]<=max(graph[A][0],graph[B][0])) and (j[0]>=min(graph[A][0],graph[B][0])) :
                if(j[1]<=max(graph[A][1],graph[B][1])) and (j[1]>=min(graph[A][1],graph[B][1])):
                    if(j != graph[A] ) and (j != graph[B] ) :
                        #print(j>=min(graph[A],graph[B]) ,j ,min(graph[A],graph[B]),j<=max(graph[A],graph[B]),max(graph[A],graph[B]))          
                        heapq.heappush(Nhq,(abs(graph[B][0]-j[0])+abs(graph[B][1]-j[1]),j))    
   #                 print(j)
        if len(Nhq) >0 :
            u,i=heapq.heappop(Nhq)
            graph_R1.append(i)
    return graph_R1

file=open(filename,'r')
graph_in=[]	 
for line in file:
    graph_in.append(list(map(int,line.split('	')))) 
nodes=graph_in.pop(0)
nodes=nodes[0]
start=0
flag=1
X,POMSpT_dis=POMSpT(start,nodes,graph_in,flag)
X.pop(0)
for i in X:
    print('{0}->{1}'.format(spppp[i[0]],spppp[i[1]]))
print('Total distance of POMSpT = {0}'.format(POMSpT_dis))
flag=0
Hin=Heuristic (graph_in)
c,dis=POMSpT(start,len(Hin),Hin,flag)


c.pop(0)
#圖
fig, ax=plt.subplots()
plt.title('POMSpT')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.xticks([])
plt.yticks([])
for i in X:
    plt.plot([graph_in[i[0]][0],graph_in[i[1]][0]],[graph_in[i[0]][1],graph_in[i[1]][1]],'b')
for i in graph_in:  
    print()
    plt.scatter(i[0], i[1],s=100,c='g')
    plt.text(i[0], i[1]+0.3, (i[0],i[1]), ha='center', va='bottom', fontsize=10.5)

plt.savefig("H11.png")
fig, ax=plt.subplots()
plt.title('POMRST')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.xticks([])
plt.yticks([])
for i in c:
    plt.plot([Hin[i[0]][0],Hin[i[1]][0]],[Hin[i[0]][1],Hin[i[1]][1]],'b')
for i in Hin:  
    print()
    if (i in graph_in):
        plt.scatter(i[0], i[1],s=100,c='g')
    else:
        plt.scatter(i[0], i[1],s=100,c='r')
    plt.text(i[0], i[1]+0.3, (i[0],i[1]), ha='center', va='bottom', fontsize=10.5)
print('Total distance of POMSpT = {0}'.format(POMSpT_dis))
print('Total distance of POMRST = {0}'.format(dis))
