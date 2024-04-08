class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        n = len(students)
        new_dict = dict()


        # keeping count of how many student want sandwich 0 and 1
        for student in students:
            new_dict[student] = new_dict.get(student, 0) + 1
        
        students = deque(students)

        while True:
            if not sandwiches or new_dict.get(sandwiches[0], 0) == 0:
                break

            top_sandwich = sandwiches[0]
            student_choice = students.popleft()

            # if student's choice matches with the stack top
            if student_choice == top_sandwich:
                sandwiches.pop(0)
                new_dict[student_choice] -= 1
            else:
                students.append(student_choice) # pushing the popped student at the end
        
        return len(sandwiches)
