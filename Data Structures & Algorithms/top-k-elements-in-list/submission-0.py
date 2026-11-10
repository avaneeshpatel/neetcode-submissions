class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num,0)+1
        result = []
        values = list(count_dict.values())
        values.sort(reverse=True)
        consider_values = values[:k]
        for key in count_dict.keys():
            if count_dict[key] in consider_values:
                result.append(key)
        return result
        