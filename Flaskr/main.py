from Flaskr import app
from flask import render_template, url_for, request, redirect, flash
from Flaskr.forms import loginForm, registerationForm


#creating a home page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
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

@app.route('/sinup', methods=['GET', 'POST'])
def register():
    form = registerationForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(f'Account created for {form.username.data}', category='success')
        return redirect(url_for('home'))
    elif not form.validate_on_submit() and request.method == 'POST':
        flash(f'Details are not valid!')
    return render_template('auth/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=loginForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(f'Logged in as {form.username.data}', category='success')
        return redirect(url_for('home'))
    elif not form.validate_on_submit() and request.method == 'POST':
        flash(f'Details are not valid!')
    return render_template('auth/login.html', form=form)