# Softlocked - Eric Guo and Michael Borczuk
# SoftDev
# K19 - Nasa RESTApi Stuff
# 2021-11-23
# time spent: 0.6 hours

from flask import Flask, render_template
import urllib
import json
import os

app = Flask(__name__) 

@app.route("/") 
def hello_world():
    print(__name__)
    script_dir = os.path.dirname(__file__) # avoid filenotfound error for key file
    print(script_dir)
    path = os.path.join(script_dir, "key_nasa.txt") # construct path to key file
    f = open(path) 
    key = f.read()
    response = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + key) # join key with base url
    print(response)
    json_stuff = json.loads(response.read())  
    print(json_stuff)
    return render_template("main.html", pic=json_stuff["url"], expl=json_stuff["title"])

app.run()  

                
