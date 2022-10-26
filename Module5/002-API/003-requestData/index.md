# Lesson 
API requests can contain 4 things: 
- URL of the request
- Type of request 
- may include headers (key-value pairs)
- may include body (JSON)

The body is the 'Data' we are interested in, such as the contents of a form a user is filling out

# Tutorial
Modify the app.py to add a POST method which takes in a body 


```py
# Body request
@app.route('/penguin', methods = ['POST'])
def penguinRoute():
    data = request.get_json()
    return data

# Getting param from URL (localhost:5000/jeff)
@app.route('/penguin/<id>', methods = ['GET'])
def getPenguin(id):
    param = id
    return id

# Query params from our route (localhost:5000?colour=red)
@app.route('/penguin', methods = ['GET'])
def getPenguin():
    data = request.args
    return data

```

https://learning.postman.com/docs/writing-scripts/script-references/variables-list/ Show adding a JSON body to a request

```json
{
    "Name" : "{{$randomFirstName}}",
    "diet" : "fish"
}
```

# Exercise
Using request bodies, url params and query params create routes for the following (they should just return the data being passed in)
- Create new record
- Get record by ID 
- Update record(s) by query
- Delete record by id

