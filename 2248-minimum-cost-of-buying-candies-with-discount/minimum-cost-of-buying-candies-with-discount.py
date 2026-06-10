class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total_cost = sum(cost)
        cost.sort(reverse=True)
        
        for i in range(0, len(cost)-2, 3):
            total_cost -= cost[i+2]
        
        return total_cost