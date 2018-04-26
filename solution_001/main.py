class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:  
            return False  
        buff_dict = {}  
        for i in range(len(nums)):  
            if nums[i] in buff_dict:  
                return [buff_dict[nums[i]], i]  
            else:  
                buff_dict[target - nums[i]] = i



if __name__ == '__main__':
    S = Solution()
    L = S.twoSum([3, 4, 5, 9, 12, 7], 16)
    print L
        
