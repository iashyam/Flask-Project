from flask import Flask
app = Flask(__name__) #creting a base for the router

#a router is something to write content in different pages

@app.route('/') #the home page
def hello():
    heading = "<h1>The Rest Frame</h1>"
    return heading

@app.route('/about')
def about():
    return "<h1>About The Rest Frame</h1>"