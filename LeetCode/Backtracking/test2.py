
maze = ['+-++++++++',
'+-++-+++++',
'+-------++',
'+-++-++-++',
'+-++-++-++',
'+-++-++-++',
'++++-++-++',
'+--------+',
'++++++++++',
'----------']
string = "CALIFORNIA;LASVEGAS;NIGERIA;CANADA;TELAVIV;ALASKA"
#arr = ['ICELAND', 'MEXICO', 'PANAMA', 'ALMATY']
def crosswords(maze, string):
    #step 1 is to generate possible
    #word placements with dfs either it can go down
    #or it can go right
    directions = [(1,0),(0,1)] 
    downvisited = set()
    rightvisited = set()
    positions = []
    height = 10
    width = 10
    def inbounds(i,j):
        if i >= 0 and i < height and j >= 0 and j < width:
            return True
        return False
    def downwards(i,j,length, start):
        while inbounds(i+length,j) and maze[i+length][j] == "-":
            downvisited.add((i+length,j))
            length +=1
        endcoord = ((i+length )-1, j)
        return (start, endcoord,"D",length-1)
    def rightwards(i,j,length,start):
        while inbounds(i,j+length) and maze[i][j+length] == "-":
            rightvisited.add((i,j+length))
            length +=1
        endcoord = (i, (j+length)-1)
        return (start, endcoord,"R",length-1)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "-":
                if (i,j) not in downvisited:
                    startcoord = (i,j)
                    if inbounds(i+1,j) and maze[i][j] == "-":
                        if maze[i+1][j] == "-":
                            positions.append(downwards(i,j,0,startcoord))
            if (i,j) not in rightvisited:
                    startcoord = (i,j)
                    if inbounds(i,j+1) and maze[i][j] == "-":
                        if maze[i][j+1] == "-":
                            positions.append(rightwards(i,j,0,startcoord))
    #print(positions)
    arr = string.split(";")
    #print(len(positions),len(arr),arr)
    permutations = set()
    def backtrack(start,arr):
        
        if len(arr) == start:
            permutations.add(tuple(arr))
        for i in range(start,len(arr)):
            arr[i],arr[start] = arr[start],arr[i]
            backtrack(start+1,arr)
            arr[start],arr[i] = arr[start],arr[i]
        
      
    backtrack(0,arr)
    permutations = [list(perm) for perm in permutations ]
    #print(permutations,len(permutations))
    #[positions,permutations]
    def final(arr,maze,coords):
        def filldown(start, end, word,maze,length):
            i,j = start
            count = 0
            while count <= length:
                if maze[i][j] == "-":
                    temp = maze[i][:j:] + word[count] + maze[i][j+1::]
                    maze[i]= temp
                    i+=1
                elif maze[i][j] == word[count]:
                    i+=1
                else:
                    return False
                count+=1
            
            return maze
        def fillright(start,end,word,maze,length):
            i,j = start
            count = 0
            while count <= length:
                if maze[i][j] == "-":
                    temp = maze[i][:j:] + word[count] + maze[i][j+1::]
                    maze[i]=temp
                    j+=1
                elif maze[i][j] == word[count]:
                    j+=1
                else:
                    return False
                count+=1
            
            return maze
        def combo(coords,maze,arr):
            for i in range(len(coords)):
                scord, end, direction, length = coords[i]
                if direction == "D" and len(arr[i]) == length+1:
                    update = filldown(scord, end, arr[i], maze, length )
                    if update == False:
                        return False
                    else:
                        maze == update
                elif direction == "R" and len(arr[i]) == length+1:
                    update = fillright(scord, end, arr[i], maze, length)
                    if update == False:
                        return False
                    else:
                        maze = update
                else:
                    return False
            return maze
        for i in permutations:
            poss = combo(coords,maze.copy(),i)
            if poss != False:
                print(poss)
                return poss
    final(permutations,maze,positions)


print(crosswords(maze,string))