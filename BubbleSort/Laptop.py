#Laptop Shop 

def bubblesort (alist):
    for passnum in range(len(alist)-1,0,-1):
                          for i in range (passnum):
                            if alist[i]>alist[i+1]:
                                temp = alist[i]
                                alist[i] = alist[i+1]
                                alist[i+1] = temp

alist = [800,400,500,600,200,150,500,200]
bubblesort(alist)
print(alist)
