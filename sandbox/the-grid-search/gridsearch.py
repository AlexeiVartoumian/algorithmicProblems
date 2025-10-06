import re


def gridSearch(G, P):
    print("hello")
    rows = len(G)
    col = len(G[0])

    row2 = len(P)
    col2 = len(P[0])
    ## iterate over everything and find matching chars
    ## initiate a qualified nested loop against P
    # if third loop completes return YES
    for i in range(rows):
        for j in range(col):

            if G[i][j] == P[0][0] :
              
                basex = i-1
                
                
                hold = True
                for ii in range(row2):
                    basex += 1
                    basey = j - 1
                    if not hold :
                        break
                    for jj in range(col2):
                        
                        basey += 1
                       
                        if not basex < rows or not basey < col :
                            hold = False
                            break
                        if not G[basex][basey] == P[ii][jj] :
                            
                            hold = False
                            break
                        
                        #print(G[basey][basex] ,P[jj][ii] )
                if hold:
                    return "YES"
              
    return "NO"
            
print(gridSearch(['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137'], ['99','99']
))
            




# # '7283455864', 
# # '6731158619', 
# # '8988242643', 
# # '3830589324', 
# # '2229505813', 
# # '5633845374', 
# # '6473530293', 
# # '7053106601', 
# # '0834282956', 
# # '4607924137']
# #['9505', '3845', '3530']