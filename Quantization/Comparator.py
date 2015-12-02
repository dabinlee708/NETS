import csv
import numpy as np
import struct as st
import hashlib as hl
import itertools as it
import os

def csvToList(Name1):
    
    #Open a .CSV file for comparison
    with open(os.getcwd()+os.sep+"Output_Data"+os.sep+Name1+".csv",'rb') as file1:
        reader1 = csv.reader(file1)
        val_list1 = list(reader1)
    #print "val_list",val_list1    
    print val_list1
    list1=[]
    for i in range(0,len(val_list1[0])):
        list1.append(int(val_list1[0][i]))
    return list1

def csvToList2(Name1, Name2):
    return csvToList(Name1), csvToList(Name2)

def csvToList3(Name1, Name2, Name3):
    return csvToList(Name1), csvToList(Name2), csvToList(Name3)
    
def compare2(OpenName1,OpenName2):    
    #Open two .CSV files for comparison
    with open(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName1+".csv",'rb') as file1:
        reader1 = csv.reader(file1)
        val_list1 = list(reader1)
#         print "val_list",val_list1
    with open(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName2+".csv",'rb') as file2:
        reader2 = csv.reader(file2)
        val_list2 = list(reader2)
    
    #Set global length for comparison
    
    GlobalLength=0
    if len(val_list1[0]) >= len(val_list2[0]):
        GlobalLength=len(val_list2[0])
    elif len(val_list2[0]) < len(val_list1[0]):
        GlobalLength=len(val_list1[0])
    print "Length of the shorter key:",GlobalLength    
    #Initialize Error Counter
    ErrorCounter=0.00
    i=0
    while i < GlobalLength:
        if val_list1[0][i]==val_list2[0][i]:
            i+=1
        else:
            ErrorCounter+=1.00
            i+=1
    
    #Output
    print "Files compared:\n",OpenName1+"\n",OpenName2
    if GlobalLength!=0:
        print "Mismatch Rate:",(ErrorCounter/GlobalLength)
        print "Match Rate:",(1-((ErrorCounter/GlobalLength)))
        
        print "============================================="
    else:
        print "length is 0"
        print "============================================="
def Quant3(OpenName1, OpenName2, OpenName3, Alpha = 0.2, Num_Samples = 64, Filtering = True):
    Quant(OpenName1,Alpha,Num_Samples,Filtering)
    Quant(openName2,Alpha,Num_Samples,Filtering)
    Quant(OpenName3,Alpha,Num_Samples,Filtering)

def Quant2(OpenName1,OpenName2,Alpha=0.2,Num_Samples=64,Filtering=True):
    Quant(OpenName1,Alpha,Num_Samples,Filtering)
    Quant(OpenName2,Alpha,Num_Samples,Filtering)

def Quant(OpenName,Alpha=0.2,Num_Samples=64,Filtering=True):
    print "Quantization\nFile Name:\t",OpenName,"\nAlpha ",Alpha,"\nNumber of Samples ",Num_Samples,"\nFiltering Option ",Filtering

    #Set sampling count
    if Num_Samples==0:
        Sampling=False
    else:
        Sampling=True
    
    #Open csv file as a list \
    with open(os.getcwd()+os.sep+"Source_Data"+os.sep+OpenName+".csv",'rb') as csvfile:
        reader = csv.reader(csvfile)
        val_list = list(reader)
        
    #Remove inapproprirate values
    #print "Number of elements:",len(val_list)
    while val_list.count(['-Infinity']) > 0:
        val_list.remove(['-Infinity'])
    while val_list.count(['#NAME?'])>0:
        val_list.remove(['#NAME?'])
                         
    #print "Number of elements after removing inapproprirate values",len(val_list)
    
    #Convert string element to float 
    final_list=[]
    for i in range(0,len(val_list)):
        final_list.append(float(val_list[i][0]))
        
    #Filtering for noise [Skip if False]
    if Filtering==True:
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
    else:
        filter_list=final_list
    
    
    #Sampling done here
    if Sampling==True:
        
        final=[]
        Num_Skip=len(filter_list)/Num_Samples
        j=0
        k=0
        while j < Num_Samples:
            #print j
            final.append(filter_list[k])
            k+=Num_Skip
            j+=1 
    else:
        final=list(filter_list)
    #print final
    #print(len(final))
    #Calculate necessary values
    mean=np.mean(final)
    stdv=np.std(final)
    Upper_Thresh=mean+(stdv*Alpha)
    Lower_Thresh=mean-(stdv*Alpha)
    
    #Printouts to let the user know about the data
#     print "Arithmetic mean:",mean
#     print "Stan. deviation:",stdv
#     print "Upper Threshold:",Upper_Thresh
#     print "Lower Threshold:",Lower_Thresh
    #print final
    
    #Quantization
    csv_list=[]
    for i in range(0,len(final)):
        if final[i] >= Upper_Thresh:
            csv_list.append(1)
        elif final[i] <= Lower_Thresh:
            csv_list.append(0)
    
#     #Create folder
#     if not os.path.exists(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName):
#         os.makedirs(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName)
    
    #Prepare List for hash function
    listForHash=[]
    for item in csv_list:
        listForHash.append(str(item))
    
#     print "List For Hash",listForHash
    #Output to CSV file
    outputCSVFile = open(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName+"A_"+str(Alpha)+"S_"+str(Num_Samples)+".csv",'wb')
    wr = csv.writer(outputCSVFile,quoting=csv.QUOTE_ALL)
    wr.writerow(csv_list)
    outputCSVFile.close()
    csvfile.close()
    
    #Output to ASCII file for NIST Analysis
    outputASCIIFile = open(os.getcwd()+os.sep+"Output_Data"+os.sep+OpenName+"A_"+str(Alpha)+"S_"+str(Num_Samples)+".dat",'w')
    for item in csv_list:
#         print item
        outputASCIIFile.write(str(item))
#     binData = 'f'*len(csv_list)
#     bin=st.pack(binData,*csv_list)
#     print(bin)
#     outputBINFile.write(bin)
    outputASCIIFile.close()
#     print listForHash
    ransom=''.join(listForHash)
#     print "Key:",ransom
    m=hl.sha256()
    m.update(ransom)
#     print "SHA256:",(m.hexdigest())

    
#     hashList(ransom)
    print "======================================="        