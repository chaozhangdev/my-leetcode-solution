class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {}
        lists = list(s)
        print (lists.index('V'))
        sum = 0
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        if (lists.index('I')<lists.index('V')):
            hashmap['I'] *= (-1)
        if (lists.index('X')<lists.index('L')) or (lists.index('X')<lists.index('C')):
            hashmap['X'] *= (-1)
        if (lists.index('I')<lists.index('V')):
            hashmap['I'] *= (-1)
        print (hashmap)
        return sum

ans = Solution()
print (ans.romanToInt("LVIII"))
