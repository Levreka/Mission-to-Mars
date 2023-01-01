

# Import Flask, PyMongo, and scraping.py 
from flask import Flask, render_template
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

# Set Up Routes
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    #holds newly scraped data, referencing scrape_all() function in scraping.py file
    mars_data=scraping.scrape_all()
    mars.update({},mars_data,upsert=True)
    return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)


#