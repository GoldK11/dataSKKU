class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        
        if self.slots[hashvalue]==None:
            self.slots[hashvalue] = UnorderedList()
            
        self.slots[hashvalue].add(key,data) 

    def hashfunction(self,key,size):
        return key%size
    
    def get(self,key): 
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            return False
        else:
            return self.slots[hashvalue].getData(key)
    
    def __getitem__(self,key):
        return self.get(key)
    
        
    def __setitem__(self,key,data):
        self.put(key,data)
    

    def __delitem__(self,key):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            return False
        else:
            self.slots[hashvalue].remove(key)


    def __len__(self):
        n = 0
        for i in range(self.size):
            if self.slots[i] != None:
                current = self.slots[i].head
                while current != None:
                    n+=1
                    current = current.getNext()         
        return n
       
    def __contains__(self,key):
        contain = self.get(key)
        if contain:
            return True
        else:
            return False
        
    def __str__(self):
        s=""
        for i in range(self.size):
            if self.slots[i] != None:
                current = self.slots[i].head
                while current != None:
                    s += str(current.getKey())+":"+current.getData()+", "
                    current = current.getNext() 
            else:
                s+="None, "
        return s
    
class Node:
    def __init__(self,initkey,initdata):
        self.key = initkey
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getKey(self):
        return self.key
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def __str__(self):
        s=""
        current = self.head
        while current != None:
            s += str(current.getKey())+":"+current.getData()+", "
            current = current.getNext() 
        return s
    

class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self,key,item):
        temp = Node(key,item)
        current = self.head
        if current == None:
            self.head = temp
        else:
            while current.getNext()!=None:
                current = current.getNext()
            current.setNext(temp)

    def search(self,key): 
        current = self.head
        found = False
        while current != None and not found:
            if current.getKey() == key:
                found = True
            else:
                current = current.getNext()
        return found

    def getData(self,key):
        current = self.head
        while current != None:
            if current.getKey() == key:
                return current.getData()
            current = current.getNext()
    
    def remove(self,key): 
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getKey() == key:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
   
