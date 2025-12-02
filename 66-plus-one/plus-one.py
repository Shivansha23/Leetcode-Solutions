class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        n= num + 1
        d= [int(i) for i in str(n)]
        return d

        
        