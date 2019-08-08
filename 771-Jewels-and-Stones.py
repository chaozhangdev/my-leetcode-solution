
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
class Solution:
    def numJewelsInStones(J: str, S: str) -> int:
        count = 0
        J = set(J)
        for word in J:
            count += S.count(word)
        return count

x = Solution.numJewelsInStones("aA","aAAbbbb")
print (x)

