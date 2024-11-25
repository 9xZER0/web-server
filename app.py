from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "Do You need Authentication ?"

# Login page
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    return '<h1> Trying To Login.<br> You naughty </h1>'

# Signup page
@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    return '<h1> Trying To Signup.<br> You naughty </h1>'

# Forgot password page
@app.route("/forgot", methods = ['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template('forgot.html')
    return '<h1> Trying To reset password.<br> You naughty </h1>'

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