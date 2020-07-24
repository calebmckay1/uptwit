Had to reinstall the pipenv using pip3, errors
everytime i tried to lock the pipfile

Restating the entire week fresh leaning from Mike this time, his 
concepts are a little easier to explain for me..

ran " export FLASK_APP=hello.py "
then " flask run "

create home_routes which will house the routes and index for the app

the init file will house the creation of the web app and initiate it with
FLASK_APP=web_app
flask run

where web_app houses the main init file that initiate the creation of the
app

create a book route heres the basic syntax

@ name of module .route("/route name you want")
add function plus return what you want here


forgot to connect to database in order to fetch users and tweets and have a place
to store the tweets and users at.

Now i just have to train the predictive model, then deploy the app. View 
the readme for more info on commands to run 

for some reason when i use my username to predict, it throws error that user has no twets lol


Ask about database entry of if we just pull it directly from the twitter API

in order to make the postgresql database work i had to run 
'''
heroku run bash
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
'''