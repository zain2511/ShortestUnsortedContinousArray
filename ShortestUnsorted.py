class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if nums == sorted(nums):
            return 0
        else:
            while nums[i] == min(nums[i:len(nums)]):
                if i != len(nums) - 1:
                    i = i+1
                else:
                    return 0
            j = len(nums) - 1
       
            while nums[j] == max(nums[0:j + 1]):
                j = j - 1
            return j - i + 1