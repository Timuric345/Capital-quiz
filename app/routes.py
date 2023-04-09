from app import app
from game import Game
from flask import render_template, request, session

@app.route('/')
@app.route('/index')
def index():
 user = {'username'}
 return  render_template('index.html', user = user)

@app.route('/game', methods = ["GET", "POST"])
def game():
  #if request.method == "GET":
  new_game = Game(10)
  data = new_game.make_questions()
  session["data"] = data
  return render_template('game.html', data = data)
 
@app.route('/result', methods = ["POST"])
def result():
  score = 0
  #print(score)
  data = request.form
  for i in range(len(data)):
    #print(session['data'][1][i])
    if data[f"useranswer_{i}"].upper() == session['data'][1][i].upper():
      #print("True")
      score += 10
    #else:
    #  print("False")
    #print(data[f"useranswer_{i}"])
  return render_template('result.html', score = score)

@app.route('/rules', methods = ["get"])
def rules():
 return render_template('rules.html')