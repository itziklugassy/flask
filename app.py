from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Function to load users from a JSON file
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save users to a JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Load users from file at the start
users = load_users()

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contactt")
def contactt():
    return render_template("contactt.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["pass"]
        
        # Check if user already exists
        for user in users:
            if user['user'] == username:
                return "User already exists! Try a different username."

        # Add new user and save to file
        users.append({"user": username, "pass": password})
        save_users(users)

        return render_template("sucess.html", user=username)
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["pwd"]
        
        # Check if credentials are valid
        for user in users:
            if user['user'] == username and user['pass'] == password:
                return render_template("success.html", user=username)
        return "Invalid username or password!"  # or you might redirect back to login page with an error

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
