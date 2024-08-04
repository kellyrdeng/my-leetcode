class Solution:
    def removeStars(self, s: str) -> str:
    #STACK SOLUTION (beats 30%)
        # stack = []

        # for char in s:
        #     if char != '*':
        #         stack.append(char)
        #     else:
        #         stack.pop()

        # return ''.join(stack)

    #TWO POINTER
        j = 0 #i represents traversal, j lags behind and adds chars
        lis = list(s)
 
        for i in range(len(lis)):
            if lis[i] == '*':
                j -= 1
            else:
                lis[j] = lis[i]
                j += 1
        
        return ''.join(lis[:j])
