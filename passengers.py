import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://lgxegpqjyojpkj:3de66de4966840fc65d3df199f32656634f1a7a165c7d89e41aef2bd1521f647@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d5rr9paa66ne9t") #creating diffeent sessions for diffeentpeople using my website
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Get all the information from flighttable and save in to var flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flight").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes.")

    # Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flight WHERE id = :id",
                        {"id": flight_id}).fetchone()

    # Make sure flight is valid.
    if flight is None:
        print("Error: No such flight.")
        return

    # List passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")

if __name__ == '__main__':
    main()
