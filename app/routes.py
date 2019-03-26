from flask import flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password")
            return render_template("login.html")

        # Query database for username
        user = User.query.filter_by(username=request.form.get("username")).first()

        # TODO Ensure username exists

        # Ensure password is correct
        if not check_password_hash(user.password_hash, request.form.get("password")):
            flash("Invalid password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = user.id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # TODO Ensure username not already taken

        # Ensure username was submitted
        if not request.form.get("username"):
            flash('Must provide username')
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash('Must provide password')
            return render_template("register.html")

        # Ensure email was submitted
        elif not request.form.get("email"):
            flash("Must provide email")
            return render_template("register.html")

        # Add user to database
        username = request.form.get("username")
        email = request.form.get("email")
        password_hash = generate_password_hash(request.form.get("password"))

        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        # login the user
        session["user_id"] = new_user.id

        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")
