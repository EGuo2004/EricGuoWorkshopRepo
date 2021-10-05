# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) # Q0: Java Constructors.

@app.route("/") # Q1: "/" signifies the largest directory
def hello_world():
    print(__name__) # Terminal, " __main__"
    return "No hablo queso!"  # Q3: This will appear on screen

app.run()  # Q4: I do not remember seeing this anywhere

                
