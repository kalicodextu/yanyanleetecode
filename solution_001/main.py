class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = dict()
        for i in xrange(len(nums)):
            a[nums[i]] = i
        key = target/2
        for x in a.iterkeys():
            if x > key:
                continue
            for y in a.iterkeys():
                if y < key:
                    continue
                if x+y == target:
                    index1 = a[x]
                    index2 = a[y]
                    if index1>index2:
                        return [index2, index1]
                    else:
                        return [index1, index2]

if __name__ == '__main__':
    S = Solution()
    L = S.twoSum([3, 4, 5, 9, 12, 7], 16)
    print L
        
