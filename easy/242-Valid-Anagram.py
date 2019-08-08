class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = set(s)
        T = set(t)
        if S==T:
            num = 0
            for i in S:
                if s.count(i) == t.count(i):
                    num += 1
            if num == len(S):
                return True
            else:
                return False
        else:
            return Flase

ans = Solution()
print (ans.isAnagram("aacc", "ccaa"))

