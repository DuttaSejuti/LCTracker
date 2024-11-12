# TC: O(NlogN + MlogM)
# SC: O(M) => m is the size of the queries
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # O(nlogn)
        items.sort(key = lambda x : x[0]) # sort items in terms of the first element price

        # we are storing the query and it's position as an array (query, index)
        # so that after sorting the queries, we still know the order, we need this for result
        # because result needs to maintain the same order as the given queries
        # O(m)
        query_list = list()
        for i in range(len(queries)):
            query_list.append([queries[i], i])
        # O(mlogm)
        query_list.sort(key = lambda x: x[0])

        result = [0]*len(queries)
        # this query_beauty will store the maximum beauty possible for a query, so that we do not need to
        # revisit the same item twice
        query_beauty = list()
        i = 0
        max_beauty = 0

        # O(n+m) => each query and item is traversed only once
        for query in query_list:
            if len(query_beauty) > 0:
                max_beauty = query_beauty[-1] # the last max_beauty encountered so far 
            while i < len(items):
                if items[i][0] > query[0]:
                    break
                max_beauty = max(max_beauty, items[i][1])
                i += 1
            result[query[1]] = max_beauty # placing the result maintaing the order of queries
            query_beauty.append(max_beauty)

        return result
                