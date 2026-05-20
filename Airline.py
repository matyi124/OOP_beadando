from TicketBooking import ticketBooking


class airline:

    def __init__(self, name):
        self._name = name
        self._routes = []
        self._bookings = []

    def add_route(self, route):
        self._routes.append(route)

    def list_routes(self):
        for route in self._routes:
            print(route)

    def list_bookings(self):
        for booking in self._bookings:
            print(booking)
        if not self._bookings:
            print("Nincsenek foglalások")

    def find_route_by_number(self, route_number):
        for route in self._routes:
            if route.get_route_number() == route_number:
                return route
        return None

    def book_ticket(self, route_number, passenger_name):
        route = self.find_route_by_number(route_number)

        if route is None:
            print("nincs ilyen járat")
            return None

        booking = ticketBooking(passenger_name, route)
        self._bookings.append(booking)

        print("sikeres foglalás")
        return route.get_ticket_price()

    def cancel_booking(self, route_number, passenger_name):
        route_number = route_number.strip()
        passenger_name = passenger_name.strip().lower()

        for booking in self._bookings:
            stored_passenger_name = booking.get_passenger_name().strip().lower()
            stored_route_number = booking.get_route().get_route_number().strip()

            if stored_passenger_name == passenger_name and stored_route_number == route_number:
                self._bookings.remove(booking)
                print("Foglalás lemondva")
                return True

        print("Nincs ilyen foglalás")
        return False