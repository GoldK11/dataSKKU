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
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def readMaze(f):
    '''미로 파일을 읽어들여서 리스트로 저장 및 리턴'''
    maze = []
    temp = []
    f = open(f,"r")
    lines = f.readlines()

    for line in lines:
        for ch in line:
            temp.append(ch)
            
        maze.append(temp)
        temp=[]
        
    f.close()
    return maze

def printMaze(maze):
    '''미로 맵을 출력한다'''
    for line in maze:
        for ch in line:
            print(ch,end='')

def printPath(stack):
    '''미로의 길을 좌표로 출력한다. 시작점은 (1,0)'''
    for item in stack.items:
        print(item,'-> ',end='')
    print('Goal')

def findPath(maze,stack):
    '''주어진 미로 맵에서 시작점부터 출구까지의 길을 stack에 담아 돌려준다'''
    
    stack.push((1,0))                      #시작점은 항상 1,0    

    while True:
        curX, curY = stack.peek()          #현재위치 x,y        
        
        eastChar = maze[curX][curY+1]      #동쪽 문자
        westChar = maze[curX][curY-1]      #서쪽 문자
        southChar = maze[curX+1][curY]     #남쪽 문자
        northChar = maze[curX-1][curY]     #북쪽 문자        

        if eastChar =='G' or westChar == 'G' or southChar == 'G' or northChar == 'G':
            break

        elif eastChar == ' ':            
            stack.push((curX, curY+1))
            maze[curX][curY+1] = 'O'            

        elif westChar == ' ':            
            stack.push((curX, curY-1))
            maze[curX][curY-1] = 'O'
           
        elif southChar == ' ':            
            stack.push((curX+1, curY))
            maze[curX+1][curY] = 'O'
            

        elif northChar == ' ':            
            stack.push((curX-1, curY))
            maze[curX-1][curY] = 'O'            

        else:
            maze[curX][curY] = '.'
            stack.pop()            

    return maze

        
     
maze = readMaze('mazeTest1.txt')
stack = Stack()
printMaze(findPath(maze,stack))
printPath(stack)
