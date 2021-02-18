"""Perfect Number
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        
        # every number including of 1 for positive divisor
        aggregated = set([1])
        
        for divisor in range(2, int(num**0.5)+1):
            # search positive divisors
            if num % divisor == 0:
                _divisor = num // divisor
                aggregated.add(divisor)
                aggregated.add(_divisor)
        return sum(list(aggregated)) == num
