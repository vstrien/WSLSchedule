from .Constant import Constant


class Reservation:
    NR = -1
    _reservationPool = {}


    def __init__(self, date: int, duration: int, room: int):
        self.Date = date
        self.Duration = duration
        self.Room = room

    @staticmethod
    def parse(hashCode):
        reservation = Reservation._reservationPool.get(hashCode)
        if reservation is None:
            date = hashCode // 100
            duration = (hashCode - date * 100) // 10
            room = (hashCode - date * 100 - duration * 10)
            reservation = Reservation(date, duration, room)
            Reservation._reservationPool[hashCode] = reservation
        return reservation

    @staticmethod
    def getHashCode(date: int, duration: int, room: int) -> int:
            return date * 100 + duration * 10 + room

    @staticmethod
    def getReservation(nr: int, date: int, duration: int, room: int):
        if nr != Reservation.NR and nr > 0:
            Reservation.NR = nr
            Reservation._reservationPool.clear()

        hashCode = Reservation.getHashCode(date, duration, room)
        reservation = Reservation.parse(hashCode)

        if reservation is None:
            reservation = Reservation(date, duration, room)
            Reservation._reservationPool[hashCode] = reservation
        return reservation

    def __hash__(self) -> int:
        return Reservation.getHashCode(self.Date, self.Time, self.Room)


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)
            
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __str__(self):
        return "Day: " + str(self.Date) + ", " + "Room: " + str(self.Room) + ", Time: " + str(self.Time)
