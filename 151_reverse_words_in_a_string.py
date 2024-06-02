class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        lst = list(filter(lambda x: x != '', lst))
        left, right = 0, len(lst) - 1
        

        while left < right:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp
            
            left += 1
            right -= 1

        return ' '.join(lst)
