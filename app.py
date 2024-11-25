from flask import Flask, render_template, flash, redirect, request # type: ignore
import requests # type: ignore

app = Flask(__name__)
app.secret_key = "noSystemIsSafe"
API_URL = "http://127.0.0.1:8000"

# Home page
@app.route("/")
def home():
    try:
        response = requests.get(f"{API_URL}/")
        response.raise_for_status()
        message = response.json()
        return f"HELLO <br> {message['messages']} <br>"
    except requests.exceptions.Timeout:
        return "Can not connect to api"

# Login page
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    try:
        _email = request.form['email']
        _passWord = request.form['password']
        payload = {
            "email" : _email,
            "password" : _passWord
        }
        response = requests.post(f"{API_URL}/verify_user", json = payload)
        response.raise_for_status()
        message = response.json()
        if message['messages'] == "verified":
            return "Login SuccessFul"
        elif message['messages'] == "not found":
            return "No user found"
        return "Invalid Credentcial"
    except requests.exceptions.Timeout:
        return "Can not connect to api"

# Signup page
# @app.route("/signup", methods = ['GET', 'POST'])
# def signup():
#     if request.method == 'GET':
#         return render_template('signup.html')
#     _email = request.form['email']
#     _userName = request.form['username']
#     _passWord = request.form['password']

# Forgot password page
# @app.route("/forgot", methods = ['GET', 'POST'])
# def forgot():
#     if request.method == 'GET':
#         return render_template('forgot.html')
#     _email = request.form['email']

# Logout page
# @app.route("/logout", methods = ['GET'])
# def logout():
#     return '<h1> Logout </h1>'

# Dashboard
# @app.route("/dashboard")
# def dashboard():
#     return '<h1> Hello User </h1>'

# Profile
# @app.route("/profile")
# def profile():
#     return '<h1> Hello User Profile </h1>'

# Main function
if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True, port = 8080)