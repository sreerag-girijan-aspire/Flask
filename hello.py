from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {escape(name)}</p>"

@app.route("/about")
def about():
    return("This is About page")


@app.route("/product")
def product():
    return("This is product page")

@app.route("/product/laptop")
def laptop():
    return("This is laptop page")

app.add_url_rule("/desc","/about",about)

@app.route("/template")
def template():
    return render_template("index.html")