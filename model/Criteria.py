from .Constant import Constant


# Reads configuration file and stores parsed objects
class Criteria:

    # check for room overlapping of classes
    @staticmethod
    def isRoomOverlapped(slots, reservation, dur):
        reservation_index = hash(reservation)
        cls = slots[reservation_index: reservation_index + dur]
        return any(True for slot in cls if len(slot) > 1)

    # check overlapping of classes for professors and student groups
    @staticmethod
    def isOverlappedTrainer(slots, courseday, numberOfRooms, timeId):
        po = False

        dur = courseday.Duration
        for i in range(numberOfRooms, 0, -1):
            # for each day or half day of class
            for j in range(timeId, timeId + dur):
                cl = slots[j]
                for cc1 in cl:
                    if courseday != cc1:
                        # professor overlaps?
                        if not po and courseday.trainerOverlaps(cc1):
                            po = True
                        # Andere overlappen kunnen hier nog aan toegevoegd
                        # both type of overlapping? no need to check more
                        if po:
                            return po

            timeId += Constant.DAY_HOURS
        return po