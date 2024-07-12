from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Changed text!!!!</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page for {username}</h1>'