class Solution:
    # def minimumCost(self, cost: List[int]) -> int:
    #     total_cost = sum(cost)
    #     cost.sort(reverse=True)
        
    #     for i in range(0, len(cost)-2, 3):
    #         total_cost -= cost[i+2]
        
    #     return total_cost
    
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        cost.sort(reverse=True)

        for i in range(len(cost)):
            # not the third candy, then add
            if i % 3 != 2:
                total += cost[i]
        return total