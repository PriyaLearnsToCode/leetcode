from typing import List
from colorama import Fore, Back, Style

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        # Initialize a lookup that will store the index of the pair element
        # Eg. if 2 is at index 0, target is 9, then stores 7 -> 0
        lookup = {}
        
        # Iterate through the elements
        # The function terminates when a pair is found
        for i in range(len(nums)):
            # print(f"{lookup}, {i}, {nums[i]}, {target - nums[i]}")
            if nums[i] in lookup:
                return [lookup[nums[i]],i]
            lookup[target - nums[i]] = i
        return None

try:
    solution = Solution()
    print(Style.BRIGHT + "Checking 2Sum")
    assert(solution.twoSum([2, 7, 11, 3], 9) == [0, 2])
    print(Fore.WHITE + Back.GREEN + "Solution is correct")
except:
    print(Fore.WHITE + Back.RED + "Solution is incorrect")

        
    
        