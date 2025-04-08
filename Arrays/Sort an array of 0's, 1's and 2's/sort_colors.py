# Leetcode 75 - Sort Colors
# Dutch National Flag Algorithm
# Time: O(n), Space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0
        oneCount = 0
        twoCount = 0

        for i in range(0,len(nums)):
            if nums[i]==0:
                zeroCount+=1
            elif nums[i]==1:
                oneCount+=1
            else:
                twoCount+=1
        
        j=0
        while zeroCount:
            nums[j]=0
            j+=1
            zeroCount-=1
        
        while oneCount:
            nums[j]=1
            j+=1
            oneCount-=1
        
        while twoCount:
            nums[j]=2
            j+=1
            twoCount-=1

