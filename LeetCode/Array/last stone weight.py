"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""




def lastStoneWeight(self, stones: List[int]) -> int:
            if len(stones) ==0:
                return 0
            if len(stones) == 1:
                return 1
            while len(stones)>1:
                stones.sort()
                s1,s2=stones[-1],stones[-2]
                if s1==s2:
                    stones.pop(-1)
                    stones.pop(-1)
                else:
                    s1 = abs(s1-s2)
                    stones.pop(-1)
                    stones[-1] = s1
            if len(stones):
                return stones[-1]
            return 0