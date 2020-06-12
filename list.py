#improting an operating system library
import os

#importing sqlachemy libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#creating database engine (object created by sqlalchemy a third party library) managed connections to the dagabase
engine = create_engine("postgresql://lgxegpqjyojpkj:3de66de4966840fc65d3df199f32656634f1a7a165c7d89e41aef2bd1521f647@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d5rr9paa66ne9t") #creating diffeent sessions for diffeentpeople using my website
db = scoped_session(sessionmaker(bind=engine))

def main():
    flight = db.execute("SELECT origin, destination, duration FROM flight").fetchall() # execute this SQL command and return all of the results
    for travel in flight:
        print(f"{travel.origin} to {travel.destination}, {travel.duration} minutes.") # for every flight, print out the flight info

if __name__ == '__main__':
    main()
