
# coding: utf-8

# In[2]:


def mergeSort(l):
    print("List: ",l)
    if len(l)>1:
        mid = len(l)//2
        left=l[:mid]
        right=l[mid:]
        
        mergeSort(left)
        mergeSort(right)
        merge(left,right,l)
        
def merge(l,r,a):
    i=0
    j=0
    k=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
        
    while i<len(l):
        a[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        a[k]=r[j]
        j+=1
        k+=1
    print('merge:',a)
                
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)    


# In[ ]:





# In[ ]:




