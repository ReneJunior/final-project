#####################################################
####################  Libraries  ####################
#####################################################

import math
import numpy as np
from numpy.linalg import inv

#####################################################
########  Loading and preparing branch data  ########
#####################################################


PC_txt = 'PC.txt'    
QC_txt = 'QC.txt'     


PC_txt = np.loadtxt(PC_txt, skiprows = 2)
QC_txt = np.loadtxt(QC_txt, skiprows = 2)

NN = 14
ND = 144

PC_1 =  PC_txt[:,1]      
PC_2 =  PC_txt[:,2]      
PC_3 =  PC_txt[:,3]      
PC_4 =  PC_txt[:,4]      
PC_5 =  PC_txt[:,5]      
PC_6 =  PC_txt[:,6]      
PC_7 =  PC_txt[:,7]    
PC_8 =  PC_txt[:,8]    
PC_9 =  PC_txt[:,9]    
PC_10=  PC_txt[:,10]    
PC_11=  PC_txt[:,11]    
PC_12=  PC_txt[:,12]    
PC_13=  PC_txt[:,13]    
PC_14=  PC_txt[:,14]    

QC_1 =  QC_txt[:,1]      
QC_2 =  QC_txt[:,2]      
QC_3 =  QC_txt[:,3]      
QC_4 =  QC_txt[:,4]      
QC_5 =  QC_txt[:,5]      
QC_6 =  QC_txt[:,6]      
QC_7 =  QC_txt[:,7]    
QC_8 =  QC_txt[:,8]    
QC_9 =  QC_txt[:,9]    
QC_10=  QC_txt[:,10]    
QC_11=  QC_txt[:,11]    
QC_12=  QC_txt[:,12]    
QC_13=  QC_txt[:,13]    
QC_14=  QC_txt[:,14]    


max_PC_1 =  0
max_PC_2 =  0
max_PC_3 =  0
max_PC_4 =  0
max_PC_5 =  0
max_PC_6 =  0
max_PC_7 =  0
max_PC_8 =  0
max_PC_9 =  0
max_PC_10=  0
max_PC_11=  0
max_PC_12=  0
max_PC_13=  0
max_PC_14=  0

max_QC_1 =  0
max_QC_2 =  0
max_QC_3 =  0
max_QC_4 =  0
max_QC_5 =  0
max_QC_6 =  0
max_QC_7 =  0
max_QC_8 =  0
max_QC_9 =  0
max_QC_10=  0
max_QC_11=  0
max_QC_12=  0
max_QC_13=  0
max_QC_14=  0


file = open('Data_Node.txt','w+') 

for i in range(ND):          
        
    if abs(PC_1[i]) > abs(max_PC_1):
        max_PC_1 = PC_1[i] 

    if abs(PC_2[i]) > abs(max_PC_2):
        max_PC_2 = PC_2[i] 
    
    if abs(PC_3[i]) > abs(max_PC_3):
        max_PC_3 = PC_2[i] 
    
    if abs(PC_4[i]) > abs(max_PC_4):
        max_PC_4 = PC_4[i] 
    
    if abs(PC_5[i]) > abs(max_PC_5):
        max_PC_5 = PC_5[i] 
    
    if abs(PC_6[i]) > abs(max_PC_6):
        max_PC_6 = PC_6[i] 
    
    if abs(PC_7[i]) > abs(max_PC_7):
        max_PC_7 = PC_7[i] 
    
    if abs(PC_8[i]) > abs(max_PC_8):
        max_PC_8 = PC_8[i] 
    
    if abs(PC_9[i]) > abs(max_PC_9):
        max_PC_9 = PC_9[i] 
    
    if abs(PC_10[i]) > abs(max_PC_10):
        max_PC_10 = PC_10[i] 
    
    if abs(PC_11[i]) > abs(max_PC_11):
        max_PC_11 = PC_11[i] 
    
    if abs(PC_12[i]) > abs(max_PC_12):
        max_PC_12 = PC_12[i] 
    
    if abs(PC_13[i]) > abs(max_PC_13):
        max_PC_13 = PC_13[i] 
    
    if abs(PC_14[i]) > abs(max_PC_14):
        max_PC_14 = PC_14[i] 
    
    if abs(QC_1[i]) > abs(max_QC_1):
        max_QC_1 = QC_1[i] 
    
    if abs(QC_2[i]) > abs(max_QC_2):
        max_QC_2 = QC_2[i] 
    
    if abs(QC_3[i]) > abs(max_QC_3):
        max_QC_3 = QC_3[i] 
    
    if abs(QC_4[i]) > abs(max_QC_4):
        max_QC_4 = QC_4[i] 
    
    if abs(QC_5[i]) > abs(max_QC_5):
        max_QC_5 = QC_5[i] 
    
    if abs(QC_6[i]) > abs(max_QC_6):
        max_QC_6 = QC_6[i] 
    
    if abs(QC_7[i]) > abs(max_QC_7):
        max_QC_7 = QC_7[i] 
    
    if abs(QC_8[i]) > abs(max_QC_8):
        max_QC_8 = QC_8[i] 
    
    if abs(QC_9[i]) > abs(max_QC_9):
        max_QC_9 = QC_9[i] 
    
    if abs(QC_10[i]) > abs(max_QC_10):
        max_QC_10 = QC_10[i] 
    
    if abs(QC_11[i]) > abs(max_QC_11):
        max_QC_11 = QC_11[i] 
    
    if abs(QC_12[i]) > abs(max_QC_12):
        max_QC_12 = QC_12[i] 
    
    if abs(QC_13[i]) > abs(max_QC_13):
        max_QC_13 = QC_13[i] 
    
    if abs(QC_14[i]) > abs(max_QC_14):
        max_QC_14 = QC_14[i] 
        

file.write('Node \t PC \t QC\n')
file.write(f'{1}\t {max_PC_1} \t {max_QC_1}\n')      
file.write(f'{2}\t {max_PC_2} \t {max_QC_2}\n')      
file.write(f'{3}\t {max_PC_3} \t {max_QC_3}\n')      
file.write(f'{4}\t {max_PC_4} \t {max_QC_4}\n')      
file.write(f'{5}\t {max_PC_5} \t {max_QC_5}\n')      
file.write(f'{6}\t {max_PC_6} \t {max_QC_6}\n')      
file.write(f'{7}\t {max_PC_7} \t {max_QC_7}\n')      
file.write(f'{8}\t {max_PC_8} \t {max_QC_8}\n')      
file.write(f'{9}\t {max_PC_9} \t {max_QC_9}\n')      
file.write(f'{10}\t {max_PC_10} \t {max_QC_10}\n')      
file.write(f'{11}\t {max_PC_11} \t {max_QC_11}\n')      
file.write(f'{12}\t {max_PC_12} \t {max_QC_12}\n')      
file.write(f'{13}\t {max_PC_13} \t {max_QC_13}\n')      
file.write(f'{14}\t {max_PC_14} \t {max_QC_14}\n')      
        
        
        
file.close()