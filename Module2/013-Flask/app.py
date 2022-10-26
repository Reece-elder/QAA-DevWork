# Flask is a web framework for Python, to create web apps of differing levels of complexity
# On its own is a backend web app, without any front end functionality

# `pip install flask` to install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/route")
def route():
    print("Cool thing")
    does_thing()
    return "Hello, this is a route!"

def does_thing():
    print(5 + 4)

@app.route("/shop/<id>")
def shop_page(id):
    return f"Page for shop {id}"

from flask import render_template
@app.route("/renderhtml")
def render_html():
    return render_template("index.html", name = "reece")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)