# Lesson 
Go through types of API requests and the fact they are Request + Response
- GET
- POST
- PUT
- DELETE 

Head - Data about the request
Body - Data for the request

HTTP - Status codes
100 - 199: informational
200 - 299: success
300 - 399: redirection
400 - 499: client error
500 - 599: server error

# Tutorial
Adding HTTP API requests to our python app

```py
@app.route('/read', methods = ['GET'])
def read():
    return "Reading data"

# No way to test this method without using another tool.. Postman! Teach after this code
@app.route('/post', methods = ['POST'])
def read():
    return "Posting data"

```

<!-- if request.method == "post"  -->

POST, PUT and DELETE requests require signing up to postman https://web.postman.co and accessing the web app. Workarounds for people that can't access the web app are as follows: - Install the app, use remote PC, ask their IT department to access postman through firewall

Get everyone downloaded and setup on Postman if possible and show how to send a request to our server running on our public IP via port 5000

# Exercise
On your flask app create routes for GET, POST, PUT, DELETE and send Postman requests to each of these routes. Each route should return appropriate text