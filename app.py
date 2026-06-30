from flask import Flask, render_template, request
from database import save_comment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comment", methods=["POST"])
def comment():

    name = request.form["name"]
    email = request.form["email"]
    comment = request.form["comment"]

    save_comment(name, email, comment)

    return "<h2>Thank You! Your comment has been saved.</h2><br><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)