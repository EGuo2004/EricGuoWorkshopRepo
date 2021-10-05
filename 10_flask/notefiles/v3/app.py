# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #Terminal when I go to the site
    return "No hablo queso!"

app.debug = True #When the file has an error, it will show on screen when I go to the site
app.run()
