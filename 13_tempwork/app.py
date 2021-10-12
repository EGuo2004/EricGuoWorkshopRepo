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
    x = random.randint(0, 998)
    y = 0
    for i in reader:
        y += reader[i] * 10
        if y > x:
            return i
            break

# Running the flask app with displayApp function
@app.route("/occupyflaskst")
def displayApp():
    fileReader()
    return render_template('tablified.html',heading="Eric Guo SoftDev K13 - To create a flask app that randomly chooses and displays an occupation based on a template 10/8/21",
                           title="Weighted Random Occupations Chooser",tnpg="Team Team : Alif Abdullah, Eric Guo, Shadman Rakib Period 2",collection=finalDict,chosenJob=("Chosen Job: " + str(randomJob(finalDict))))
    
    '''return ("Team Team - Alif Abdullah, Eric Guo, Shadman Rakib Period 2 <br><br>List of occupations: <br>" +
        str(list(finalDict.keys())[:len(list(finalDict.keys()))-1]) +
        "<br><br>Chosen Occupation: " + str(randomJob(finalDict)))
    '''

app.debug = True
app.run()


