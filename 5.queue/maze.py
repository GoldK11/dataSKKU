# 2015311588 김결 미로찾기 과제


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

def readMaze(file):
    f = open(file, 'r')

    global start
    global final
    global data
    
    data=[]

    while True:
        line = f.readline().strip()
        if not line:
            break
        data.append(line)
    x=len(data)
    y=len(data[0])
    maze = []
    for i in range (x):
        for j in range (y):
            if data[i][j] == "O":
                start = (i,j)
            elif data[i][j] == " ":
                maze.append((i,j))
            elif data[i][j] == "G":
                final = (i,j)
    f.close()

    return maze

def findPath(maze,stack):
    st = Stack()
    now = start
    go = True
    re = []

    stack.push(start)

    while go:
        for i in [(now[0],now[1]-1),(now[0],now[1]+1),(now[0]-1,now[1]),(now[0]+1,now[1])]:
            if i ==final:
                go = False
            elif i in maze:
                st.push(i)
                maze.remove(i)
        if go:        
            now = st.pop()
        else:
            break
        p=stack.peek()
        
        yes = True
        while yes:
            if now in [(p[0],p[1]-1),(p[0],p[1]+1),(p[0]-1,p[1]),(p[0]+1,p[1])]:
                yes= False
            else:
                re.append(stack.pop())
                p=stack.peek()        
        stack.push(now)

    x=len(data)
    y=len(data[0])        
    for i in range (x):
        for j in range (y):
            if (i,j) in stack.items:
                data[i]=data[i][:j]+"0"+data[i][j+1:]
            elif (i,j) in re:
                data[i]=data[i][:j]+"."+data[i][j+1:]
    maze = data
    
    return maze

def printMaze(maze):
    for line in maze:
        for ch in line:
            print(ch,end='')
        print()


def printPath(stack):
    for item in stack.items:
        print(item,'-> ',end='')
    print('Goal')


maze = readMaze("mazeTest5.txt")
s = Stack()
printMaze(findPath(maze,s))
printPath(s)
