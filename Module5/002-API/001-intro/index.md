# Lesson 
Go through API slides 
Explain API (Application Programming Interface) - Specifies how separate components should interact, such as a website (front end) sending requests to the server (backend)
API is the building blocks, developers use the building blocks to create something

# Tutorial 
To create an API its easier to use an existing framework, Flask + Python / NodeJs + JavaScript / Java + Spring

Flask and Python - Flask is micro-framework meaning its simple but extendable 

Requires EC2 with port 5000 open

Python and flask are needed to run 
`sudo apt update`
`sudo apt install python3 python3-pip python3-venv`
`python3 -m venv venv`
`source venv/bin/activate`
`pip3 install flask`

`touch app.py` and add the following
```py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet!"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

```
Run the app with python3 app.py and access the browser to see the API working

# Exercise 
Using python and flask create a basic API that listens on a port and returns "Hello <your name>