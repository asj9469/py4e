class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # count method
        # time complexity: O(n)
        # space complexity: O(n)

        unableToEat = len(students)
        studentCount = defaultdict(int)

        for i in students:
            studentCount[i] += 1

        for i in sandwiches:
            if studentCount[i] > 0:
                unableToEat -= 1
                studentCount[i] -= 1
            else:
                return unableToEat

        return unableToEat

        # Ilma (Coach) approach
        # time complexity: O(n^2)
        # space complexity: O(1)
        unableToEat = 0

        while sandwiches:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                unableToEat = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                unableToEat += 1

            if unableToEat == len(students):
                break

        return len(students)

        # Ayush's approach
        # time complexity: O(n^2)
        # space complexity: O(1)

        while sandwiches and sandwiches[0] in students:
            students.remove(sandwiches.pop(0))

        return len(students)


