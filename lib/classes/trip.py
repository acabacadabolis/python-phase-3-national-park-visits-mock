
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        visitor.tripss.append(self)
        self.national_park = national_park
        national_park.tripss.append(self)
        self.start_date = start_date
        self.end_date = end_date

