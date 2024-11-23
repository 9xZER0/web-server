from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Do You need Authentication ?"

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    return '<h1> Trying To Login.<br> You naughty </h1>'

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, port = 8080)