import datetime


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
