"""
Count of smaller numbers
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""

class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        superNums = []
        global results
        results = [0] * len(nums)
        for i in xrange(len(nums)):
            superNums.append((i,nums[i]))
        def merge(left, right):
            l = 0
            r = 0
            merged = []
            global results
            accu = 0
            while l < len(left) and r< len(right):
                if left[l][1] > right[r][1]:
                    merged.append(right[r])
                    r += 1
                    accu += 1
                else:
                    merged.append(left[l])
                    results[left[l][0]] += accu
                    l += 1
            if l < len(left):
                for one in left[l:]:
                    results[one[0]] += accu
                merged += left[l:]
            else:
                merged += right[r:]
            return merged
        def mergeSort(target):
            if len(target) < 2:
                return target
            mid = len(target) / 2 
            return merge(mergeSort(target[:mid]), mergeSort(target[mid:]))
        mergeSort(superNums)

        return results
