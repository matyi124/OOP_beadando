from abc import ABC, abstractmethod


class route(ABC):
    def __init__(self, route_number, destination, ticket_price):
        self._route_number = route_number
        self._destination = destination
        self._ticket_price = ticket_price

    
    def get_route_number(self):
            return self._route_number
        

    def get_destination(self):
            return self._destination
        
        
    def get_ticket_price(self):
            return self._ticket_price

    @abstractmethod
    def get_route_type(self):
        pass

    def __str__(self):
        return f"{self._route_number} | {self._destination} | {self._ticket_price} Ft | {self.get_route_type()}."
    