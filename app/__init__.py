from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
from app import routes
#source env/Scripts/activate
#export FLASK_APP=Capital-quiz.py
#flask run