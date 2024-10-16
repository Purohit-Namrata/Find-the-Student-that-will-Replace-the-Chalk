from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum=0
        n=len(chalk)
        for i in range(n):
            sum+=chalk[i]
        chalkForLastRound=(k%sum)

        for i in range(n):
            if chalkForLastRound<chalk[i]:
                return i
            chalkForLastRound-=chalk[i]

        return -1
s=Solution()
print(s.chalkReplacer([5,1,5],22))
    