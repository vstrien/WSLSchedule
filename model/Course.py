# Stores data about course
class Course:
    # Initializes course
    def __init__(self, id, name, days_between_sessions, schedule):
        # Returns course ID
        self.Id = id
        # Returns course name
        self.Name = name
        # Returns the number of days between each training session in the schedule
        self.DaysBetweenSessions = days_between_sessions
        # Returns the training sessions in a list of integers: 1 = full day training, 0.5 = half day
        self.Schedule = schedule
