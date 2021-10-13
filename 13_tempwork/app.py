#Team Team : Alif Abdullah, Eric Guo, Shadman Rakib Period 2
#SoftDev
#K13 - To create a flask app that randomly chooses and displays an occupation based on a template
#10/8/21
import csv
import random
from flask import Flask, render_template

# Declaration of dictionary to store CSV File contents
finalDict = {}
# Create instance of flask app
app = Flask(__name__)

# Read in CSV file
def fileReader():
    with open('data/occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            finalDict[row['Job Class']] = float(row['Percentage'])

# Choose random job from dictionary
def randomJob(reader):
    x = random.randint(0, 1000)
    y = 0
    for i in reader:
        y += reader[i] * 10
        if y > x:
            return i
            break
        
@app.route("/")
def homePage():
    return("new phone, who dis?")
    
# Running the flask app with displayApp function
@app.route("/occupyflaskst")
def displayApp():
    fileReader()
    return render_template('tablified.html',names="Eric Guo", course="SoftDev", assignment="K13 - To create a flask app that randomly chooses and displays an occupation based on a template", date="10/8/21",
                           title="Weighted Random Occupations Chooser",tnpg="Team Team : Alif Abdullah, Eric Guo, Shadman Rakib Period 2",collection=finalDict,tab_space=": ", chosenJob=("Chosen Job: " + str(randomJob(finalDict))))


app.debug = True
app.run()