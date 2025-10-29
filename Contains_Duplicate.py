# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num]=1
        return False 

#  O(N)   TIME COMPLEXITY