class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      i = j = 0
      sorted = []
      
      # merge two sorted arrays
      while i < len(nums1) and j < len(nums2):
          if nums1[i] < nums2[j]:
              sorted.append(nums1[i])
              i += 1
          else:
              sorted.append(nums2[j])
              j += 1

      while i < len(nums1):
          sorted.append(nums1[i])
          i += 1

      while j < len(nums2):
          sorted.append(nums2[j])
          j += 1
      
      # odd number of length of sorted array
      if len(sorted) % 2 == 1:
          return sorted[len(sorted)//2]
        
      # even number of length of sorted array
      else:
          return (sorted[int(len(sorted)/2-1)] 
