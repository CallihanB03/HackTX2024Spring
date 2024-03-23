from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  response = form.response
  return 'Hello, World!'

@app.route('/<name>')
def hello_name(name):
  return 'Hello, ' + name

@app.route('/login')
def login():
  return 'Login page'



if __name__ == '__main__':
  app.run()