from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3c69b36a828b8c3d2954921ed15bddbe'

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
		flash(f'Account Created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register',form=form)         


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)      

if __name__ == '__main__':
	app.run(debug=True)