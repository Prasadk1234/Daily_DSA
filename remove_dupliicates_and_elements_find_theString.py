#remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Use two pointers approach
        i = 0  # Slow pointer

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

#remove-element
class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
      temp = []
      # a = val
      for i in nums:
          if i != val:
              temp.append(i)
      nums[:] = temp
      return len(nums)


#find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1



