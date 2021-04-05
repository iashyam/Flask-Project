from flask import Flask, render_template, url_for, request
from forms import registerationForm, loginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '1dee4de2f1e0017b7aba8b5b8b2e4280'

#creating a home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#creating a blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

#creating an about page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sinup')
def register():
    form = registerationForm()
    return render_template('auth/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=loginForm()
    return render_template('auth/login.html', form=form)