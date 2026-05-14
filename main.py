from Airline import airline
from DomesticRoute import DomesticRoute
from InternationalRoute import internationalRoute

airline = airline("Wizz Air")
airline.add_route(DomesticRoute("W6 1234", "Budapest", 10000))
airline.add_route(internationalRoute("W6 5678", "London", 20000))
airline.add_route(internationalRoute("W6 9012", "Paris", 15000))
airline.book_ticket("W6 1234", "Kiss Ádám")
airline.book_ticket("W6 5678", "Nagy Péter")

while True:
    print("1. Jaratok listázása")
    print("2. Jegyfoglalás")
    print("3. Jegylemondás")
    print("4. Foglalások listázása")
    print("0. kilépés")

    choice = int(input("Válassz egy opciót: "))
    print( )
    if choice < 0 or choice > 4:
        print("Érvénytelen választás, próbáld újra.")
        continue

    elif choice == 1:
        airline.list_routes()

    elif choice == 2:
        route_number = input("Add meg a járatszámot: ")
        passenger_name = input("Add meg az utas nevét: ")
        airline.book_ticket(route_number, passenger_name)

    elif choice == 3:
        route_number = input("Add meg a járatszámot: ")
        passenger_name = input("Add meg az utas nevét: ")
        airline.cancel_booking(passenger_name, route_number)

    elif choice == 4:
        airline.list_bookings()

    elif choice == 0:
        print("Viszlát!")
        break