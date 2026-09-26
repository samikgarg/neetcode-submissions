class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1], len(temperatures) - 1)]
        results = [0] * len(temperatures)

        for i in range (2, len(temperatures) + 1):
            curr_index = len(temperatures) - i
            curr_temp = temperatures[-i]
            prev_temp, prev_index = stack.pop()
            to_continue = True
            while prev_temp <= curr_temp:
                if len(stack) == 0:
                    stack.append((curr_temp, curr_index))
                    to_continue = False
                    break
                else:
                    prev_temp, prev_index = stack.pop()
            if to_continue:
                results[-i] = prev_index - curr_index
                stack.append((prev_temp, prev_index))
                stack.append((curr_temp, curr_index))
        
        return results


