class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        matching = 0

        players.sort()
        trainers.sort()
        queue = deque()
        idx = 0

        for player in players:
            while idx < len(trainers):
                if player <= trainers[idx]:
                    queue.append(trainers[idx])
                idx += 1
            # print(queue)
            while queue:
                trainer_capacity = queue.popleft()
                if player <= trainer_capacity:
                    matching += 1
                    break
            
        return matching
