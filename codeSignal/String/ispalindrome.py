"""
check if string is palindrome. split into two take into account if length string si odd or even. symmetric count.
"""



def solution(inputString):
    
    if len(inputString) == 1:
        return True
    if len(inputString) % 2 == 0:
        
        left = inputString [:len(inputString)//2:]
        right = inputString [len(inputString)//2:]
        lcount = 0
        rcount = len(right)-1
        
        while lcount < len(left) and rcount< len(right):
            
            if left[lcount] != right[rcount]:
                return False
            
            lcount+=1
            rcount-=1
        return True 
    else:
        left = inputString [:len(inputString)//2:]
        right = inputString [(len(inputString)//2)+1:]
        
        lcount = 0
        rcount = len(right)-1
        
        while lcount < len(left) and rcount< len(right):
            
            if left[lcount] != right[rcount]:
                return False
            
            lcount+=1
            rcount-=1
        return True 