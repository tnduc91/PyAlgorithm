def maxSubArray(nums) -> int:
        length = len(nums)
        max_ending = nums[0]
        max_so_far = nums[0]
        
        for i in range(1, length, 1):
            if (max_ending + nums[i] > nums[i]):
                max_ending += nums[i]
            else:
                max_ending = nums[i]
            
            if max_so_far < max_ending:
                max_so_far = max_ending
        
        
        
        return max_so_far

output = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print (output)