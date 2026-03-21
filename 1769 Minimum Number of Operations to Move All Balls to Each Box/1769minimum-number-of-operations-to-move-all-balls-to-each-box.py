class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ls = [0 for i in range(len(boxes))]
        count = 0
        moves = 0

        for i in range(len(boxes)):
            ls[i] = count + moves
            moves += count
            count += int(boxes[i])
        
        count = 0
        moves = 0

        for i in range(len(boxes) - 1, -1, -1):
            ls[i] += (count + moves)
            moves += count
            count += int(boxes[i])
        
        return ls