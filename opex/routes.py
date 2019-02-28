from flask import render_template, url_for, flash, redirect
from opex import app, db, bcrypt
from opex.forms import RegistrationForm, LoginForm
from opex.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
    #return render_template('home.html', posts=v_posts)  # posts is the argument name that will be passed to the template
    # and v_posts is the acutal variable with the posts

@app.route("/about")
def about():
    return render_template('about.html') 

@app.route("/register", methods=['GET','POST'])
def register():
	form  = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email=form.email.data, password = hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created. You can login to your account!','success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register',form=form)         


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'araj@gmail.com' and form.password.data == 'welcome123': 
			flash(f'Welcome {form.email.data}!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful!!', 'danger')     
	return render_template('login.html', title='Login', form=form) 