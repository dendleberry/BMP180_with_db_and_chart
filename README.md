# BMP180_with_db_and_chart
A python, mariadb, js. project to collect persist and display pressure readings from a BMP180 sensor

Basic app to monitor the air pressure (in my case a sewer!). I used this on a raspberry pi with a BMP180 sensor.

There are lots of improvements that could be made but it suited my needs at the time.

There are a few prerequisits, Mariadb, python3, chart.js probably others I've forgotten

To start the web server run: sudo python3 sewer.py, 
this will log out the ip address of your pi on your network then start the web server.

You'll need to change the IP address in /static/code.js to the ip address of your pi.
