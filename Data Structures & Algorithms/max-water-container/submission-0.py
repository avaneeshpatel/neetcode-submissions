class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        start = 0
        end = len(heights)-1
        while start < end :
            index_gap = end - start
            min_h = min(heights[start],heights[end])
            max_water = max(max_water, min_h*index_gap)
            if heights[start]<heights[end]:
                 start += 1
            else:
                end -= 1
        return max_water   
        