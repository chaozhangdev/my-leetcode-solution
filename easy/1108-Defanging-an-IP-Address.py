class Solution:
    def defangIPaddr(address: str) -> str:
        new_address = address.replace('.','[.]')
        return new_address
x = Solution.defangIPaddr("255.100.50.0")
print (x)

