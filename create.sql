/* creating a table */
CREATE TABLE flights (
   /* serial is the data type, primary key explaning the primary way via which im going to reference a flight */
   /* that every fligh is going to have a unique ID */1
   id SERIAL PRIMARY KEY,
   /*origin is the name, varchar sort of the string we want to ente, not null means this need to have a value since is
   a flight origin */
   origin VARCHAR NOT NULL,
   duration INTEGER NOT NULL
);


/* creating a table */

INSERT INTO flight (origin, destination, duration) VALUES ('Malaysia', 'Aberdeen', 415);
INSERT INTO flight (origin, destination, duration) VALUES ('London', 'Tenerife', 312);
INSERT INTO flight (origin, destination, duration) VALUES ('Vienna', 'Edinburgh', 456);
INSERT INTO flight (origin, destination, duration) VALUES ('Amsterdam', 'Ireland', 215);
INSERT INTO flight (origin, destination, duration) VALUES ('London', 'Ireland', 312);
INSERT INTO flight (origin, destination, duration) VALUES ('New york', 'Ireland', 715);



   CREATE TABLE flight (
      id SERIAL PRIMARY KEY,
      origin VARCHAR NOT NULL,
      destination VARCHAR NOT NULL,
      duration INTEGER NOT NULL
   );

   CREATE TABLE passengers (
      id SERIAL PRIMARY KEY,
      name VARCHAR NOT NULL,
      flight_id INTEGER REFERENCES flight
   );

   INSERT INTO passengers (name, flight_id) VALUES ('Monica', 3);
   INSERT INTO passengers (name, flight_id) VALUES ('Marina', 2);
   INSERT INTO passengers (name, flight_id) VALUES ('Julio', 1);
   INSERT INTO passengers (name, flight_id) VALUES ('Sofia', 2);
   INSERT INTO passengers (name, flight_id) VALUES ('Alba', 4);
   INSERT INTO passengers (name, flight_id) VALUES ('Mario', 5);
   INSERT INTO passengers (name, flight_id) VALUES ('Eris', 6);
   INSERT INTO passengers (name, flight_id) VALUES ('Dave', 6);
