from flask import Flask
import csv
import random

app = Flask(__name__)

@app.route("/")
def index():
    job_and_prob = {}

    with open ("occupations.csv", "r") as f:

            csv_reader = csv.reader(f, delimiter=",")
            next(csv_reader)
            sum = 0.0

            for value in csv_reader:
                            if(value[0] == "Total"):
                                    continue
                            sum = sum + (10 * float(value[1])) #adding the values
                            job_and_prob[sum] = value[0]




            randNum = random.randrange(998) #random number
            for percent in job_and_prob.keys():
                if(percent >= randNum): #if it's below the value that means it's in between it and the value before it - elsewise we know it's above the value so we don't actually need another logic operator
                        returnstring = '<h2>The Nameless Team: Patrick Ging, Eric Guo, Hebe Huang</h2> </hr>'
                        returnstring += '<h2>Your job is ' +  job_and_prob.get(percent) + '</h2></br>'
                        returnstring += "<table> <tr> <th> Possible Jobs </th> </tr>";
                        returnstring += "<tr> <td> Management </tr></td>"
                        returnstring += "<tr> <td> Buisness and Financial operations </tr></td>"
                        returnstring += "<tr> <td> Computer and Mathematical </tr></td>"
                        returnstring += "<tr> <td> Architecture and Engineering </tr></td>"
                        returnstring += "<tr> <td> Life, Physical and Social Science </tr></td>"
                        returnstring += "<tr> <td> Community and Social Service </tr></td>"
                        returnstring += "<tr> <td> Legal </tr></td>"
                        returnstring += "<tr> <td> Education, training and library </tr></td>"
                        returnstring += "<tr> <td> Arts, design, entertainment, sports and media </tr></td>"
                        returnstring += "<tr> <td> Healthcare practioners and technical </tr></td>"
                        returnstring += "<tr> <td> Healthcare support </tr></td>"
                        returnstring += "<tr> <td> Protective service </tr></td>"
                        returnstring += "<tr> <td> Food preparation and serving </tr></td>"
                        returnstring += "<tr> <td> Building and grounds cleaning and maintenance </tr></td>"
                        returnstring += "<tr> <td> Personal care and service </tr></td>"
                        returnstring += "<tr> <td> Sales </tr></td>"
                        returnstring += "<tr> <td> Office and administrative support </tr></td>"
                        returnstring += "<tr> <td> Farming, fishing and forestry </tr></td>"
                        returnstring += "<tr> <td> Construction and extraction </tr></td>"
                        returnstring += "<tr> <td> Installation, maintenance and repair </tr></td>"
                        returnstring += "<tr> <td> Production </tr></td>"
                        returnstring += "<tr> <td> Transportation and material moving </tr></td>"
                        returnstring += "</table>"
                        return returnstring

if __name__ == "__main__":
    app.debug = True
    app.run()
