from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "noSystemIsSafe"
API_URL = "http://api"

# Home page
@app.route("/")
def home():

# Login page
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    _email = request.form['email']
    _passWord = request.form['password']

# Signup page
@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    _email = request.form['email']
    _userName = request.form['username']
    _passWord = request.form['password']

# Forgot password page
@app.route("/forgot", methods = ['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template('forgot.html')
    _email = request.form['email']

# Logout page
@app.route("/logout", methods = ['GET'])
def logout():
    return '<h1> Logout </h1>'

# Dashboard
@app.route("/dashboard")
def dashboard():
    return '<h1> Hello User </h1>'

# Profile
@app.route("/profile")
def profile():
    return '<h1> Hello User Profile </h1>'

# Main function
if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, port = 8080)