class ticketBooking:
    def __init__(self, passenger_name, route):
        self._passenger_name = passenger_name
        self._route = route
    
    def get_passenger_name(self):
        return self._passenger_name
    
    def get_route(self):
        return self._route
    
    def __str__(self):
        return f"{self._passenger_name} - {self._route}"
    
