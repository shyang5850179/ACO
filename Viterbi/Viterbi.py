# -*- coding: utf-8 -*-
import numpy as np
import dspBox as dsp
Tobser=[]
file=open('Observation_1.txt','r')	
obser1_r =file.read() 
Tobser.append(dsp.str2ndar(obser1_r))
file.close
file=open('Observation_2.txt','r')	
obser2_r =file.read() 
Tobser.append(dsp.str2ndar(obser2_r))
file.close
file=open('Observation_3.txt','r')	
obser3_r =file.read() 
Tobser.append(dsp.str2ndar(obser3_r))
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
TA=np.array([A1,A2,A3])
TB=np.array([B1,B2,B3])
Tpi=np.array([pi1,pi2,pi3])

def Viterbi (obser,A,B,pi): 
    state=np.zeros((len(obser)-1,len(pi)),dtype=np.int32)   
    delta=pi*B[:,obser[0]]    
    #Adelta=[]
    #Adelta.append(delta)
    for j in range(1,len(obser),+1):
        M_delta=np.zeros(len(pi),dtype=np.float64)    
        for i in range(len(pi)):
            M_delta[i]=max(delta*A[:,i]*B[i][obser[j]])
            state[j-1][i]=np.argmax(delta*A[:,i]*B[i][obser[j]])
        delta=M_delta
    #print(state)
            #Adelta.append(delta)
    w=[]
    w.append(np.argmax(delta))
    for i in range(len(state)):    
        w.append(state[len(state)-1-i][w[i]])
    w=w[::-1]
    return max(delta),w
P,S=Viterbi(Tobser[1],TA[1],TB[1],Tpi[1])
for i in range(len(TA)) :
    print('obser_{0}'.format(i+1))
    for j in range(len(Tobser)):
        P,S=Viterbi(Tobser[i],TA[j],TB[j],Tpi[j])
        print('Model_{0} probability:{1}'.format(j+1,P))
        print('Viterbi max state sequence:{0}'.format(S) )
        
    print('\n')

