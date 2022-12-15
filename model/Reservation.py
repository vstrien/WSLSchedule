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
            date = hashCode // (Reservation.NR)
            hashCode2 = hashCode - (date * Reservation.NR)
            room = hashCode2 // 1
            time = hashCode2 % 
            reservation = Reservation(date, time, room)
            Reservation._reservationPool[hashCode] = reservation
        return reservation

    @staticmethod
    def getHashCode(date: int, duration: int, room: int) -> int:
            return date * Reservation.NR * duration + room * duration + duration

    @staticmethod
    def getReservation(nr: int, date: int, time: int, room: int):
        if nr != Reservation.NR and nr > 0:
            Reservation.NR = nr
            Reservation._reservationPool.clear()

        hashCode = Reservation.getHashCode(date, duration, room)
        reservation = Reservation.parse(hashCode)

        if reservation is None:
            reservation = Reservation(date, time, room)
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
