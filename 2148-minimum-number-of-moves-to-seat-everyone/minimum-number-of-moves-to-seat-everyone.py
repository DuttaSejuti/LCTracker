class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        min_move = 0
        seats.sort()
        students.sort()

        for i in range(len(students)):
            min_move += abs(students[i] - seats[i])
        
        return min_move
        