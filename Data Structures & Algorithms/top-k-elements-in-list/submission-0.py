class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = {}

        for num in nums:
            if num in frequency_table:
                frequency_table[num] += 1
            else:
                frequency_table[num] = 1

        frequency_table_sorted = sorted(
            frequency_table.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []

        for i in range(k):
            result.append(frequency_table_sorted[i][0])

        return result