from typing import List, defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.helper(nums1, nums2)
        else:
            return self.helper(nums2, nums1)

    def helper(self, smaller_list: List[int], bigger_list: List[int]) -> List[int]:
        smaller_list_counter = defaultdict(int)
        smaller_list_counter_orig = defaultdict(int)

        for num in smaller_list:
            smaller_list_counter[num] += 1
            smaller_list_counter_orig[num] += 1

        for num in bigger_list:
            smaller_list_counter[num] -= 1

        result = []
        for num, count in smaller_list_counter.items():
            if count <= 0:
                to_add = [num] * smaller_list_counter_orig[num]
                result.extend(to_add)

        return result

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2]
    nums2 = [1, 1]

    result = solution.intersect(nums1, nums2)
    print(result)
