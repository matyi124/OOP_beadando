from Route import route

class DomesticRoute(route):
    def __init__(self, route_number, destination, ticket_price):
        super().__init__(route_number, destination, ticket_price)

    def get_route_type(self):
        return "Belföldi járat"
    
