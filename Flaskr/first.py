from flask import Flask, url_for, render_template, redirect, request
from forms import registerForm
from markupsafe import escape
app = Flask(__name__) #creting a base for the router
app.config['SECRET_KEY'] = '123hrk34j45j5k3k1k'

#a router is something to write content in different pages
#adding varibale in url


@app.route('/') #the home page
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/register')
def login():
    form = loginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login_from.html', form=form)

# @app.route('/<name>')
# def about(name):
#     return "<h1>The page of {}</h1>".format(escape(name))

# @app.route('/postid=<pid>')
# def post(pid):
#     return "<h1>This is post number %s</h2>" %escape(pid)

# with app.test_request_context():
#     print(url_for('about', name='Shyam Sunder'))


