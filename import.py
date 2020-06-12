import csv
import os

#importing sqlachemy libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://lgxegpqjyojpkj:3de66de4966840fc65d3df199f32656634f1a7a165c7d89e41aef2bd1521f647@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d5rr9paa66ne9t") #creating diffeent sessions for diffeentpeople using my website
db = scoped_session(sessionmaker(bind=engine))

def main():
#calling the csv file with information
  f = open("flight.csv")
  #built on method of python
  reader = csv.reader(f)

  for origin, destination, duration in reader: # loop gives each column a name in this case three columns
      db.execute("INSERT INTO flight (origin, destination, duration) VALUES (:origin, :destination, :duration)", #:origin.. are a placeholder since we dont know what infor we are goig to be giving
                  {"origin": origin, "destination": destination, "duration": duration}) # substitute values from CSV line into SQL command, as per this dict
      print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
  db.commit() # transactions are assumed, so close the transaction finished (basically commiting my new rows to the database flight)

if __name__ == '__main__':
    main()
