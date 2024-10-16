from typing import List, Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic = Counter(nums1)

        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1

        return res

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2]
    nums2 = [1, 1]

    result = solution.intersect(nums1, nums2)
    print(result)
