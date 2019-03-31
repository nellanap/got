from flask import flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db
from app.models import User, Response
from app.helpers import login_required, calculate_score, calculate_rank, calculate_points

@app.route('/')
@app.route('/index')
def index():

    # Gather responses, calculate scores, and order by score.
    submissions = Response.query.all()
    for s in submissions:
        s.score = calculate_score(s)
        s.rank = calculate_rank(s.score)
    db.session.commit()
    submissions = Response.query.order_by(Response.score.desc()).all()
    return render_template('index.html', submissions=submissions)




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

        # Query database for username and ensure username exists
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user is None:
            flash("Username does not exist")
            return render_template("login.html")

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


@app.route("/predict", methods=["GET", "POST"])
@login_required
def predict():
    """Fill out questionnaire"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        author = User.query.filter_by(id=session["user_id"]).first()
        response = Response.query.filter_by(author=author).first()

        # Check if user has made predictions before
        if response is not None:
            flash("You can only make one set of predictions")
            return render_template("rules.html")

        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
        q6 = request.form.get("q6")
        q7 = request.form.get("q7")
        q8 = request.form.get("q8")
        q9 = request.form.get("q9")
        q10 = request.form.get("q10")
        q11 = request.form.get("q11")
        q12 = request.form.get("q12")
        q13 = request.form.get("q13")
        q14 = request.form.get("q14")
        q15 = request.form.get("q15")
        q16 = request.form.get("q16")
        q17 = request.form.get("q17")
        q18 = request.form.get("q18")
        q19 = request.form.get("q19")
        q20 = request.form.get("q20")
        q21 = request.form.get("q21")
        q22 = request.form.get("q22")
        q23 = request.form.get("q23")
        q24 = request.form.get("q24")
        q25 = request.form.get("q25")
        q26 = request.form.get("q26")
        q27 = request.form.get("q27")
        q28 = request.form.get("q28")
        q29 = request.form.get("q29")
        q30 = request.form.get("q30")
        author = User.query.filter_by(id=session["user_id"]).first()

        new_response = Response(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10, \
        q11=q11, q12=q12, q13=q13, q14=q14, q15=q15, q16=q16, q17=q17, q18=q18, q19=q19, q20=q20, \
        q21=q21, q22=q22, q23=q23, q24=q24, q25=q25, q26=q26, q27=q27, q28=q28, q29=q29, q30=q30, author=author)
        db.session.add(new_response)
        db.session.commit()

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("predict.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # TODO Ensure username not already taken
        users = User.query.all()
        username = request.form.get("username")
        email = request.form.get("email")
        for u in users:
            if username == u.username:
                flash('That username is already taken')
                return render_template("register.html")
            if email == u.email:
                flash('That email is already taken')
                return render_template("register.html")

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

@app.route("/rules", methods=["GET", "POST"])
@login_required
def rules():
    """Rules"""

    return render_template("rules.html")



@app.route("/scores", methods=["GET", "POST"])
@login_required
def scores():
    """Show Scores"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        author = User.query.filter_by(username=request.form.get("username")).first()
        response = Response.query.filter_by(author=author).first()

        # Check if user has made predictions.
        if response is None:
            flash("That user hasn't made any predictions")
            return render_template("rules.html")
        score = calculate_score(response)
        points = calculate_points(response)
        return render_template("scores.html", author=author, response=response, score=score, points=points)

    # User reached route via GET (as by clicking a link)
    else:
        author = User.query.filter_by(id=session["user_id"]).first()
        response = Response.query.filter_by(author=author).first()

        # Check if user has made predictions.
        if response is None:
            flash("Make your predictions before seeing your score")
            return render_template("predict.html")
        score = calculate_score(response)
        points = calculate_points(response)
        return render_template("scores.html", author=author, response=response, score=score, points=points)
