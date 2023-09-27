"""
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

solution(image) = [[5, 4], 
                   [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.
"""


"""
im sure theres a way more optimal way to do this but i went about this by checking if a given co-ordinate is within  the bounds of a 3 by 3 matrix eg if co-ord is 0,0 then it cannot be the center of a matrix. after that my condition was to loop through 8 directions  append the values stored there and if the final length of these values is equal to 9 then we have a 3 by 3 matrix. for every j append to a temp list and at the end of the i append to final result if it exists.
"""

def solution(image):
    
    directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
  
    final = []
    
    height = len(image)
    width = len(image[0])    
    def dfs(i,j,results):
    
        if i >= 0 and i < height and j >=0 and j < width:
            
            results.append(image[i][j])
            return results
        else:
            return results
    
    
    for i in range(height):
        
        res = []
        for j in range(width):
            temp =[]
            temp.append(image[i][j])
            if i != 0 and j != 0 and i < height -1 and j < width -1:
                
                for d in directions:
                    xcord = i + d[0]
                    ycord = j + d[1]
                    dfs(xcord,ycord,temp)
                if len(temp) == 9:
                    res.append( sum(temp)//9)
            
        if res:
            final.append(res)
    
    return final