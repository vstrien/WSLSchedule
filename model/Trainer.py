# Stores data about professor
class Trainer:
    # Initializes professor data
    def __init__(self, id, name, possible_courses, available_dates):
        self.Id = id
        self.Name = name
        self.PossibleCourses = possible_courses
        self.AvailableDates = available_dates
        self.CourseClasses = []

    # Bind professor to course
    def addCourseClass(self, courseClass):
        self.CourseClasses.append(courseClass)

    def __hash__(self):
        return hash(self.Id)

    # Compares ID's of two objects which represent professors
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)
