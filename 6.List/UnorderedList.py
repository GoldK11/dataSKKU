
# coding: utf-8

# In[20]:


from Node import *

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous= None
        found = False
        while not found:
            if current.getData() == item:
                found  = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

            
    def append(self,item):
        new = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(new)

    def insert(self,index,item):
        count = 0
        current = self.head
        previous = None
        while count != index:
            previous = current
            current = current.getNext()
            count += 1
        temp = Node(item)
        previous.setNext(temp)
        temp.setNext(current)
        
            
    
    def index(self,item):
        current = self.head
        pos = 0
        while current != None:
            if current.getData() == item:
                return pos
            else:
                current = current.getNext()
            pos += 1
    
    def pop(self,index):
        count = 0
        current = self.head
        previous = None
        while count != index:
            previous = current
            current = current.getNext()
            count += 1
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    
    def __str__(self):
        current = self.head
        s = ""
        while current != None:
            s = s + " " + str(current.getData())
            current = current.getNext()
        return s


# In[21]:


mylist = UnorderedList()
mylist.add(3)
mylist.add(5)
mylist.add(2)
print(mylist)


# In[22]:


mylist.size()


# In[23]:


mylist.remove(3)
print(mylist)


# In[24]:


mylist.size()


# In[25]:


mylist.add(41)
print(mylist)


# In[26]:


mylist.insert(2,90)


# In[27]:


mylist.index(90)


# In[28]:


print(mylist)


# In[29]:


mylist.insert(1,13)
print(mylist)


# In[30]:


mylist.index(2)


# In[31]:


mylist.index(5)


# In[32]:


mylist.pop(0)
print(mylist)


# In[33]:


mylist.append(78)


# In[34]:


print(mylist)


# In[36]:


mylist.append(13)


# In[37]:


print(mylist)


# In[38]:


mylist.pop(5)


# In[39]:


print(mylist)


# In[40]:


mylist.add(44)
print(mylist)


# In[ ]:




