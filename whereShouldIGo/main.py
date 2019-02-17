import collections
import json
import subprocess
import datetime

from sqlalchemy import exc
from flask import Flask, request, render_template, flash, Flask, request, url_for, redirect, session
from wtforms import Form, BooleanField, RadioField, TextField, PasswordField, DateField, validators

import os
import models as dbHandler

web_app = Flask(__name__)
web_app.secret_key = "ancab"

@web_app.route('/', methods=['POST', 'GET'])
def index_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method=='POST':
		password = request.form['password']
		dbHandler.addUser(username, password)
		user = dbHandler.retrieveUsers()
		return render_template('index.html',username=username)
	else:
		return render_template('index.html')
		
@web_app.route('/login/', methods=['GET', 'POST'])
def login_page():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		userId = dbHandler.getUserId(username)
		if len(userId) == 1:
			session['logged_in'] = True
			session['username'] = username
			session['userid'] = userId[0][0]
			return render_template('index.html', username=username)
		else:
			flash("Invalid credentials. Please try again!")
			return render_template("login.html")
	if request.method == "GET":
		return render_template("login.html")


@web_app.route('/signUp/', methods=["GET", "POST"])
def signUp_page():
    if request.method == "GET":
        return render_template("signUp.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['password2']
        if password == confirmPassword:
            userId = dbHandler.getUserId(username)
            if len(userId) == 1:
                flash("Username already exists")
                return render_template('signUp.html')
            else:
                dbHandler.addUser(username, password)
                userId = dbHandler.getUserId(username)
                session['logged_in'] = True
                session['username'] = username
                session['userid'] = userId[0][0]
                return redirect(url_for('index_page'))
        else:
            flash("Password must match")
            return render_template('signUp.html')

@web_app.route('/logout/', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('index_page'))

##############################################################	
@web_app.route('/locationType/', methods=['POST', 'GET'])
def locationType_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method=='GET':
		locationType = dbHandler.retrieveLocationtype()
		return render_template('locationType.html',locationType=locationType, username = username)
	else:
		return render_template('index.html')
		
@web_app.route('/addLocationType/', methods=['POST', 'GET'])	
def addLocationType_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method == "GET":
		return render_template("addLocationType.html", username = username)
	if request.method == 'POST':
		category = request.form['category']
		idLocationType = dbHandler.getIdLocationType(category)
		if len(idLocationType) == 1:
			flash("Category already exists")
			return render_template('addLocationType.html', username = username)
		else:
			dbHandler.addLocationType(category)
			idLocationType = dbHandler.getIdLocationType(category)
			flash("Category added")
			return render_template('addLocationType.html', username = username)	
@web_app.route('/addLocationDetails/', methods=['POST', 'GET'])	
def addLocationDetails_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method == "GET":
		locationType = dbHandler.retrieveLocationtype()
		return render_template("addLocationDetails.html",locationType = locationType, username = username)
	if request.method == 'POST':
		locationType = dbHandler.retrieveLocationtype()
		
		nameLocationType = request.form['nameLocationType']
		idLocationTypeTuple = dbHandler.getIdLocationType(nameLocationType)
		
		s = str(idLocationTypeTuple[0]).replace("(","")
		idLocationType = s.replace(",)","")
		name = request.form['name']
		picture = request.form['picture']
		price = request.form['price']
		history = request.form['history']
		dbHandler.addLocationDetails(idLocationType,name, picture,price, history)
		flash("Location added")
		return render_template('addLocationDetails.html',locationType = locationType, username = username)
##############################################################		
@web_app.route('/addLocation/', methods=['POST', 'GET'])	
def addLocation_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method == "GET":
		nameLocationDetails = dbHandler.retrieveLocationName()
		return render_template("addLocation.html",nameLocationDetails = nameLocationDetails, username = username)
	if request.method == 'POST':
		nameLocationDetails = dbHandler.retrieveLocationName()
		
		locationDetails = request.form['nameLocationDetails']
		idLocationTuple = dbHandler.getIdLocation(locationDetails)
		
		s = str(idLocationTuple[0]).replace("(","")
		idLocation= s.replace(",)","")
		
		country = request.form['country']
		city = request.form['city']
		dbHandler.addLocation(idLocation,country, city)
		flash("Location added")
		return render_template('addLocation.html',nameLocationDetails = nameLocationDetails, username = username)	

##############################################################	
@web_app.route('/locationDetails/', methods=['POST', 'GET'])
def locationDetails_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method=='GET':
		allLocations = dbHandler.retriveLocation()
		return render_template('locationDetails.html',allLocations = allLocations, username = username)
	else:
		return render_template('index.html')
@web_app.route('/searchByCountry/', methods=['POST', 'GET'])
def searchByCountry_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method == "GET":
		country = dbHandler.retrieveCountry()
		return render_template("searchByCountry.html",country = country, username = username)
	if request.method == 'POST':
		country = dbHandler.retrieveCountry()
		countryy = request.form['selectCountry']
		idCountryTuple = dbHandler.getIdCountry(countryy)
		s = str(idCountryTuple[0]).replace("(","")
		idCountry = s.replace(",)","")
		
		allLocations = dbHandler.retriveLocationByCountry(countryy)
		return render_template('searchByCountry.html',country = country,allLocations = allLocations, username = username)	
@web_app.route('/searchByCity/', methods=['POST', 'GET'])
def searchByCity_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method == "GET":
		city = dbHandler.retrieveCity()
		return render_template("searchByCity.html",city = city, username = username)
	if request.method == 'POST':
		city = dbHandler.retrieveCity()
		cityy = request.form['selectCity']
		idCityTuple = dbHandler.getIdCity(cityy)
		s = str(idCityTuple[0]).replace("(","")
		idCity= s.replace(",)","")
		
		allLocations = dbHandler.retriveLocationByCity(cityy)
		return render_template('searchByCity.html',city = city,allLocations = allLocations, username = username)	
@web_app.route('/location/', methods=['POST', 'GET'])
def location_page():
	username = ""
	if session.get('logged_in') == True:
		username = session['username']
	if request.method=='GET':
		allLocations = dbHandler.retrieveLocation()
		return render_template('location.html',allLocations = allLocations, username = username)
	else:
		return render_template('index.html')
							
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5003))
	web_app.run(host="127.0.0.1", port=port)