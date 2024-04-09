class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sold_tickets = 0

        while True:
            for i in range(len(tickets)):
                tickets[i] -= 1
                if tickets[k] == 0:
                    sold_tickets += 1
                    return sold_tickets
                if tickets[i] >= 0:
                    sold_tickets += 1
        