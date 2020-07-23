# uptwit
newly updated twitoff web app


download the repo and navigate to it by running this command in the terminal

'''git clone https://github.com/calebmckay1/uptwit.git
cd uptwit
'''

run 
'''pipenv install
pipenv shell
'''

to use
'''
FLASK_APP=web_app flask run
'''

setup the database

'''
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade

had to connect to the database DATABASE_URL = "sqlite:///db_name.db"