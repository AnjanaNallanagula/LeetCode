class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:        
        sum1 = sum(damage) - min(max(damage), armor) + 1
        
        return sum1