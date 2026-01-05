class Solution:
    def twoSum(self, nums:List[int], target:int)-> List[int]:
        #sample array nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 9
        #return indices of pair of numbers that adds up to the target
        #Warning:  must no use the same element twice
        h={} # hashmap
        for i in range(len(nums)):
            h[nums[i]]=i #This uses the value from the nums array (at the current index i) as the key in the hash map h, and sets its corresponding value in the hash map to the current index i. 

        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i, h[y]]

#This is a O(n) - very efficient and less time complexity solution
