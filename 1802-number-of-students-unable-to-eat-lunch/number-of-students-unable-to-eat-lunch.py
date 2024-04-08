class Solution:
    # TC:O(n), SC:O(1)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = Counter(students) # return a hashMap

        # the order of students does not matter
        # the order of the sandwiches matters
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                res -= 1
                count[sandwich] -= 1
            else:
                return res
        return res

    # TC: O(n), SC:O(n) => SC O(n) because of the deque
    # def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    #     new_dict = dict()


    #     # keeping count of how many student want sandwich 0 and 1
    #     for student in students:
    #         new_dict[student] = new_dict.get(student, 0) + 1
        
    #     students = deque(students)

    #     while True:
    #         # all the sandwiches are chosen sandwiches becomes empty OR
    #         # the top sandwich is not wanted by any od the students => nothing to distribute 
    #         if not sandwiches or new_dict.get(sandwiches[0], 0) == 0:
    #             break

    #         top_sandwich = sandwiches[0]
    #         student_choice = students.popleft()

    #         # if student's choice matches with the stack top
    #         if student_choice == top_sandwich:
    #             sandwiches.pop(0)
    #             new_dict[student_choice] -= 1
    #         else:
    #             students.append(student_choice) # pushing the popped student at the end
        
    #     return len(sandwiches)
