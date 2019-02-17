import sqlite3
from sqlite3 import Error
 
 
def createConnection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		return conn
	except Error as e:
		print(e)
	return None
def createTable(conn, createTable_sql):
    try:
        c = conn.cursor()
        c.execute(createTable_sql)
    except Error as e:
        print(e)

def createReviews(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS reviews(
			idReviews integer PRIMARY KEY,
			idLocationDetails integer NOT NULL,
			stars integer NOT NULL,
			comment text NOT NULL
			);"""
	createTable(connectionToDatabase, query)
	
def createLocationType(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS locationType(
			idLocationType integer PRIMARY KEY,
			category text NOT NULL
			);"""
	createTable(connectionToDatabase, query)

def createLocationDetails(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS locationDetails(
			idLocationDetails integer PRIMARY KEY,
			idLocationType integer NOT NULL,
			name text NOT NULL,
			picture text,
			price integer,
			history text,
			foreign key (idLocationType) references locationType (idLocationType)
			);"""
	createTable(connectionToDatabase, query)
	
def createLocation(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS location(
			idLocation integer PRIMARY KEY,
			idLocationDetails integer NOT NULL,
			country text NOT NULL,
			city text NOT NULL,
			foreign key (idLocationDetails) references locationDetails (idLocationDetails)
			);"""
	createTable(connectionToDatabase, query)
	
def createUser(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS user(
			idUser integer PRIMARY KEY,
			username text NOT NULL,
			password text NOT NULL
			);"""
	createTable(connectionToDatabase, query)
	
def createUserDetails(connectionToDatabase):
	query = """ CREATE TABLE IF NOT EXISTS userDetails(
			idUserDetails integer PRIMARY KEY,
			idUser integer NOT NULL,
			idLocation integer NOT NULL,
			idTrips integer NOT NULL,
			foreign key (idUser) references user (idUser),	
			foreign key (idLocation) references location (idLocation),
			foreign key (idTrips) references trips (idTrips)
			);"""
	createTable(connectionToDatabase, query)

def createTrips(connectionToDatabase):	
	query = """ CREATE TABLE IF NOT EXISTS trips(
			idTrips integer PRIMARY KEY,
			idLocationDetails integer NOT NULL,
			startingDate text,
			endingDate text,
			foreign key (idLocationDetails) references locationDetails (idLocationDetails)
			);"""
	createTable(connectionToDatabase, query)
			
def main():
	database = "travelling.db"
	
	connectionToDatabase = createConnection(database)
	
	if connectionToDatabase is not None:
		createReviews(connectionToDatabase);
		createLocationType(connectionToDatabase);
		createLocationDetails(connectionToDatabase);
		createLocation(connectionToDatabase);
		createUser(connectionToDatabase);
		createUserDetails(connectionToDatabase);
		createTrips(connectionToDatabase);
	else:
		print("Error!!! connection to database is not created")
	
if __name__ == '__main__':
	main()