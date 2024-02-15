class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #TC: O(n); Bucket Sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # TC: O(nlogn), SC:O(n+k)
        # new_dict = dict()
        # result_list = list()
        # for num in nums:
        #     new_dict[num] = new_dict.get(num, 0) + 1
        # new_dict = dict(sorted(new_dict.items(), key = lambda x:x[1], reverse = True))
        # print(new_dict)
        # ke = list(new_dict.keys())
        # for i in range(k):
        #     result_list.append(ke[i])
        # return result_list

        # TC:O(n^2), SC:O(n)
        # result_list = list()
        # new_dict = dict()
        # for e in nums:
        #     new_dict[e] = new_dict.get(e, 0) + 1
        # ke = list(new_dict.keys())
        # v = list(new_dict.values())
        # while 1:
        #     item = v.index(max(v))
        #     final_item = ke[item]
        #     ke.pop(item)
        #     v.pop(item)
        #     result_list.append(final_item)
        #     if len(result_list) == k:
        #         break
        # return result_list