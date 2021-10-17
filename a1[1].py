class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         """
        :type nums: List[int]
        :rtype: int
        """
         hash_table = {}
         for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
         return hash_table.popitem()[0]
        