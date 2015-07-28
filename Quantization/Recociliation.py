import hashlib as hl
import itertools as it



def reconcil(list1,list2):
        
    
    #Initialize SHA256 Hash Algorithm
    ha=hl.sha256()
    hb=hl.sha256()
    
    #Input values and get the hash value in string format
    ha.update(' '.join(str(x) for x in list1))
    hb.update(' '.join(str(x) for x in list2))
    hasha=ha.hexdigest()
    hashb=hb.hexdigest()
    
    #Hash value 
    print hasha,'\n',hashb
        
    if len(list1)==1:
        if list1==list2:
            return ''.join(str(x) for x in list1)
        else:
            return ''
    else:            
        #Compare Hash Values:
        if (hasha==hashb):
            return ''.join(str(x) for x in list1)
        else:
        #Slice lists and replace original lists
            list1a=list1[0:len(list1)/2]
            list1b=list1[len(list1)/2:]
            list2a=list2[0:len(list2)/2]
            list2b=list2[len(list2)/2:]
            
        #Print out sliced lists
        print "list1a",list1a,'\n',"list2a",list2a,"\n","list1b",list1b,'\n',"list2b",list2b
        return (reconcil(list1a, list2a))+(reconcil(list1b, list2b))
           
        
#Sample lists for testing
a=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0]
b=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1]
c=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1]
d=[1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1]
#Execute reconciliation function
print (reconcil(a,b))

