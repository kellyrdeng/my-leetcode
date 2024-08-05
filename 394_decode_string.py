class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                #iterate until '[' to get substring
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring #insert popped at beginning of string
                stack.pop() #pop opening bracket

                #iterate while not empty and peek is numeric to get multiplier
                multiplier = ''
                while stack and stack[-1].isnumeric():
                    multiplier = stack.pop() + multiplier

                #add multiplied substring into stack
                stack.append(int(multiplier) * substring)
            else:
                stack.append(char)

        return ''.join(stack)
