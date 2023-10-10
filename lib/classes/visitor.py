from .trip import Trip

class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and len(name)>=1 and len(name)< 16:
            self._name = name
        self.tripss = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        pass

    def trips(self):
        trips = self.tripss
        return trips
    
    def nationalparks(self):
        nationalpark = []
        for trip in self.tripss:
            if not trip.national_park in nationalpark:
                nationalpark.append(trip.national_park)
        return nationalpark
    
    def create_trip(self, national_park, start_date, end_date):
        Trip(self, national_park, start_date, end_date)
