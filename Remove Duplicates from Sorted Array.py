class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        cnt=1
        for i in range (0,len(nums)):
            if (nums[i]!=nums[j]):
                j+=1
                nums[j] = nums[i]
                cnt+=1
        return cnt
