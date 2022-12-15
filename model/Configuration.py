import codecs
import json

from .Trainer import Trainer
from .Course import Course
from .Room import Room


# Reads configuration file and stores parsed objects
class Configuration:

    # Initialize data
    def __init__(self):
        # Indicate that configuration is not parsed yet
        self._isEmpty = True
        # parsed trainers
        self._trainers = {}
        # parsed courses
        self._courses = {}
        # parsed rooms
        self._rooms = {}

    # Returns trainer with specified ID
    # If there is no trainer with such ID method returns NULL
    def getTrainerById(self, id) -> Trainer:
        if id in self._trainers:
            return self._trainers[id]
        return None

    @property
    # Returns number of parsed trainers
    def numberOfTrainers(self) -> int:
        return len(self._trainers)


    # Returns course with specified ID
    # If there is no course with such ID method returns NULL
    def getCourseById(self, id) -> Course:
        if id in self._courses:
            return self._courses[id]
        return None

    @property
    def numberOfCourses(self) -> int:
        return len(self._courses)

    # Returns room with specified ID
    # If there is no room with such ID method returns NULL
    def getRoomById(self, id) -> Room:
        if id in self._rooms:
            return self._rooms[id]
        return None

    @property
    # Returns number of parsed rooms
    def numberOfRooms(self) -> int:
        return len(self._rooms)

    @property
    # Returns TRUE if configuration is not parsed yet
    def isEmpty(self) -> bool:
        return self._isEmpty

    # Reads trainer's data from config file, makes object and returns
    # Returns NULL if method cannot parse configuration data
    @staticmethod
    def __parseTrainer(dictConfig):
        id = 0
        name = ''

        for key in dictConfig:
            if key == 'id':
                id = dictConfig[key]
            elif key == 'name':
                name = dictConfig[key]
            elif key == 'possibleCourses':
                possible_courses = dictConfig[key]
            elif key == 'availableDates':
                available_dates = dictConfig[key]

        if id == 0 or name == '':
            return None
        return Trainer(id, name, possible_courses, available_dates)

    # Reads course's data from config file, makes object and returns
    # Returns None if method dictConfig parse configuration data
    @staticmethod
    def __parseCourse(dictConfig):
        id = 0
        name = ''
        days_between_sessions = 1
        schedule = []

        for key in dictConfig:
            if key == 'id':
                id = dictConfig[key]
            elif key == 'name':
                name = dictConfig[key]
            elif key == 'daysBetweenSessions':
                days_between_sessions = dictConfig[key]
            elif key == 'schedule':
                schedule = dictConfig[key]
        
        if id == 0:
            return None
        return Course(id, name, days_between_sessions, schedule)

    # Reads rooms's data from config file, makes object and returns
    # Returns None if method cannot parse configuration data
    @staticmethod
    def __parseRoom(dictConfig):
        name = ''
        size = 0

        for key in dictConfig:
            if key == 'name':
                name = dictConfig[key]
            elif key == 'size':
                size = dictConfig[key]

        if size == 0 or name == '':
            return None
        return Room(name, size)

    # parse file and store parsed object
    def parseFile(self, fileName):
        # clear previously parsed objects
        self._trainers = {}
        self._courses = {}
        self._rooms = {}

        Room.restartIDs()

        with codecs.open(fileName, "r", "utf-8") as f:
            # read file into a string and deserialize JSON to a type
            data = json.load(f)

        for dictConfig in data:
            for key in dictConfig:
                if key == 'trainer':
                    prof = self.__parseTrainer(dictConfig[key])
                    self._trainers[prof.Id] = prof
                elif key == 'course':
                    course = self.__parseCourse(dictConfig[key])
                    self._courses[course.Id] = course
                elif key == 'room':
                    room = self.__parseRoom(dictConfig[key])
                    self._rooms[room.Id] = room

        self._isEmpty = False
