from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
  return 'Hello, World!'

@app.route('/account/<name>')
def hello_name(name):
  return 'Hello, ' + name

@app.route('/bets')
def bets():
    games = [
      {
        'id': 1,
        'name': 'Game 1',
        'gameTime': '12:00 PM',
        'teamA': 'Dallas Jims',
        'teamB': 'GS Warriors',
        'odds': -100
      },
      {
        'id': 2,
        'name': 'Game 2',
        'gameTime': '3:00 PM',
        'teamA': 'Team C',
        'teamB': 'Team D',
        'odds': +200
      },
      {
        'id': 3,
        'name': 'Game 3',
        'gameTime': '6:00 PM',
        'teamA': 'Team E',
        'teamB': 'Team F',
        'odds': +300
      }
    ]

    return jsonify(games)


if __name__ == '__main__':
    app.run(debug=True)