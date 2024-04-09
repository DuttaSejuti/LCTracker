class Solution:
    # TC:O(n*m)=> n is the len of the tickets, m is the maximum no of iteration of outer while loop, SC:O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sold_tickets = 0

        # keep track of the sold_tickets in each pass untill the tickets[k] == 0
        while True:
            for i in range(len(tickets)):
                tickets[i] -= 1
                if tickets[k] == 0:
                    sold_tickets += 1
                    return sold_tickets
                if tickets[i] >= 0:
                    sold_tickets += 1
