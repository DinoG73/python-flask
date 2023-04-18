from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html", textVar="Testing", user="Bruno", boolean=True,)

@auth.route('logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
            pass
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
            pass
        elif password1 != password2:
            flash('Passwords dont\'t match.', category='error')
            pass
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
            pass
        else:
            # add user to database
            flash('Account created!', category='success')
                        
    return render_template("sign_up.html")
