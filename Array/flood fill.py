"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""


def floodFill( image ,sr, sc,color):
        """
        alist = [       #--> 
        [1,1,1],  #  [2,2,2]
        [1,1,0],  #  [2,2,0]
        [1,0,1]]  #  [2,0,1]
        """
        if image[sr][sc]== color:
            return image
        visited = []
        for i in range(len(image)):
            visited.append([-1] * len(image[0]))
        thingy=image[sr][sc]
        image[sr][sc] = color
        visited[sr][sc] = color
        start = (sr,sc)
        component = [start]
        cur = 0
        tempi =sr 
        tempj =sc
    
        while cur < len(component):
        
            #go left
            for i in range(tempj,-1,-1):
            
                if image[tempi][i] != thingy and image[tempi][i] != color:
                    break
                elif i != tempj and image[tempi][i] == color:
                    break
                elif image[tempi][i] == thingy  and visited[tempi][i]== -1:
                    visited[tempi][i]= color
                    image[tempi][i] = color
                    component.append((tempi,i))
        
        #go right
            for i in range(tempj,len(image[sr])):
                if image[tempi][i] != thingy and image[tempi][i] != color:
                    break
                elif i != tempj and image[tempi][i] == color:
                    break
                elif image[tempi][i] == thingy  and visited[tempi][i]== -1:
                    visited[tempi][i]= color
                    image[tempi][i] = color
                    component.append((tempi,i))
        
        #go up
            for i in range(tempi,-1,-1):
                if image[i][tempj] != thingy and image[i][tempj] != color:
                    break
                elif i != tempi and image[i][tempj] == color:
                    break
                elif image[i][tempj] == thingy  and visited[i][tempj]== -1:
                    visited[i][tempj]= color
                    image[i][tempj] = color
                    component.append((i,tempj))
        
        
        #go down
            for i in range(tempi,len(image)):
                if image[i][tempj] != thingy and image[i][tempj] != color:
                    break
                elif i != tempi and image[i][tempj] == color:
                    break
                elif image[i][tempj] == thingy  and visited[i][tempj]== -1:
                    visited[i][tempj]= color
                    image[i][tempj] = color
                    component.append((i,tempj))
        
            cur +=1
            if cur == len(component):
                break
            tempi = component[cur][0]
            tempj = component[cur][1]
        return image

alist = [       #--> 
        [1,1,1],  #  [2,2,2]
        [1,1,0],  #  [2,2,0]
        [1,0,1]]  #  [2,0,1]
def floodfill(image,sr,sc,color):

    height = len(image)
    width = len(image[0])

    oldcolour = image[sr][sc]

    def dfs(image,sr,sc,oldcolour):

        if sr >= 0 and sr < height and sc >= 0 and sc < width and image[sr][sc] == oldcolour:
            image[sr][sc] = color
        
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for i in range(len(directions)):

                dfs(image, sr+directions[i][0],sc+directions[i][1],oldcolour)
    
    dfs(image,sr,sc,oldcolour)

    return image

print(floodfill(alist,1,1,2))