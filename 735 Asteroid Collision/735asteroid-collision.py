class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            flag = False

            while (len(stack) != 0 and stack[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i]) >= stack[-1]):
                if (abs(asteroids[i]) == stack[-1]):
                    stack.pop()
                    flag = True
                    break
                
                stack.pop()
            
            if ((flag == True) or (len(stack) != 0 and asteroids[i] < 0 and stack[-1] > abs(asteroids[i]))):
                continue
            
            stack.append(asteroids[i])
        
        return stack