class Solution:
    # TC:O(n*m)=> n is the len of the tickets, m is the maximum no of iteration of outer while loop, SC:O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sold_tickets = 0 # time taken

        # keep track of the sold_tickets in each pass untill the tickets[k] == 0
        # while True:
        #     for i in range(len(tickets)):
        #         tickets[i] -= 1
        #         if tickets[k] == 0:
        #             sold_tickets += 1
        #             return sold_tickets
        #         if tickets[i] >= 0:
        #             sold_tickets += 1

        # another version of the while loop
        while tickets[k] > 0:
            for i in range(len(tickets)):
                # buy a ticket at idx i if possible; tickets[i] > 0
                if tickets[i] != 0:
                    tickets[i] -= 1
                    sold_tickets += 1
                # if k bought all it's required tickets, return 
                if tickets[k] == 0:
                    return sold_tickets

        return sold_tickets

    # TC:O(n), SC:O(1)
    # def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    #     time = 0

    #     for i in range(len(tickets)):
    #         # current person is after k
    #         if i > k:
    #             time += min(tickets[k] - 1, tickets[i])
    #         else:
    #             # current person is k or current person is before k
    #             time += min(tickets[k], tickets[i])
            
    #     return time
