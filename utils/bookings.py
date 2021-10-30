import datetime

from bookings.models import BookedRoom


def get_booked_dates(this_room_bookings):
    """" this will calculate the number of bookings for each room and return the dates """
    dates = []
    for booking in this_room_bookings:
        count = 0
        while booking.duration > count:
            date = booking.start_date + datetime.timedelta(days=count)
            dates.append(date)
            count += 1
    return dates


class ValidateDate:

    def __init__(self, start_date=None, duration=None, room_number=None):
        self.start_date = start_date
        self.duration = duration
        self.room_number = room_number
        self.error_date = None
        self.booked_rooms = BookedRoom.objects.all().filter(room__room_number=self.room_number)

    def get_booked_dates(self):
        dates = []
        for booking in self.booked_rooms:
            count = 0
            while booking.duration > count:
                date = booking.start_date + datetime.timedelta(days=count)
                dates.append(date)
                count += 1

        return dates

    def get_entered_dates(self):
        dates = []
        count = 0
        while self.duration > count:
            date = self.start_date + datetime.timedelta(days=count)
            dates.append(date)
            count += 1
        return dates

    def not_valid(self):
        booked_dates = self.get_booked_dates()
        entered_dates = self.get_entered_dates()

        for date in entered_dates:
            if date in booked_dates:
                self.error_date = date
                return True
        return False