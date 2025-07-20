'''
Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.
'''

class Solution:
    def maxScore(self, cardScore, k):
        n = len(cardScore)
        total_sum = 0
        for i in range(k):
            total_sum += cardScore[i]
        maxsum = total_sum
        l = k - 1
        r = n - 1
        while l >= 0:
            total_sum = total_sum - cardScore[l] + cardScore[r]
            maxsum = max(maxsum, total_sum)
            l -= 1
            r -= 1
        return maxsum
        
obj = Solution()
ans = obj.maxScore([5, 4, 1, 8, 7, 1, 3 ],3)
print(ans)

