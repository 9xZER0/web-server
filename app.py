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

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    return '<h1> Trying To Signup.<br> You naughty </h1>'

@app.route("/forgot", methods = ['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template('forgot.html')
    return '<h1> Trying To reset password.<br> You naughty </h1>'

@app.route("/logout", methods = ['GET'])
def logout():
    return '<h1> Logout </h1>'

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, port = 8080)