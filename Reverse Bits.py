class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:]
        a = a.zfill(32)
        a = a[::-1]
        return int(a,2)
        
