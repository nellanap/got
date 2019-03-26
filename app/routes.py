from flask import redirect, render_template, request, session
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

        # Ensure username was submitted
        #if not request.form.get("username"):
        #    return apology("must provide username", 403)

        # Ensure password was submitted
        #elif not request.form.get("password"):
        #    return apology("must provide password", 403)

        # Query database for username
        user = User.query.filter_by(username=request.form.get("username")).first()
        
        # Ensure username exists and password is correct
        #if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        #    return apology("invalid username and/or password", 403)

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

        # Ensure username was submitted
        #if not request.form.get("username"):
        #    return apology("must provide username")

        # Ensure password was submitted
        #elif not request.form.get("password"):
        #    return apology("must provide password")

        # Ensure password confirmation was submitted
        #elif not request.form.get("confirmation"):
        #    return apology("must provide password confirmation")

        # Ensure password and confirmation are the same
        #elif request.form.get("password") != request.form.get("confirmation"):
        #    return apology("must provide same password and confirmation")

        # Add user to database
        username = request.form.get("username")
        email = request.form.get("email")
        password_hash = generate_password_hash(request.form.get("password"))

        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        #if not result:
        #    return apology("must provide unique username")

        # login the user
        # session["user_id"] = result

        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")
