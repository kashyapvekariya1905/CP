from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students.copy()  
        sandwich_stack = sandwiches.copy()  
        while queue:
            if not sandwich_stack:
                break  
            if queue[0] == sandwich_stack[0]:
                queue.pop(0) 
                sandwich_stack.pop(0) 
            else:
                queue.append(queue.pop(0))
            if len(queue) == len(students) and queue == students:
                break
        return len(sandwich_stack)

s = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(s.countStudents(students,sandwiches))