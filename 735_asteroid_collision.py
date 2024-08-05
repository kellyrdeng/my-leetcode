class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            should_add = True

            while stack and stack[-1] > 0 and a < 0: #collision, pop and update stack continuously until no collision
                peek = stack[-1]

                if abs(peek) < abs(a): #asteroid destroys top
                    stack.pop()
                    should_add = True
                elif abs(peek) > abs(a): #top destroys astroid
                    should_add = False
                    break
                else: #both destroyed
                    stack.pop()
                    should_add = False
                    break
                    
            if should_add:
                    stack.append(a)

        return stack
