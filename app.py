from flask import Flask, render_template, request

users = [{"user": "itzik", "pass": "12345"}, {"user": "moran", "pass": "12345"}]
app = Flask(__name__)

ary = ['itzik', 'moran']


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contactt")
def contactt():
    return render_template("contactt.html")



@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        if user == "itzik" or "moran" and pwd == "12345": 
            return render_template("sucess.html",user=user)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
