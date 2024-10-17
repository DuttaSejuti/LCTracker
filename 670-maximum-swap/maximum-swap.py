class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [n for n in str(num)]
        max_val = -1
        max_idx = -1
        for i in range(len(num_list)):
            curr = num_list[i]
            for j in range(len(num_list)-1, i, -1):
                if num_list[j] > curr:
                    if int(num_list[j]) > int(max_val):
                        max_idx = j
                        max_val = int(num_list[j])
            if max_idx != -1:
                num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
                break

        return int(''.join(num_list))
