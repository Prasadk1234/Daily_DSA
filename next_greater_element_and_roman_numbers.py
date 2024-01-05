# next_greater_element
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {n: i for i, n in enumerate(nums1)}  # Createing a dict for indexing items in nums1 stack
        res = [-1] * len(nums1)  # reversing that stack for start form right to left

        stack = []  # declearing an empty stack
        for i in range(len(nums2)):  # entering in nums2 stack
            cur = nums2[i]  # storing an ith element in cur
            while stack and cur > stack[-1]:  # if the stack is not null then you will enter in this loop
                val = stack.pop()  # then pop the first item of the stack
                idx = nums1idx[val]  # store the idex of that item with the help of dict(nums1idx)
                res[idx] = cur  # ?
            if cur in nums1idx:  # if the cur values are present in nums1idx then
                stack.append(cur)  # append the the cur variable to stack
        return res  # then return the res variable

# roman_integer
class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
               'M': 1000}  # declearing an map or dict for roman numbers

        res = 0  # declearing result variable with 0

        for i in range(len(s)):  # entering in string
            if i + 1 < len(s) and rom[s[i]] < rom[
                s[i + 1]]:  # if string + 1 is less than length of string and in rom map
                # if string of rom is less than further string then subtract it
                res -= rom[s[i]]  # sub in process
            else:
                res += rom[s[i]]  # else we can add towards the result
        return res  # returning result
