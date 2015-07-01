#Written by Dabin Lee
#Last update 2015.06.30
#Import necessary libraries
###########################################################################################################

import csv
import numpy as np
import struct as st
import os


def Quant(OpenName,Alpha=0.2,Num_Samples=64):
    
    #Open csv file as a list \
    with open(os.getcwd()+"\\"+OpenName+".csv",'rb') as csvfile:
        reader = csv.reader(csvfile)
        val_list = list(reader)
        
    #Remove inapprorpirate values
    #print "Number of elements:",len(val_list)
    while val_list.count(['-Infinity']) > 0:
        val_list.remove(['-Infinity'])
    #print "Number of elements after removing inapprorpirate values",len(val_list)
    
    #Convert string element to float 
    final_list=[]
    for i in range(0,len(val_list)):
        final_list.append(float(val_list[i][0]))
        
    #Filtering for noise
    filter_list=[]
    fc=5
    initial_mean=np.mean(final_list[0:5])
    lockNum=0
    print fc < len(final_list)
    while fc < len(final_list):
        print "Number to check:",final_list[fc],"Stand:",(initial_mean-(initial_mean*0.3)) 
        if final_list[fc] >= (initial_mean-(initial_mean*0.3)):
            lockNum=fc
            break
        else:
            fc+=1
            initial_mean=np.mean(final_list[(fc-5):fc])
    for e in range(lockNum,len(final_list)):
        filter_list.append(final_list[e])
    
    print len(filter_list)

    final=[]
    Num_Skip=len(filter_list)/Num_Samples
    j=0
    k=0
    while j < Num_Samples:
        #print j
        final.append(filter_list[k])
        k+=Num_Skip
        j+=1 
    #print final
    #print(len(final))
    #Calculate necessary values
    mean=np.mean(final)
    stdv=np.std(final)
    Upper_Thresh=mean+(stdv*Alpha)
    Lower_Thresh=mean-(stdv*Alpha)
    
    #Printouts to let the user know about the data
    print "Arithmetic mean:",mean
    print "Stan. deviation:",stdv
    print "Upper Threshold:",Upper_Thresh
    print "Lower Threshold:",Lower_Thresh
    #print final
    
    #Quantization
    csv_list=[]
    for i in range(0,len(final)):
        if final[i] >= Upper_Thresh:
            csv_list.append(1)
        elif final[i] <= Lower_Thresh:
            csv_list.append(0)
    
    #Output to CSV file
    outputCSVFile = open(os.getcwd()+"\\"+OpenName+"A_"+str(Alpha)+"S_"+str(Num_Samples)+".csv",'wb')
    wr = csv.writer(outputCSVFile,quoting=csv.QUOTE_ALL)
    wr.writerow(csv_list)
    outputCSVFile.close()
    csvfile.close()
    
    #Output to ASCII file for NIST Analysis
    outputASCIIFile = open(os.getcwd()+"\\"+OpenName+"A_"+str(Alpha)+"S_"+str(Num_Samples)+".dat",'w')
    for item in csv_list:
        print item
        outputASCIIFile.write(str(item))
#     binData = 'f'*len(csv_list)
#     bin=st.pack(binData,*csv_list)
#     print(bin)
#     outputBINFile.write(bin)
    outputASCIIFile.close()
Quant("Movement Close Eve")