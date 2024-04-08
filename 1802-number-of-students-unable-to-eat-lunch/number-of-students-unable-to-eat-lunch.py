class Solution:
    # TC: O(n), SC: O(1)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]  # count[0] for students who want sandwich 0, count[1] for students who want sandwich 1
        
        # Count the number of students who want each type of sandwich
        for student in students:
            count[student] += 1
            
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            
            count[sandwich] -= 1
        
        return sum(count)
