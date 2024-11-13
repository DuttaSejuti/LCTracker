class Solution:
    def custom_binary_search(self, items: List[List[int]], query_price: int) -> int:
        # Initialize binary search boundaries and the variable to track maximum beauty
        l, r = 0, len(items) - 1
        max_beauty = 0
        
        # Perform binary search to find the highest beauty for items under the query price
        while l <= r:
            mid = l + (r - l) // 2
            if items[mid][0] > query_price:
                # If the current item's price exceeds the query price, ignore current and right side
                r = mid - 1
            else:
                # If the current item's price is within the query price:
                # Update max_beauty and continue to the right to find potential higher beauties
                max_beauty = max(max_beauty, items[mid][1])
                l = mid + 1
        
        # Return the highest beauty for all items within or below the query price
        return max_beauty


    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Sort items by price to ensure binary search applicability
        items.sort(key=lambda x: x[0])
        
        # Prepare to track max beauty encountered so far and initialize the result array
        len_items = len(items)
        max_beauty = 0
        result = [0] * len(queries)
        
        # Step 2: Update each item's beauty to store the maximum beauty seen up to that price
        for i in range(len_items):
            # Update max_beauty to the highest beauty seen so far
            max_beauty = max(max_beauty, items[i][1])
            # Set the beauty value of items[i] to max_beauty up to that item's price
            items[i][1] = max_beauty
        
        # Step 3: For each query, use binary search to find the max beauty available within the price limit
        for i in range(len(queries)):
            query_price = queries[i]
            # Use binary search helper to find the best beauty possible within the query price
            result[i] = self.custom_binary_search(items, query_price)
        
        return result


# TC: O(NlogN + MlogM)
# SC: O(M) => m is the size of the queries
# class Solution:
#     def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
#         # O(nlogn)
#         items.sort(key = lambda x : x[0]) # sort items in terms of the first element price

#         # we are storing the query and it's position as an array (query, index)
#         # so that after sorting the queries, we still know the order, we need this for result
#         # because result needs to maintain the same order as the given queries
#         # O(m)
#         query_list = list()
#         for i in range(len(queries)):
#             query_list.append([queries[i], i])
#         # O(mlogm)
#         query_list.sort(key = lambda x: x[0])

#         result = [0]*len(queries)
#         # this query_beauty will store the maximum beauty possible for a query, so that we do not need to
#         # revisit the same item twice
#         # query_beauty = list()
#         i = 0
#         max_beauty = 0

#         # O(n+m) => each query and item is traversed only once
#         for query in query_list:
#             # if len(query_beauty) > 0:
#             #     max_beauty = query_beauty[-1] # the last max_beauty encountered so far 
#             while i < len(items):
#                 if items[i][0] > query[0]:
#                     break
#                 max_beauty = max(max_beauty, items[i][1])
#                 i += 1
#             result[query[1]] = max_beauty # placing the result maintaing the order of queries
#             # query_beauty.append(max_beauty)

#         return result
