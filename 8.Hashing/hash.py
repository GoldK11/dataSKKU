class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace


    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data, position

    def __getitem__(self,key):
        return (self.get(key))[0]

    def __setitem__(self,key,data):
        self.put(key,data)

    def __delitem__(self, key):
        d, p = self.get(key)
        self.data[p] = None
        self.slots[p] = None

    def __contains__(self, key):
        d, p = self.get(key)
        if d:
            return True
        else:
            return False
        
    def __len__(self):
        n = 0
        for i in self.slots:
            if i:
                n = n + 1
        return n

    def __str__(self):
        s = ''
        for i in range(self.size):
            if self.slots[i]:
                s = s + str(self.slots[i]) + ':' + self.data[i] + ','
        return s

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
del H[20]
print(20 in H)
print(17 in H)
print(len(H))
H[20]='duck'
print(H[20])
print(H[99])
print(H)
