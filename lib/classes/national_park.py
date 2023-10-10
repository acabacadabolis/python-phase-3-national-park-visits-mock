from .trip import Trip

class NationalPark:

    def __init__(self, name):
        if isinstance(name, str):
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
    
    def visitors(self):
        visitors = []
        for trip in self.tripss:
            if not trip.visitor in visitors:
                visitors.append(trip.visitor)
        return visitors

    def total_visits(self):
        return [trip for trip in self.tripss if trip.national_park == self]
    
    def total_trips(self):
        return len(self.tripss)
    
    def best_visitor(self):
        return self.tripss[0].visitor