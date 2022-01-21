# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 30 min

### Prerequisites:

- A Digital Ocean Droplet

## Instructions

### Deploying Flask app with virtual host
1. Enable mod_wsgi
   ```
   sudo apt-get install libapache2-mod-wsgi-py3 python-dev
   ```
   ```
   sudo a2enmod wsgi 
   ```
2. Create flask app 
   ```
   cd /var/www
   ```
   - create a directory, it will be named "test1" in this guide
   - cd into it
   - create another folder, name it whatever you want it will be referred to as "test2"
   - cd into it
   ```
   sudo mkdir static templates
   ```
- create a file called __init__.py and sudo nano into it
   ```
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello():
   	return "Hi"
   if __name__ == "__main__":
   	app.run()
   ```
   ```
   sudo nano test1.wsgi 
   ```
   ```
   #!/usr/bin/python
   import sys
   import logging
   logging.basicConfig(stream=sys.stderr)
   sys.path.insert(0,"/var/www/FlaskApp/")

   from FlaskApp import app as application
   application.secret_key = 'Add your secret key'
   ```
3. Install Flask
- Activate your virtual environment
   ```
   sudo apt-get install python3-pip 
   ```
   ```
   sudo pip3 install Flask 
   ```
   Test it
   ```
   sudo python3 __init__.py 
   ```
4. Configure and enable virtual host 
   ```
   sudo nano /etc/apache2/sites-available/test1.conf
   ```
   Change mywebsite.com to the IP
   ```
   <VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/test1/test1.wsgi
		<Directory /var/www/test1/test2/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/test1/test2/static
		<Directory /var/www/test1/test2/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```
   Enable it with this
   ```
   sudo a2ensite FlaskApp
   ```
   Just in case do this
   ```
   sudo service apache2 restart 
   ```
You should be able to access your virtual host at your ip without the 5000

### Apps Successfully Deployed and the Devos Who Deployed Them
* https://docs.google.com/spreadsheets/d/1TXXdyeLUvXsuX2RuDW6cImMASGJ29B4JY1Lywvq-6i4/edit?resourcekey#gid=1813728504


### Resources
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
* https://flask.palletsprojects.com/en/2.0.x/deploying/mod_wsgi/

---

Accurate as of (last update): 2022-01-21

#### Contributors:  
Eric Guo, pd2
