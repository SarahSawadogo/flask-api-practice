# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os #import os allows us to access environmental variables that 

# -- Initialization section --
app = Flask(__name__)
#os.getenv() is how you pull private information (such as an API key) without revealing it in the code. 
#the .env file with the actual key does not get pushed to Github since it is in .gitignore file
#The string inside app.config ("GIPHY_KEY") is what you need to specify in heroku's config vars in settings for your app to run
app.config["GIPHY_KEY"] = os.getenv("GIPHY_KEY")


# -- Routes section --
@app.route('/')
@app.route('/index')
#time = datetime.now() is a way to trick your browser into not caching CSS and reloading the CSS every time
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods=['GET', 'POST'])
def yourgif():
    #needs to pull form data from index.html (name was gifchoice)
    query = request.form["gifchoice"]
    #this print statement is just for debugging purposes
    print(request.form)
    #needs to call getImageUrlFrom function, passing in query as an argument
    gif_choice = getImageUrlFrom(query, app.config["GIPHY_KEY"])
    #needs to pass URL into render_template
    return render_template("yourgif.html", time = datetime.now(), image = gif_choice)