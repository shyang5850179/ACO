# -*- coding: utf-8 -*-
import numpy as np
import dspBox as dsp
file=open('obser1.txt','r')	
obser1_r =file.read() 
#print(obser1_r)
obser1= dsp.str2ndar(obser1_r)
file.close
file=open('obser2.txt','r')	
obser2_r =file.read() 
obser2= dsp.str2ndar(obser2_r)
file.close
file=open('obser3.txt','r')	
obser3_r =file.read() 
obser3= dsp.str2ndar(obser3_r)
file.close

A1=np.array([[0.2,0.7,0.1],[0.1,0.2,0.7],[0.7,0.1,0.2]])
B1=np.array([[0.5,0.4,0.1],[0.7,0.2,0.1],[0.7,0.1,0.2]])
pi1=np.array([0.7,0.2,0.1])

A2=np.array([[0.7,0.2,0.1],[0.3,0.6,0.1],[0.1,0.2,0.7]])
B2=np.array([[0.1,0.8,0.1],[0.2,0.7,0.1],[0.4,0.5,0.1]])
pi2=np.array([0.1,0.7,0.2])

A3=np.array([[0.2,0.7,0.1],[0.6,0.3,0.1],[0.2,0.7,0.1]])
B3=np.array([[0.1,0.2,0.7],[0.2,0.2,0.6],[0.3,0.1,0.6]])
pi3=np.array([0.2,0.2,0.6])
#print(obser1)
p_f=[]
p_b=[]
#forward
def forward (obser,A,B,pi): 
    alpha=np.zeros((len(pi)),dtype=np.float64)
    alpha=pi*B[:,obser[0]]    
    for j in range(1,len(obser),+1):    
        R_alpha=np.zeros((len(pi)),dtype=np.float64)
        for i in range(len(pi)):        
            a=A[:,i]       
            R_alpha [i]=sum(alpha*a)*B[i][obser[j]]         
        alpha=R_alpha     
    return sum(alpha)


def backward (obser,A,B,pi):
    bata=np.ones((len(pi)),dtype=np.float64)
    for j in range(len(obser)-1,0,-1):   
        R_bata=np.zeros((len(pi)),dtype=np.float64)   
        b=B[:,obser[j]]
        #print(j)        
        for i in range(len(pi)):            
            a=A[i]              
            R_bata[i]=sum(bata*a*b)           
        bata=R_bata  
    #print(B[:,obser[0]],type(B))
    return sum(bata*pi*B[:,obser[0]])
p_b.append(backward (obser1,A1,B1,pi1 ) )
p_b.append(backward (obser2,A2,B2,pi2 ) )
p_b.append(backward (obser3,A3,B3,pi3 ) )    
p_f.append(forward (obser1,A1,B1,pi1))
p_f.append(forward (obser2,A2,B2,pi2))
p_f.append(forward (obser3,A3,B3,pi3))           

for i in range(0,3,+1):
    print('obser{0}:'.format(i)) 
    print('model_{0} forward:{1} backward:{2} '.format(i,'%.16e'%(p_f[i]),'%.16e'%(p_b[i])))           
         
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            