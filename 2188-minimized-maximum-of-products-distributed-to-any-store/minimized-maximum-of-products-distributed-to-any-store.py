# we need to keep checking with all possible distributions from 1 to the max
class Solution:
    def canDistribute(self, n: int, max_value: int, quantities: List[int]) -> int:
        stores = 0
        for quantity in quantities:
            stores += ceil(quantity/max_value)
            # we do not have enough stores
            if stores > n:
                return False
        return True

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1 # initially all stores has 0 product, So no need to check for 0
        r = max(quantities)
        x = 0

        while l <= r:
            mid = l + (r-l)//2
            if self.canDistribute(n, mid, quantities):
                # we can check if we can find more less value that we can distribute
                # we will go left
                x = mid
                r = mid - 1
            else:
                # we need to look for bigger value, go right
                l = mid + 1
        return x
