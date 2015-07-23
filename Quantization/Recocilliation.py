import hashlib as hl

def reconcil(list1,list2):
    list1a=list1[0:len(list1)/2]
    list1b=list1[len(list1)/2:]
    list2a=list2[0:len(list2)/2]
    list2b=list2[len(list2)/2:]
    
    
    
a=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0]
b=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1]
reconcil(a,b)