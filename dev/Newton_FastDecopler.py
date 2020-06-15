#####################################################
####################  Libraries  ####################
#####################################################

import math
import numpy as np
from numpy.linalg import inv
import time

import matplotlib.pyplot as plt

#####################################################
########  Loading and preparing branch data  ########
#####################################################

S_base = 100                                  
zeta = 10**-5      
   
branch_txt = 'System_IEEE_14bus_branch.txt'    
    

start_time = time.time()                    

data_branches = np.loadtxt(branch_txt, skiprows = 2)

if np.shape(data_branches) == (7,):
    data_branches = data_branches.reshape((1, 7))

TO =    data_branches[:,0]      
FROM =  data_branches[:,1]      
r =     data_branches[:,2]      
x =     data_branches[:,3]      
bsh =   data_branches[:,4]/2      
a =     data_branches[:,5]      
phi =   data_branches[:,6]      

#####################################################
######  Loading and preparing data from nodes  ######
#####################################################

node_txt = 'System_IEEE_14bus_node.txt' 
node_data = np.loadtxt(node_txt, skiprows = 3)

node2_txt = 'Data_Node.txt' 
node2_data = np.loadtxt(node2_txt, skiprows = 1)

NN = max(node_data[:,0])      
NN = int(NN)

bus = node_data[:,0]          
Type = node_data[:,1]   

V = node_data[:,2]            
theta = node_data[:,3]

P_G = node_data[:,4]/S_base    
Q_G = node_data[:,5]/S_base    
B_shunt = node_data[:,6]/S_base 

P_C = node2_data[:,1]/S_base    
Q_C = node2_data[:,2]/S_base    

P_nom = P_G - P_C               
Q_nom = Q_G - Q_C    

NN = int(max(max(TO),max(FROM)))    
NB = len(TO)                      

#####################################################
########  Calculation of initial parameters  ########
#####################################################

Y = np.zeros([NN,NN], dtype=complex)
tii = np.zeros([NB])
tjj = np.zeros([NB])
tij = np.zeros([NB])
tij = np.zeros([NB])

for b in range(NN):  
    Y[b][b] = B_shunt[b] *1j;

B_line = np.zeros([NN,NN])
B_2line = np.zeros([NN,NN])

for b in range(NB):
    i = int(TO[b])-1
    j = int(FROM[b])-1   
    
    ykm = (r[b]+x[b]*1j)**(-1)
 
    tii[b] = (a[b]*a[b])**(-1)
    tjj[b] = 1
    tij[b] = a[b]**(-1)

    Y[i][i] = Y[i][i] + tii[b]*ykm+ 1j*bsh[b]
    Y[j][j] = Y[j][j]+ tjj[b]*ykm+ 1j*bsh[b]   

    Y[i][j] = Y[i][j] - tij[b]*ykm
    Y[j][i] = Y[j][i] - tij[b]*ykm
    
    B_line[i][i] = B_line[i][i] + 1/x[b]
    B_line[j][j] = B_line[j][j] + 1/x[b]
    
    B_line[i][j] = -1/x[b]
    B_line[j][i] = -1/x[b]
    
    B_2line[i][i] = - 1/x[b]
    
    B_2line[i][j] = -1/x[b]
    B_2line[j][i] = -1/x[b]
    
    if Type[i] == 3 or Type[j] == 3:  
        B_line[i][j] = 0
        B_line[j][i] = 0
        
    if Type[i] ==3:
        B_line[i][i] = 10**10    


G = np.real(Y)               
B = np.imag(Y)            
  
for i in range(NN):
    for j in range(NN):
        if Type[i] < 1 and Type[j] < 1:
            B_2line[i][i] = -B[i][i]
            B_2line[i][j] = -B[i][j]
        if Type[i] > 1 or Type[j] > 1:
            B_2line[i][i] = 0
            B_2line[i][j] = 0
            B_2line[j][i] = 0
    if Type[i] > 1:
        B_2line[i][i] = 10**10   

var = node_data[:,8:14]

PV = [i for i in range(len(Type)) if Type[i] == 1 or Type[i] == 2]
nPV = len(PV) 

PQ = [i for i in range(len(Type)) if Type[i] == 3]
nPQ = len(PQ) 

#####################################################
#########  Beginning the iterative process  #########
#####################################################
B_line_inv= np.linalg.inv(B_line)
B_2line_inv= np.linalg.inv(B_2line)

p = 0
q = 0
KP = 0
KQ = 0


mismP = np.array([])
mismQ = np.array([])

while (p <= 200 or q <= 200):    

    P_Calc = np.zeros_like(P_nom)

    for i in range(NN):
        P_Calc[i] = G[i][i] * V[i]**2
    
    for w in range(NB):    
        i = int(TO[w])-1
        j = int(FROM[w])-1        
    
        ykm = (r[w]+x[w]*1j)**(-1)
        
        g = np.real(ykm) * tij[w]
        b = np.imag(ykm) * tij[w]
    
        ab = theta[i] - theta[j] + phi[w]    
    
        P_Calc[i] = P_Calc[i] + V[i] * V[j] * ( - g * math.cos(ab) - b * math.sin(ab))
        P_Calc[j] = P_Calc[j] + V[i] * V[j] * ( - g * math.cos(ab) + b * math.sin(ab))      

    DP = np.zeros_like(P_nom)    
    
    maxDP = 0   
    
    for i in range(NN):        
        if Type[i]!= 3:
            DP[i] = ((P_nom[i] - P_Calc[i])/V[i])            
            if abs(DP[i]) > abs(maxDP):
                maxDP = DP[i]  

    mismP = np.append(mismP, maxDP)
    
    if abs(maxDP) > zeta:  
        d_theta = np.dot(B_line_inv,DP)
        theta = d_theta + theta          
        KQ = 1
        p += 1
    else:
        KP = 0            
        if KQ == 0:		
            break			
 
    Q_Calc = np.zeros_like(Q_nom)
    
    for i in range(NN):
        Q_Calc[i] = - B[i][i] * V[i]**2
	
    for w in range(NB):    
        i = int(TO[w])-1
        j = int(FROM[w])-1        
    
        ykm = (r[w]+x[w]*1j)**(-1)
        
        g = np.real(ykm) * tij[w]
        b = np.imag(ykm) * tij[w]
    
        ab = theta[i]-theta[j]+ phi[w]  
	
        Q_Calc[i] = Q_Calc[i] + V[i] * V[j] * ( - g * math.sin(ab) + b * math.cos(ab))
        Q_Calc[j] = Q_Calc[j] - V[i] * V[j] * ( - g * math.sin(ab) - b * math.cos(ab))
    
    DQ = np.zeros_like(Q_nom)
    
    maxDQ = 0    

    for i in range(NN):          
        if Type[i]<= 1:
            DQ[i] = ((Q_nom[i] - Q_Calc[i])/V[i]) 
            
            if abs(DQ[i]) > abs(maxDQ):
                maxDQ = DQ[i] 
                
    mismQ = np.append(mismQ, maxDQ)
    
    if abs(maxDQ) > zeta:    
        dV = np.dot(B_2line_inv,DQ)
        V = dV + V    
        KP = 1
        q += 1
    else:
        KQ = 0
        if KP==0:
            break
total_time = time.time() - start_time

for k in range(NN):
    P_G[k] = P_Calc[k]+P_C[k]
    Q_G[k] = Q_Calc[k]+Q_C[k]
    
Pkm = np.zeros(NB)
Qkm = np.zeros(NB)
Pmk = np.zeros(NB)
Qmk = np.zeros(NB)
    
for w in range(NB):    
    k = int(TO[w])-1
    m = int(FROM[w])-1    

    ykm= (r[w])/(r[w]**2+x[w]**2) - (x[w]*1j)/(r[w]**2+x[w]**2)

    g = np.real(ykm)
    b = np.imag(ykm)
    
    ab = theta[k]-theta[m]-(phi[w]*math.pi/180)

    Pkm[w] = ((V[k]/a[w])**2)*g - V[k]*(V[m]/a[w])*(g*math.cos(ab) + b*math.sin(ab))
    Pmk[w] = (V[m]**2)*g - V[k]*(V[m]/a[w])*(g*math.cos(ab) - b*math.sin(ab))
    Qkm[w] = -((V[k]/a[w])**2)*(b + bsh[w]/2) + V[k]*(V[m]/a[w])*(b*math.cos(ab) - g*math.sin(ab))
    Qmk[w] = -(V[m]**2)*(b+bsh[w]/2) + V[k]*(V[m]/a[w])*(b*math.cos(ab) + g*math.sin(ab))

print(p,q,total_time)

print('|  Node  |   Voltage  |    Theta   |')
print('|    N   |    [pu]   |     [degrees]    |')
for k in range(NN):
    print(f'|    {k+1}    |   {V[k]:.4f}  |    {(theta[k]*180/math.pi): .2f}   |')

x = range(p)
y1= abs(mismQ)
y2= abs(mismP)
plt.ylabel('Magnitude of tension [p.u]')
plt.xlabel('Iterations')

plt.ylim(ymax = 1, ymin = 0)
plt.xlim(xmax = p, xmin = 0)
plt.plot(x, y1, y2)
plt.show()