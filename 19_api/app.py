# Softlocked - Eric Guo and Michael Borczuk
# SoftDev
# Oct 2021

from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__) 

@app.route("/") 
def hello_world():
    print(__name__) 
    picture = urllib3.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=DzW2D4l1DakGW9bo7dheF10L7evZVr2YyzkOIvCi")
    print (picture);
    return render_template("main.html", pic="")

app.run()  

                
