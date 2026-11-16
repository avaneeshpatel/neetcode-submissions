class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)-1):
            if temperatures[i] < temperatures[i+1]:
                result[i] = 1
                while len(stack) > 0:
                    index = stack[-1]
                    if temperatures[index] < temperatures[i+1]:
                        result[index] = i+1 - index
                        stack.pop(-1)
                    else:
                        break                
            else:
                stack.append(i)
        return result

        