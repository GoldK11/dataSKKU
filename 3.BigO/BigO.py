from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]
        
def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]
    
def test4():
    l = list(range(1000))
    
    
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


def anagramSolution1(s1,s2):
    alist = list(s2)
    count = 0
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            count +=1
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    print('solutioin1:',count)
    return stillOK

print(anagramSolution1('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm'))

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    count = 0 

    while pos < len(s1) and matches:
        count +=1
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    print('solution2:',count)
    return matches



print(anagramSolution2('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm'))


def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    count = 0
    
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        count +=1
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False
            
    print('solution3:',count)
    return stillOK

print(anagramSolution4('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm'))


t1 = Timer("anagramSolution1('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm')","from __main__ import anagramSolution1")
print("Solution1:",t1.timeit(number=1000))
t2 = Timer("anagramSolution2('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm')","from __main__ import anagramSolution2")
print("Solution2:",t1.timeit(number=1000))
t4 = Timer("anagramSolution4('abxbscdefzokokzmsltlwxxmm','mabxkctwdebzmxfzookllssxm')","from __main__ import anagramSolution4")
print("Solution4:",t1.timeit(number=1000))
