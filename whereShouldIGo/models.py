import sqlite3
from sqlite3 import Error

def addUser(username, password):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("INSERT INTO user (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()
	
def retrieveUsers():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM user")
	users = cur.fetchall()
	con.close()
	return users
	
def getUserId(name):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idUser FROM user WHERE username = ?", (name,))
    users = cur.fetchall()
    con.close()
    return users
	
def addLocationType(category):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("INSERT INTO locationType(category) VALUES(?)", (category,))
	con.commit()
	con.close()
	
def retrieveLocationtype():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT category FROM locationType")
	locationType = cur.fetchall()
	con.close()
	return locationType	
	
def getIdLocationType(category):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idLocationType FROM locationType WHERE category = ?", (category,))
    categories = cur.fetchall()
    con.close()
    return categories	
#############################################################################
def addReview(idLocationDetails, stars, comment):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("INSERT INTO reviews(idLocationDetails, stars, comment) VALUES(?,?)", (idLocationDetails, stars,comment))
	con.commit()
	con.close()
	
def retrieveReviews(idLocationDetails):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT locationDetails.name, reviews.stars,reviews.comment FROM reviews inner join locationDetails on locationDetails.idLocationDetails = ?",(idLocationDetails,))
	reviews = cur.fetchall()
	con.close()
	return locationType	
##############################table LocationDetails###############################################
def addLocationDetails(idLocationType,name, picture,price, history):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("INSERT INTO locationDetails(idLocationType, name, picture, price, history) VALUES(?,?,?,?,?)", (idLocationType,name, picture,price, history))
	con.commit()
	con.close()
	
def retrieveLocationName():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT name FROM locationDetails")
	locationDetails = cur.fetchall()
	con.close()
	return locationDetails	
	
#get location by location type
def getIdLocationDetails(name):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idLocationType FROM locationType WHERE name = ?", (name,))
    locDetails = cur.fetchall()
    con.close()
    return locDetails
def retriveLocation():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT location.country, location.city, locationDetails.name, locationDetails.picture, locationDetails.price, locationDetails.history FROM location inner join locationDetails on location.idLocationDetails = locationDetails.idLocationDetails")
	allLocation = cur.fetchall()
	con.close()
	return allLocation
######################LOCATION TABLE#######################################################
def addLocation(idLocationDetails,country, city):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("INSERT INTO location(idLocationDetails,country, city) VALUES(?,?,?)", (idLocationDetails,country, city))
	con.commit()
	con.close()	
def retrieveLocation():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT country, city FROM location")
	locationDetails = cur.fetchall()
	con.close()
	return locationDetails	
def getIdLocation(name):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idLocationDetails FROM locationDetails WHERE name = ?", (name,))
    locDetails = cur.fetchall()
    con.close()
    return locDetails	
def retrieveCountry():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT country FROM location")
	country = cur.fetchall()
	con.close()
	return country	
def getIdCountry(name):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idLocationDetails FROM location WHERE country = ?", (name,))
    countryDet = cur.fetchall()
    con.close()
    return countryDet	
def retriveLocationByCountry(country):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT location.country, location.city, locationDetails.name, locationDetails.picture, locationDetails.price, locationDetails.history FROM location inner join locationDetails on location.idLocationDetails = locationDetails.idLocationDetails and location.country = ?", (country,))
	allLocation = cur.fetchall()
	con.close()
	return allLocation
	#######
def retrieveCity():
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT city FROM location")
	city = cur.fetchall()
	con.close()
	return city	
def getIdCity(name):
    con = sqlite3.connect("travelling.db")
    cur = con.cursor()
    cur.execute("SELECT idLocationDetails FROM location WHERE city = ?", (name,))
    cityDet = cur.fetchall()
    con.close()
    return cityDet	
def retriveLocationByCity(city):
	con = sqlite3.connect("travelling.db")
	cur = con.cursor()
	cur.execute("SELECT location.country, location.city, locationDetails.name, locationDetails.picture, locationDetails.price, locationDetails.history FROM location inner join locationDetails on location.idLocationDetails = locationDetails.idLocationDetails and location.city = ?", (city,))
	allLocation = cur.fetchall()
	con.close()
	return allLocation
if __name__ == '__main__':
    main()