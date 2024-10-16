class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        new_list = [(a, 'a'), (b, 'b'), (c, 'c')]
        max_heap = [(-val, char) for val, char in new_list if val > 0]
        heapq.heapify(max_heap)
        last_char = ''
        
        while max_heap:
            max_val, char = heapq.heappop(max_heap)
            max_val = - max_val
            if char != last_char:
                char_cnt = min(max_val, 2)
                ans += char * char_cnt
                max_val -= char_cnt

                last_char = char
            else:
                if not max_heap:
                    break
                second_max_val, second_char = heapq.heappop(max_heap)
                second_max_val = - second_max_val
                ans += second_char
                second_max_val -= 1
                last_char = second_char
                if second_max_val > 0:
                    heapq.heappush(max_heap, (-second_max_val, second_char))
            if max_val > 0:
                heapq.heappush(max_heap, (-max_val, char))
        
        return ans

        