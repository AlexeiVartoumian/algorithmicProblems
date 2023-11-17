"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

example 
ranked = [100,90,90,80]
player [70,80,105]

The ranked players will have ranks 1,2 , 2, and 3, respectively. If the player's scores are 70,80  and ,105 their rankings after each game are 4th, 3rd and . Return [4,3,1].
Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score
Input Format

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers , ranked[i]the leaderboard scores in decreasing order.
The next line contains an integer, m, the number games the player plays.
The last line contains m space-separated integers player[j], the game scores.
"""

"""
my approach was to iterate through the rankings and store the values with the rank as key and ranked[i] as value.
after that reverse binary search each value in this dictionary checking by key where its respective rank is.I say reverse bin search because low is the last assigned rank and high is 1 since ranked is sorted descending. the problem statement was ambiguous enough for me to at first assume that a given players score will update the ranked array as would a normal arcade game which required me to change my implmentation but this not the case the rankings are in place.
"""

def climbingLeaderboard(ranked, player):
    # Write your code here
    rankings = {}
    rank = 1
    seen = set()
    for i in range(len(ranked)):
        
        if ranked[i] not in seen:
            seen.add(ranked[i])
            rankings[rank] = ranked[i]
            rank+=1
    rank -=1
    results = []
    def binsearch(rankings,value):
        
        if value >= rankings[1]:
            return 1
        if value < rankings[rank]:
            return rank+1
        low = 1
        high = rank
        while low <= high:
            
            mid = int( (low + high)/2)
            if rankings[mid] == value or (value > rankings[mid] and value < rankings[mid+1]):
                return mid
            elif value < rankings[mid] and value > rankings[mid+1]:
                return mid+1
            
            if value > rankings[mid]:
                high = mid -1
            else:
                low = mid+1
            
    for i in range(len(player)):
        results.append(binsearch(rankings,player[i]))
    return results