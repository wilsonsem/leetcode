class Solution:
    
    def two_sum(self, nums, target):
        complementMap = dict()
        
        for i in range(len(nums)):
            complement = target - num[i]
            num = num[i]
            if num in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i
                
                   
    def two_sum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]