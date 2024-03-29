#flask run needs to be run using command promp in visual studio go to by were the output is seen and on the plus sign add commmand prompt terminal 
#and type flask run in there


# Import Flask, PyMongo, and scraping.py 
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Let's break down what this code is doing.

# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
# The second line says we'll use PyMongo to interact with our Mongo database.
# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.

#set up our flask app
app= Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".

# Set Up Route for the html page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#set up scraping route view 1051 module for more explanation on this code
@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    #holds newly scraped data, referencing scrape_all() function in scraping.py file
    mars_data = scraping.scrape_all()
    #update the database using .update_one()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

#run the flask app remember this is done in the terminal
if __name__ == "__main__":
    app.run(debug=True)


