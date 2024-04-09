class Solution:
    #Approach-01
    # TC:O(n*m)=> m is the max no of tickets at each index, SC:O(n) => for the deque
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        queue = deque()

        #initialize the queue with indices of the tickets
        for i in range(len(tickets)):
            queue.append(i)
        
        while len(queue) > 0:
            time += 1 #increment time for each iteration

            front = queue.popleft() # get the front of the queue
            tickets[front] -= 1 # buy ticket for the front person

            # if k has bought all the tickets, return
            if front == k and tickets[front] == 0:
                return time
            
            # push the front person at the end of the queue, so he can buy again later
            if tickets[front] != 0:
                queue.append(front)
            
        return time


    # Approach-02
    # TC:O(n*m)=> n is the len of the tickets, m is the maximum no of iteration of outer while loop, SC:O(1)
    # def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    #     sold_tickets = 0 # time taken

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
        # while tickets[k] > 0:
        #     for i in range(len(tickets)):
        #         # buy a ticket at idx i if possible; tickets[i] > 0
        #         if tickets[i] != 0:
        #             tickets[i] -= 1
        #             sold_tickets += 1
        #         # if k bought all it's required tickets, return 
        #         if tickets[k] == 0:
        #             return sold_tickets

        # return sold_tickets

    # Approach-03
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
