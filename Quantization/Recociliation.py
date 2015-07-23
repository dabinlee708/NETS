import hashlib as hl
import itertools as it

def reconcil(list1,list2):
    
    #Slice lists and replace original lists
    list1a=list1[0:len(list1)/2]
    list1b=list1[len(list1)/2:]
    list1=[list1a,list1b]
    
    list2a=list2[0:len(list2)/2]
    list2b=list2[len(list2)/2:]
    list2=[list2a,list2b]
    
    #Print out lists for validation
    print "lista:",list1a, list1b, list1
    print "listb:",list2a, list2b, list2
    
    
    #Initialize SHA256 Hash Algorithm
    ha1=hl.sha256()
    ha2=hl.sha256()
    hb1=hl.sha256()
    hb2=hl.sha256()
    
    #Input values and get the hash value in string format
    ha1.update(' '.join(str(x) for x in list1a))
    ha2.update(' '.join(str(x) for x in list1b))
    hb1.update(' '.join(str(x) for x in list2a))
    hb2.update(' '.join(str(x) for x in list2b))
    hasha1=ha1.hexdigest()
    hasha2=ha2.hexdigest()
    hashb1=hb1.hexdigest()
    hashb2=hb2.hexdigest()
    
    #Hash value 
    print hasha1,'\n',hasha2,'\n',hashb1,'\n',hashb2
    
    
    #Compare hash values
    if (hasha1==hashb1):
        it.chain.from_iterable()
    else:
        reconcil(list1[0],list2[0])
    if(hashb1==hashb2):
        
    else:
        reconcil(list1[1],list2[1])
        
        
        
#Sample lists for testing
a=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0]
b=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1]

#Execute reconciliation function
reconcil(a,b)


print a,b
