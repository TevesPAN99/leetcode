class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer=[1]*n

        frontanswer = 1
        for i in range(n):
            answer[i]=frontanswer
            frontanswer*=nums[i]
        
        behindanswer = 1
        for i in range(n-1,-1,-1):
            answer[i]*=behindanswer
            behindanswer*=nums[i]
        
        return answer