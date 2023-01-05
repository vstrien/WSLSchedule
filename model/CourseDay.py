class CourseDay:
    # ID counter used to assign IDs automatically
    _next_class_id = 0

    # Initializes class object
    def __init__(self, trainer, course, duration):
        self.Id = CourseDay._next_class_id
        CourseDay._next_class_id += 1
        # Return pointer to professor who teaches
        self.Trainer = trainer
        # Return pointer to course to which class belongs
        self.Course = course
        # Returns duration of class in days (or parts of day)
        self.Duration = duration
        
        # bind professor to class
        self.Trainer.addCourseClass(self)

    # Returns TRUE if another class has same professor.
    def trainerOverlaps(self, c):
        return self.Trainer == c.Professor

    def __hash__(self):
        return hash(self.Id)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    # Restarts ID assigments
    @staticmethod
    def restartIDs() -> None:
        CourseDay._next_class_id = 0
