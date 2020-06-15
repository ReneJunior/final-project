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

NN = max(node_data[:,0])      
NN = int(NN)

bus = node_data[:,0]          
Type = node_data[:,1]   

V = node_data[:,2]            
theta = node_data[:,3]

P_G = node_data[:,4]/S_base    
Q_G = node_data[:,5]/S_base    
B_shunt = node_data[:,6]/S_base 

node2_txt = 'Data_Node.txt' 
node2_data = np.loadtxt(node2_txt, skiprows = 1)
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

for b in range(NN):  
    Y[b][b] = B_shunt[b] *1j;

for b in range(NB):
    i = int(TO[b])-1
    j = int(FROM[b])-1   
    
    ykm = 1/(r[b]+x[b]*1j)
 
    tii[b] = 1/(a[b]*a[b])
    tjj[b] = 1
    tij[b] = 1/ a[b]



    Y[i][i] = Y[i][i] + tii[b]*ykm+ 1j*bsh[b]
    Y[j][j] = Y[j][j]+ tjj[b]*ykm+ 1j*bsh[b]
    

    Y[i][j] = Y[i][j] - tij[b]*ykm
    Y[j][i] = Y[j][i] - tij[b]*ykm

G = np.real(Y)                
B = np.imag(Y)              

#####################################################
#########  Beginning the iterative process  #########
#####################################################

itera = 0 
maxDP = 10**5
maxDQ = 10**5

mismP = np.array([])
mismQ = np.array([])

while (abs(maxDP) > zeta or abs(maxDQ) > zeta):    

    P_Calc = np.zeros_like(P_nom)
    Q_Calc = np.zeros_like(Q_nom)
    for i in range(NN):
        P_Calc[i] = G[i][i] * V[i] * V[i]
        Q_Calc[i] =-B[i][i] * V[i] * V[i]
    
    for w in range(NB):    
        i = int(TO[w])-1
        j = int(FROM[w])-1        
    
        ykm = 1/(r[w]+x[w]*1j)
    
        g = np.real(ykm) * tij[w]
        b = np.imag(ykm) * tij[w]
    
        ab = theta[i]-theta[j]+ phi[w]    

        P_Calc[i] = P_Calc[i] + V[i] * V[j] * ( - g * math.cos(ab) - b * math.sin(ab))
        P_Calc[j] = P_Calc[j] + V[i] * V[j] * ( - g * math.cos(ab) + b * math.sin(ab))
        
        Q_Calc[i] = Q_Calc[i] + V[i] * V[j] * ( - g * math.sin(ab) + b * math.cos(ab))
        Q_Calc[j] = Q_Calc[j] - V[i] * V[j] * ( - g * math.sin(ab) - b * math.cos(ab))

    DP = np.zeros_like(P_nom)    
    DQ = np.zeros_like(Q_nom)
    
    maxDP = 0
    maxDQ = 0    
    
    for i in range(NN):        
        if Type[i]!= 3:
            DP[i] = P_nom[i] - P_Calc[i]
            
            if abs(DP[i]) > abs(maxDP):
                maxDP = DP[i]
                
        if Type[i]<= 1:
            DQ[i] = Q_nom[i] - Q_Calc[i]
            
            if abs(DQ[i]) > abs(maxDQ):
                maxDQ = DQ[i]    

    mismQ = np.append(mismQ, maxDQ)
    mismP = np.append(mismP, maxDP)

    DS = np.r_[DP,DQ]    
    
    H = np.zeros((NN, NN))
    N = np.zeros((NN, NN))
    M = np.zeros((NN, NN))
    L = np.zeros((NN, NN))
    
    for i in range(NN):
        
        H[i][i] =-Q_Calc[i] - V[i]**2 * B[i][i]
        if Type[i] == 3:
            H[i][i] = 10**10     
        N[i][i] = P_Calc[i] + V[i] * G[i][i]
        M[i][i] = P_Calc[i] - V[i]* V[i] * G[i][i]
        L[i][i] = Q_Calc[i] - V[i] * B[i][i]        
        if Type[i] >= 2:
            L[i][i] = 10**10
    
    for w in range(NB):    
        i = int(TO[w])-1
        j = int(FROM[w])-1        
        
        ab = theta[i]-theta[j]-(phi[w]*math.pi/180)
        
        H[i][j] = V[i] * V[j] * ( G[i][j] * math.sin(ab) - B[i][j] * math.cos(ab))
        H[j][i] = V[i] * V[j] * (-G[i][j] * math.sin(ab) - B[i][j] * math.cos(ab))
    
        N[i][j] = V[i] * (G[i][j] * math.cos(ab) + B[i][j] * math.sin(ab))
        N[j][i] = V[j] * (G[i][j] * math.cos(ab) - B[i][j] * math.sin(ab))
        
        M[i][j] =-V[i] * V[j] * (G[i][j] * math.cos(ab) + B[i][j] * math.sin(ab))
        M[j][i] =-V[i] * V[j] * (G[i][j] * math.cos(ab) - B[i][j] * math.sin(ab))
    
        L[i][j] = V[i] * (G[i][j] * math.sin(ab) - B[i][j] * math.cos(ab))
        L[j][i] = V[j] * (G[i][j] * math.sin(ab) - B[i][j] * math.cos(ab))    
    
    J1 = np.hstack((H, N))
    J2 = np.hstack((M, L))
    J = np.linalg.inv(np.vstack((J1, J2)))

    DV = np.dot(J,DS)
    
    d_theta = DV[:NN]
    dV = DV[NN:]

    theta = d_theta + theta        
    V = dV + V    

    itera += 1
    if itera >= 200:
        print("Maximum number of iterations reached.")
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

    ykm = 1/(r[w]+x[w]*1j)

    g = np.real(ykm)
    b = np.imag(ykm)
    
    ab = theta[k]-theta[m]-(phi[w]*math.pi/180)

    Pkm[w] = ((V[k]/a[w])**2)*g - V[k]*(V[m]/a[w])*(g*math.cos(ab) + b*math.sin(ab))
    Pmk[w] = (V[m]**2)*g - V[k]*(V[m]/a[w])*(g*math.cos(ab) - b*math.sin(ab))
    Qkm[w] = -((V[k]/a[w])**2)*(b + bsh[w]/2) + V[k]*(V[m]/a[w])*(b*math.cos(ab) - g*math.sin(ab))
    Qmk[w] = -(V[m]**2)*(b+bsh[w]/2) + V[k]*(V[m]/a[w])*(b*math.cos(ab) + g*math.sin(ab))

    

print('|  Node  |   Voltage  |    Theta   |')
print('|    N   |    [pu]   |     [degrees]    |')
for k in range(NN):
    print(f'|    {k+1}    |   {V[k]:.4f}  |    {(theta[k]*180/math.pi): .2f}   |')


x = range(itera)
y1= abs(mismQ)
y2= abs(mismP)
plt.ylabel('Magnitude of tension [p.u]')
plt.xlabel('Node')

plt.ylim(ymax = 1, ymin = 0)
plt.xlim(xmax = itera, xmin = 0)
plt.plot(x, y1, y2)
plt.show()