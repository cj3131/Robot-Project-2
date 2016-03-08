#Phone Shop 

def bubblesort (alist):
    for passnum in range(len(alist)-1,0,-1):
                          for i in range (passnum):
                            if alist[i]>alist[i+1]:
                                temp = alist[i]
                                alist[i] = alist[i+1]
                                alist[i+1] = temp

alist = [500,400,100,300,200,400,200,500]
bubblesort(alist)
print(alist)
