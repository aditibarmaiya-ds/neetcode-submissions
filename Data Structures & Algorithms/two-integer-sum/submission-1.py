class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remaning = target - nums[i]
            if remaning in hashmap:
                return [hashmap[remaning],i]
                
            hashmap[nums[i]] =i    
     
                  
                

        
        