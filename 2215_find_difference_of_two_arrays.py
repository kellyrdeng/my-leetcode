class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        set1, set2 = set(nums1), set(nums2)

        answer.append(list(set1.difference(set2)))
        answer.append(list(set2.difference(set1)))
        
        return answer
