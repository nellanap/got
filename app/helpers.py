from flask import redirect, render_template, request, session
from functools import wraps



def calculate_score(response):
    score = 0
    if response.q1 == 'Yes':
        score = score + 5
    if response.q2 == 'Yes':
        score = score + 5
    if response.q3 == 'Yes':
        score = score + 3
    if response.q4 == 'Yes':
        score = score + 3
    if response.q5 == 'Yes':
        score = score + 2
    if response.q6 == 'Yes':
        score = score + 2
    if response.q7 == 'Yes':
        score = score + 2
    if response.q8 == 'Yes':
        score = score + 2
    if response.q9 == 'Yes':
        score = score + 2
    if response.q10 == 'Yes':
        score = score + 2
    if response.q11 == 'Yes':
        score = score + 2
    if response.q12 == 'Yes':
        score = score + 2
    if response.q13 == 'Yes':
        score = score + 1
    if response.q14 == 'Yes':
        score = score + 1
    if response.q15 == 'Yes':
        score = score + 1
    if response.q16 == 'Daenerys':
        score = score + 3
    if response.q17 == 'Daenerys':
        score = score + 5
    if response.q18 == 'Jamie':
        score = score + 3
    if response.q19 == 'Jamie':
        score = score + 2
    if response.q20 == 'Yes':
        score = score + 2
    if response.q21 == 'Tyrion':
        score = score + 2
    if response.q22 == 'Jon':
        score = score + 1
    if response.q23 == 'Yes':
        score = score + 1
    if response.q24 == 'Hound':
        score = score + 1
    if response.q25 == 'Yes':
        score = score + 2
    if response.q26 == 'Yes':
        score = score + 3
    if response.q27 == 'Yes':
        score = score + 2
    if response.q28 == 'Yes':
        score = score + 1
    if response.q29 == 'Yes':
        score = score + 2
    if response.q30 == 'Yes':
        score = score + 5
    return score

def calculate_rank(score):
    if (score >= 0) and (score < 20):
        return 'Stonemen'
    if (score >= 20) and (score < 30):
        return 'Unsullied'
    if (score >= 30) and (score < 40):
        return 'Brotherhood'
    if (score >= 40) and (score < 50):
        return 'Iron Banker of Braavos'
    if (score >= 50) and (score < 60):
        return 'Nights Watch'
    if (score >= 60) and (score < 65):
        return 'Maester'
    if score == 65:
        return 'Warg'
    if score == 67:
        return 'Greenseer'
    if score == 68:
        return 'One-Eyed Raven'
    if score == 69:
        return 'Two-Eyed Raven'
    if score == 70:
        return 'Three-Eyed Raven'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
